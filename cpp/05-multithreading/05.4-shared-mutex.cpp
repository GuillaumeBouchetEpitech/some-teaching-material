
#include <cstdio> // <= EXIT_SUCCESS
#include <iostream>
#include <vector>
#include <algorithm> // std::find_if
#include <functional>
#include <memory>
#include <thread>
#include <mutex> // <= std::unique_lock
#include <shared_mutex> // <= std::shared_mutex

// !MARK: utils::NonCopyable

namespace utils {
    class NonCopyable
    {
    public:
        NonCopyable() = default;
        virtual ~NonCopyable() = default;

    public:
        // disable copy
        NonCopyable(const NonCopyable& other) = delete;
        NonCopyable& operator=(const NonCopyable& other) = delete;

        // disable move semantic
        NonCopyable(NonCopyable&& other) = delete;
        NonCopyable& operator=(NonCopyable&& other) = delete;
    };
};

// !MARK: IDummyPlayerSession

class IDummyPlayerSession
{
public:
    virtual ~IDummyPlayerSession() = default;

public:
    virtual uint32_t getPlayerId() const = 0;
    virtual uint32_t getHealth() const = 0;
    virtual bool isAlive() const = 0;

public:
    virtual void setHealth(uint32_t inHealth) = 0;
    virtual void applyDamage() = 0;
};

// !MARK: DummyPlayerSession

class DummyPlayerSession : public IDummyPlayerSession, public utils::NonCopyable
{
public:
    DummyPlayerSession(uint32_t inPlayerId)
        : _playerId(inPlayerId)
    {}

public:
    uint32_t getPlayerId() const override { return _playerId; }
    uint32_t getHealth() const override { return _health; }
    bool isAlive() const override { return _health > 0U; }

public:
    void setHealth(uint32_t inHealth) override { _health = inHealth; }
    void applyDamage() override { _health -= 1; }

public:
    static std::shared_ptr<IDummyPlayerSession> create(uint32_t inPlayerId)
    {
        return std::make_shared<DummyPlayerSession>(inPlayerId);
    }

private:
    uint32_t _playerId;
    uint32_t _health = 5U;
};

// !MARK: ThreadSafePlayerSessionManager

class ThreadSafePlayerSessionManager : public utils::NonCopyable
{
public:
    ThreadSafePlayerSessionManager()
    {
        // pre-allocate
        _allSessions.reserve(1228);
    }

public:
    std::shared_ptr<IDummyPlayerSession> addSession()
    {
        // only one write at a time
        std::unique_lock uniqueLock(_mutex);

        _allSessions.emplace_back(DummyPlayerSession::create(_currentId));

        std::cout << " -> [addSession] adding session, id=" << _currentId << std::endl;

        _currentId += 1;

        return _allSessions.back();
    }

    bool removeSession(uint32_t playerId)
    {
        // only one write at a time
        std::unique_lock uniqueLock(_mutex);

        // search session
        auto it = std::find_if(
            _allSessions.begin(),
            _allSessions.end(),
            [playerId](const std::shared_ptr<IDummyPlayerSession> session)
            {
                return session->getPlayerId() == playerId;
            });

        // session found?
        if (it == _allSessions.end())
        {
            std::cout << " -> [removeSession] session was not found, id=" << playerId << std::endl;
            return false;
        }

        std::cout << " -> [removeSession] session found, removing, id=" << playerId << std::endl;

        // remove session
        _allSessions.erase(it);
        return true;
    }

    void forEachSession(const std::function<void(std::shared_ptr<IDummyPlayerSession>)>& callback)
    {
        // allow multiple read at the same time
        std::shared_lock sharedLock(_mutex);

        std::cout << " -> [forEachSession] looping sessions (nonconst)" << std::endl;

        for (std::size_t index = 0; index < _allSessions.size(); ++index)
        {
            callback(_allSessions[index]);
        }
    }

    void forEachSession(const std::function<void(const std::shared_ptr<IDummyPlayerSession>)>& callback) const
    {
        // allow multiple read at the same time
        std::shared_lock sharedLock(_mutex);

        std::cout << " -> [forEachSession] looping sessions (const)" << std::endl;

        for (std::size_t index = 0; index < _allSessions.size(); ++index)
        {
            callback(_allSessions[index]);
        }
    }

    std::size_t totalSessions() const { return this->_allSessions.size(); }

private:
    // made mutable so it -> allow it to lock while used in a const method(s)
    mutable std::shared_mutex _mutex;

    std::vector<std::shared_ptr<IDummyPlayerSession>> _allSessions;

    uint32_t _currentId = 1;

};

// !MARK: main()

int main()
{
    // RAW SHARED MUTEX

    ThreadSafePlayerSessionManager sessionManager;

    constexpr uint32_t k_maxSession = 3;
    for (uint32_t ii = 0; ii < k_maxSession; ++ii)
    {
        // threadsafe session container (unique_lock -> only one write)
        auto newSession = sessionManager.addSession();

        // make the health start at X
        newSession->setHealth(1U + ii);
    }

    auto threadedFunc = [&sessionManager](int threadIndex)
    {
        std::vector<uint32_t> toRemove;
        toRemove.reserve(k_maxSession);

        constexpr int k_totalCycles = 5;
        for (int ii = 0; ii < k_totalCycles; ++ii)
        {
            sessionManager.forEachSession([&toRemove](std::shared_ptr<IDummyPlayerSession> currSession)
            {
                // threadsafe session container (shared_lock -> mutiple read)

                // decrease health
                if (currSession->isAlive())
                {
                    currSession->applyDamage();
                    std::cout << "session hp drop -> id=" << currSession->getPlayerId() << ", hp=" << currSession->getHealth() << std::endl;
                }

                if (!currSession->isAlive())
                {
                    std::cout << "dead session -> id=" << currSession->getPlayerId() << std::endl;

                    // must remove session
                    toRemove.emplace_back(currSession->getPlayerId());
                }

            });

            if (!toRemove.empty())
            {
                // remove dead sessions
                for (uint32_t playerId : toRemove)
                {
                    // threadsafe session container (unique_lock -> only one write)
                    sessionManager.removeSession(playerId);
                }

                while (sessionManager.totalSessions() < k_maxSession)
                {
                    // threadsafe session container (unique_lock -> only one write)
                    sessionManager.addSession();
                }
            }

            if (ii + 1 < k_totalCycles)
            {
                std::this_thread::sleep_for(std::chrono::milliseconds(100));
            }
        }
    };

    std::cout << "START" << std::endl;

    std::vector<std::thread> allThreads;

    // /!\ reserve() -> this will prevent thread reallocation!
    allThreads.reserve(2);

    // /!\ emplace_back() -> this will prevent thread copy constructor call!
    allThreads.emplace_back(threadedFunc, 1); // threadIndex=1
    allThreads.emplace_back(threadedFunc, 2); // threadIndex=2

    for (auto& currThread : allThreads)
    {
        // always check is joinable
        if (currThread.joinable())
        {
            // actual join
            currThread.join();
        }
    }

    //
    //
    //

    std::cout << std::endl;
    std::cout << " ##" << std::endl;
    std::cout << " ##" << std::endl;
    std::cout << " ###### PRINT DEBUG ######" << std::endl;

    std::cout << "total sessions: size=" << sessionManager.totalSessions() << std::endl;
    sessionManager.forEachSession([](const std::shared_ptr<IDummyPlayerSession> currSession)
    {
        // threadsafe session container (shared_lock -> mutiple read)

        std::cout << " -> print session: id=" << currSession->getPlayerId() << ", hp=" << currSession->getHealth() << std::endl;
    });

    std::cout << " ###### PRINT DEBUG ######" << std::endl;
    std::cout << " ##" << std::endl;
    std::cout << " ##" << std::endl;
    std::cout << std::endl;

    //
    //
    //

    std::cout << "STOP" << std::endl;

    return EXIT_SUCCESS;
}


