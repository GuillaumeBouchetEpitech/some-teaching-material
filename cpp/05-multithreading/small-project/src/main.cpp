
#include "./tasks-runner/AbstractTasksScheduler.hpp"

#include "./utilities/DeterministicRng.hpp"

#include <iostream>
#include <cstdio>
#include <thread>
#include <chrono>

int main()
{
  std::cout << "main: begin" << std::endl;

  //
  //
  //

  utils::DeterministicRng tmpRng;
  // only for clarification
  // -> this is not needed, default internal seed value is already 1
  tmpRng.setSeed(1);

  //
  //
  //

  auto taskScheduler = AbstractTasksScheduler::create();

  constexpr uint32_t k_totalThreads = 2;
  taskScheduler->initialize(k_totalThreads);

  //
  //
  //

  std::cout << "main: step begin" << std::endl;

  constexpr uint32_t k_totalTasks = 5;
  for (uint32_t ii = 0; ii < k_totalTasks; ++ii)
  {
    // pseudo random task sleep time, it's just easier that way...
    const int taskSleepTime = tmpRng.getRangedValue(50, 100);

    // push a task
    // -> which is in fact a simple callback
    // ---> std::function<void()>
    taskScheduler->pushTask([ii, taskSleepTime]() {
      std::cout << "task[" << ii << "]: begin (" << taskSleepTime << "ms)" << std::endl;

      // "fake work"
      // -> just make the thread of the task runner sleep...
      std::this_thread::sleep_for(std::chrono::milliseconds(taskSleepTime));

      std::cout << "task[" << ii << "]: end   (" << taskSleepTime << "ms)" << std::endl;
    });
  }

  taskScheduler->waitUntilAllTasksAreCompleted();

  std::cout << "main: step end" << std::endl;

  //
  //
  //

  // only for clarification
  // -> this is not needed, the scheduler will auto-shutdown at destruction
  taskScheduler->shutdown();

  //
  //
  //

  std::cout << "main: end" << std::endl;
  return EXIT_SUCCESS;
}