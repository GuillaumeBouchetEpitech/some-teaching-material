
#pragma once

#include "utilities/NonCopyable.hpp"

#include <memory>
#include <functional>

class AbstractTasksScheduler : public utils::NonCopyable
{
public:
  static std::unique_ptr<AbstractTasksScheduler> create();

// public:
//   ~AbstractTasksScheduler() = default;

public:
  virtual void initialize(uint32_t inTotalThreads) = 0;
  virtual void shutdown() = 0;
  virtual bool isRunning() const = 0;

public:
  virtual void pushTask(const std::function<void()>& taskCallback) = 0;
  virtual void waitUntilAllTasksAreCompleted() = 0;
  virtual bool allTasksAreCompleted() const = 0;
};
