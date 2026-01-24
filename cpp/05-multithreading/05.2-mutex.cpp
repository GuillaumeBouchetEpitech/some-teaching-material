
#include <cstdio> // <= EXIT_SUCCESS
#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

int main()
{

    {
        // RAW MUTEX

        std::mutex commonMutex;

        auto threadedFunc = [&commonMutex](int threadIndex)
        {
            constexpr int k_totalCycles = 5;
            for (int ii = 0; ii < k_totalCycles; ++ii) {

                commonMutex.lock();

                // only one thread is logging at the same time
                std::cout << "THREAD[" << threadIndex << "] STEP " << ii << std::endl;

                commonMutex.unlock();

                if (ii + 1 < k_totalCycles) {
                    std::this_thread::sleep_for(std::chrono::milliseconds(500));
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

        for (auto& currThread : allThreads) {
            // always check is joinable
            if (currThread.joinable()) {
                // actual join
                currThread.join();
            }
        }

        std::cout << "STOP" << std::endl;
    }

    return EXIT_SUCCESS;
}


