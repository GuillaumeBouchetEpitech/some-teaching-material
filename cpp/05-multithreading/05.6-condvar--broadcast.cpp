
#include <cstdio> // <= EXIT_SUCCESS
#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable> // <= std::condition_variable

namespace utils {

    // !MARK: ThreadSynchronizer

    class ThreadSynchronizer
    {
    public:
        void waitUntilNotified(std::unique_lock<std::mutex>& lock)
        {
            this->_isNotified = false;

            // must loop to avoid spurious wakeups
            while (this->_isNotified == false)
            {
                // the locked thread will now wait (sleep) until notified (awoken)
                // the locked mutex will now allow another thread to lock it
                this->_condVar.wait(lock);
            }

            // if this line is reached -> this got notified
        }

        void broadcast()
        {
            this->_isNotified = true;

            // this will wake up "any and all" that is waiting
            this->_condVar.notify_all();
        }

    private:
        // std::mutex _mutex;
        std::condition_variable _condVar;
        bool _isNotified = false;
    };
};

// !MARK: main()

int main()
{
    // RAW CONDVAR

    std::mutex commonMutex;
    utils::ThreadSynchronizer threadSynchronizer;


    auto threadedFunc = [&commonMutex, &threadSynchronizer](int threadIndex)
    {
        auto lock = std::unique_lock(commonMutex);

        std::cout << "THREAD[" << threadIndex << "] STARTED" << std::endl;

        threadSynchronizer.waitUntilNotified(lock);

        // when reaching this line -> we are locked again (threadsafe)

        std::cout << "THREAD[" << threadIndex << "] STOPPED" << std::endl;
    };

    std::cout << "START" << std::endl;

    std::vector<std::thread> allThreads;

    // /!\ reserve() -> this will prevent thread reallocation!
    allThreads.reserve(2);

    // /!\ emplace_back() -> this will prevent thread copy constructor call!
    allThreads.emplace_back(threadedFunc, 1); // threadIndex=1
    allThreads.emplace_back(threadedFunc, 2); // threadIndex=2

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    std::cout << "BROADCAST!" << std::endl;
    threadSynchronizer.broadcast();

    for (auto& currThread : allThreads) {
        // always check is joinable
        if (currThread.joinable()) {
            // actual join
            currThread.join();
        }
    }

    std::cout << "STOP" << std::endl;

    return EXIT_SUCCESS;
}



