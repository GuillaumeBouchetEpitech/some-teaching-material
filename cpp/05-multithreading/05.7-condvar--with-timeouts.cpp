
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
        bool waitUntilNotifiedOrTimedOut(std::unique_lock<std::mutex>& lock, float timeoutInSeconds)
        {
            this->_isNotified = false;

            // setup the timeout "point in time"
            const int64_t millisecondsToWait = int64_t(timeoutInSeconds * 1000.0f);
            auto timeoutPoint = std::chrono::system_clock::now();
            timeoutPoint += std::chrono::milliseconds(millisecondsToWait);

            // loop to avoid spurious wakeups
            while (_isNotified == false)
            {
                if (_condVar.wait_until(lock, timeoutPoint) == std::cv_status::timeout)
                {
                    // we did time out
                    return false;
                }
            }

            // we did not time out and got notified instead
            return true;
        }

        void notify()
        {
            this->_isNotified = true;
            this->_condVar.notify_one();
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

        const float timeoutInSec = 2.5f;
        const bool gotNotified = threadSynchronizer.waitUntilNotifiedOrTimedOut(lock, timeoutInSec);

        // when reaching this line -> we are locked again (threadsafe)

        if (gotNotified) {
            std::cout << "THREAD[" << threadIndex << "] GOT NOTIFIED!" << std::endl;
        } else {
            std::cout << "THREAD[" << threadIndex << "] DID TIMEOUT!" << std::endl;
        }

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

    std::cout << "NOTIFIED!" << std::endl;
    threadSynchronizer.notify();

    // will not notify and let the remaining thread time out

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



