
#pragma once

#include "../AbstractTasksScheduler.hpp"

#include "./IObserverTaskScheduler.hpp"

#include "./TaskRunner.hpp"

#include "./ThreadSynchronizer.hpp"

#include <list>
#include <vector>
#include <thread>
#include <memory>

class ConcreteTasksScheduler : public AbstractTasksScheduler, public IObserverTaskScheduler
{
public:
  ConcreteTasksScheduler() = default;
  ~ConcreteTasksScheduler();

public:
  void initialize(uint32_t inTotalThreads) override;
  void shutdown() override;
  bool isRunning() const override;

public:
  void pushTask(const std::function<void()>& taskCallback) override;
  void waitUntilAllTasksAreCompleted() override;
  bool allTasksAreCompleted() const override;

private:
  // this is from the interface IObserverTaskScheduler
  void _notifyTaskCompleted(TaskRunner* taskRunner) override;

private:
  void _threadedMethod();

private:
  struct InternalTask
  {
  public:
    std::function<void()> callback = nullptr;
    std::shared_ptr<TaskRunner> taskRunner = nullptr;

  public:
    InternalTask(const std::function<void()>& taskCallback);
  };

private:
  std::vector<std::shared_ptr<TaskRunner>> _allTaskRunners;

  // std::list here since heavy use of the pop_front()/push_back() methods
  std::list<std::shared_ptr<TaskRunner>> _availableTaskRunners;
  std::list<std::shared_ptr<TaskRunner>> _busyTaskRunners;

  std::thread _thread;

  bool _isRunning = false;

  ThreadSynchronizer _setupSynchronizer;
  ThreadSynchronizer _taskSynchronizer;
  ThreadSynchronizer _allTaskSynchronizer;

  // std::list here since heavy use of the pop_front()/push_back() methods
  std::list<InternalTask> _allPlannedTasks;
  std::list<InternalTask> _allRunningTasks;

};
