
#include "AbstractTasksScheduler.hpp"

#include "./internals/ConcreteTasksScheduler.hpp"

std::unique_ptr<AbstractTasksScheduler> AbstractTasksScheduler::create()
{
  return std::make_unique<ConcreteTasksScheduler>();
}
