
# Multithreading - "Tasks Runner" (small project)

## How to Use

```c++
#include "./tasks-runner/AbstractTasksScheduler.hpp"

#include <cstdio>
#include <thread>
#include <chrono>

int main()
{
    // note: taskScheduler is a unique_ptr
    auto taskScheduler = AbstractTasksScheduler::create();

    constexpr uint32_t k_totalThreads = 2;
    taskScheduler->initialize(k_totalThreads);

    // schedule a task
    // note: tasks are callbacks (std::function<void()>)
    taskScheduler->pushTask([]()
    {
        // ...simulated work...
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    });

    // schedule another task
    taskScheduler->pushTask([]()
    {
        // ...simulated work...
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    });

    // this will block the calling thread (here -> main thread)
    taskScheduler->waitUntilAllTasksAreCompleted();

    taskScheduler->shutdown();

    return EXIT_SUCCESS;
}
```

## How to Build

```bash
cmake -B ./build
cd ./build || exit 1
cmake --build . --parallel
```
...or just
```bash
sh sh_run.sh
```

## How to Run

```bash
./build/multi-threading
```

## Diagrams
### Sequence Diagram

```mermaid
---
title: Task Runner sequence
---

sequenceDiagram

    main->>TaskScheduler: push a new task to run

    Note over main,TaskScheduler: this wakes up the scheduler's thread
    TaskScheduler-->>TaskScheduler: check for any planned task
    Note over TaskScheduler: we have a task to run
    TaskScheduler-->>TaskScheduler: check for any available runner
    Note over TaskScheduler: we have a runner available

    TaskScheduler->>TaskRunner: tell the runner to execute
    Note over TaskScheduler,TaskRunner: this wakes up the runner's thread

    TaskRunner-->>TaskRunner: execute the task
    TaskRunner->>TaskScheduler: notify the task is done

    Note over TaskScheduler,TaskRunner: this wakes up the scheduler's thread
    TaskScheduler-->>TaskScheduler: check for any planned task
    Note over TaskScheduler: we don't have any tasks to run

    TaskScheduler->>main: notify the main thread we're done
    Note over main,TaskScheduler: will unblock the (potentially) waiting main thread


```

### Class Diagram

Some details:
* pImpl (pointer to implementation):
    * AbstractTasksScheduler::create() will hide the ConcreteTasksScheduler logic
* Producer-Consumer Pattern:
    * the TaskScheduler "produce" tasks
    * a TaskRunner "consume" tasks
* Observer pattern (simplified):
    * this was heavily simplified -> no subscribe/register methods, just a notify method
    * a TaskRunner will "notify" the TaskScheduler once a task is completed

```mermaid

---
title: Task Runner classes
---
classDiagram

    direction TD

    AbstractTasksScheduler <|-- ConcreteTasksScheduler
    IObserverTaskScheduler <|-- ConcreteTasksScheduler

    ConcreteTasksScheduler *-- TaskRunner
    TaskRunner o.. IObserverTaskScheduler
    ConcreteTasksScheduler *-- InternalTask
    InternalTask o.. TaskRunner

    ConcreteTasksScheduler *-- ThreadSynchronizer
    TaskRunner *-- ThreadSynchronizer
    ScopedLockedNotifier o.. ThreadSynchronizer

    class AbstractTasksScheduler{

        + std::unique_ptr<AbstractTasksScheduler> create()$

        + void initialize(uint32_t inTotalThreads)
        + void shutdown()
        + bool isRunning() const
        + void pushTask(const std::function<void()>& taskCallback)
        + void waitUntilAllTasksAreCompleted()
        + bool allTasksAreCompleted() const
    }
    <<abstract>> AbstractTasksScheduler

    class IObserverTaskScheduler {
    }
    <<interface>> IObserverTaskScheduler

    class ConcreteTasksScheduler {
    }

```
