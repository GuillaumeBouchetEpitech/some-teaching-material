
#pragma once

#include "utilities/NonCopyable.hpp"

#include <functional>
#include <memory>

// forward declaration
class TaskRunner;

class IObserverTaskScheduler : public utils::NonCopyable
{
  // friendship so the runner can call _notifyTaskCompleted()
  friend TaskRunner;

public:
  virtual ~IObserverTaskScheduler() = default;

protected:
  virtual void _notifyTaskCompleted(TaskRunner* taskRunner) = 0;
};

