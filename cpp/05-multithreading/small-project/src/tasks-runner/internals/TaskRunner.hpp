
#pragma once

#include "./IObserverTaskScheduler.hpp"

#include "./ThreadSynchronizer.hpp"

#include "utilities/NonCopyable.hpp"

#include <thread>

class TaskRunner : public utils::NonCopyable
{
public:
  TaskRunner(IObserverTaskScheduler& taskScheduler);
  ~TaskRunner();

public:
  void execute(const std::function<void()>& taskCallback);
  void shutdown();

public:
  bool isRunning() const;
  bool isAvailable() const;

private:
  void _threadedMethod();

private:
  IObserverTaskScheduler& _taskScheduler;

  std::thread _thread;
  ThreadSynchronizer _setupSynchronizer;
  ThreadSynchronizer _taskSynchronizer;

  bool _isRunning = false;
  bool _avoidBlocking = false;

  std::function<void()> _callback;

};
