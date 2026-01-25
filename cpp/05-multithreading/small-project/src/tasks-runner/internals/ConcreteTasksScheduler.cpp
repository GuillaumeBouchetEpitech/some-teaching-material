
#include "ConcreteTasksScheduler.hpp"

#include <algorithm> // <= std::find / std::find_if
#include <stdexcept> // <= std::runtime_error

ConcreteTasksScheduler::~ConcreteTasksScheduler()
{
  this->shutdown();
}

void ConcreteTasksScheduler::initialize(uint32_t inTotalThreads)
{
  if (_isRunning) {
    throw std::runtime_error("scheduler already running");
  }
  if (inTotalThreads > 50) {
    throw std::runtime_error("scheduler told to start with > 50 threads, here we will assume it was a human error");
  }

  //
  // launch task runners (consumers)

  _allTaskRunners.reserve(inTotalThreads);
  for (uint32_t ii = 0; ii < inTotalThreads; ++ii) {
    auto newTaskRunner = std::make_shared<TaskRunner>(*this);

    _allTaskRunners.push_back(newTaskRunner);
    _availableTaskRunners.push_back(newTaskRunner);
  }

  //
  // launch scheduler thread (producer)

  auto setupLock = _setupSynchronizer.makeScopedLock();

  _isRunning = false; // the producer's thread will set it to true

  // start the threaded method
  _thread = std::thread(&ConcreteTasksScheduler::_threadedMethod, this);

  // wait for the thread to be running

  // as we wait -> release the lock for other thread(s)
  _setupSynchronizer.waitUntilNotified(setupLock);
}

void ConcreteTasksScheduler::shutdown()
{
  if (!_isRunning) {
    // we're not running -> simple return
    // -> we could throw an exception but since this method is also called in the destructor it's best avoided
    // ---> thrown exceptions while in a destruction = undefined behaviour
    return;
  }

  // clear all the planned task(s) and wake up the running thread
  {
    auto lockNotifier = _taskSynchronizer.makeScopedLockNotifier();

    // this part is locked and will notify at the end of the scope

    _allPlannedTasks.clear();
  }

  waitUntilAllTasksAreCompleted();

  // stop the scheduler thread (producer)
  {
    auto lockNotifier = _taskSynchronizer.makeScopedLockNotifier();

    // this part is locked and will notify at the end of the scope

    _isRunning = false;
  }

  if (_thread.joinable()) {
    _thread.join();
  }

  _busyTaskRunners.clear();
  _availableTaskRunners.clear();
  _allTaskRunners.clear();

  // no more shared_ptr reference are held for the task runners (consumers)
  //
  // the TaskRunner destructor:
  // => should have been called
  // => will terminate their thread
}

bool ConcreteTasksScheduler::isRunning() const
{
  return _isRunning;
}

void ConcreteTasksScheduler::pushTask(const std::function<void()>& taskCallback)
{
  if (!_isRunning) {
    throw std::runtime_error("scheduler not running");
  }

  auto lockNotifier = _taskSynchronizer.makeScopedLockNotifier();

  // this part is locked and will notify at the end of the scope

  _allPlannedTasks.push_back(InternalTask(taskCallback));
}

void ConcreteTasksScheduler::waitUntilAllTasksAreCompleted()
{
  if (!_isRunning) {
    throw std::runtime_error("scheduler not running");
  }
    // make the (main) thread wait for all tasks to be completed

  auto lock = _allTaskSynchronizer.makeScopedLock();

  // this part is locked

  while (!allTasksAreCompleted())
  {
    // wait -> release the lock for other thread(s)
    _allTaskSynchronizer.waitUntilNotified(lock, 1.0f);
  }
}

bool ConcreteTasksScheduler::allTasksAreCompleted() const
{
  return (
    _allPlannedTasks.empty() &&
    _allRunningTasks.empty()
  );
}

void ConcreteTasksScheduler::_notifyTaskCompleted(TaskRunner* taskRunner)
{
  auto lockNotifier = _taskSynchronizer.makeScopedLockNotifier();

  // this part is locked and will notify at the end of the scope

  // find the "inter task" per "task runner" in the "running tasks list"
  auto itTask = std::find_if(
    _allRunningTasks.begin(),
    _allRunningTasks.end(),
    [taskRunner](const InternalTask& currTask) { return currTask.taskRunner.get() == taskRunner; });

  // defensive programming: this should never fail
  if (itTask == _allRunningTasks.end()) {
    return;
  }

  // move task runner from "busy" to available
  auto currTaskRunner = itTask->taskRunner;

  // first add it to the "available runners list"
  _availableTaskRunners.push_back(currTaskRunner);

  // then remove it to the "busy runners list"

  // find it first
  auto itTaskRunner = std::find(_busyTaskRunners.begin(), _busyTaskRunners.end(), currTaskRunner);

  // defensive programming: this should never fail
  if (itTaskRunner != _busyTaskRunners.end()) {
    // then erase it
    _busyTaskRunners.erase(itTaskRunner);
  }

  // now safe to erase the newly completed task from this list
  _allRunningTasks.erase(itTask);

  // check if no more tasks to run
  if (_allPlannedTasks.empty() && _allRunningTasks.empty())
  {
    // no more tasks left to run means we must wake up the potentially waiting (main?) thread
    // -> this is how the waitUntilAllTasksAreCompleted() method knows it can stop blocking
    _allTaskSynchronizer.notify();
  }
}

void ConcreteTasksScheduler::_threadedMethod()
{
  auto taskLock = _taskSynchronizer.makeScopedLock();

  // this part is locked

  {
    auto setupLockNotifier = _setupSynchronizer.makeScopedLockNotifier();

    // this part is locked and will notify at the end of the scope

    // done to tell the scheduler to stop blocking on the initialize()
    _isRunning = true;
  }

  // we're still locked

  while (_isRunning)
  {
    // wait -> release the lock for other thread(s)
    _taskSynchronizer.waitUntilNotified(taskLock);

    // this part is locked again

    if (!_isRunning)
    {
      // the shutdown() method was called
      break;
    }

    while (!_allPlannedTasks.empty())
    {
      if (_availableTaskRunners.empty()) {
        // no consumer available? just wait again...
        break;
      }

      // move consumer from free to busy
      auto taskRunner = _availableTaskRunners.front();
      _busyTaskRunners.push_back(taskRunner);
      _availableTaskRunners.pop_front();

      // get the next task
      InternalTask& currentTask = _allPlannedTasks.front();

      // associate it with a runner the available "task runner"
      currentTask.taskRunner = taskRunner;

      // tell the "task runner" to execute the task
      taskRunner->execute(currentTask.callback);

      // move the task from the "planned tasks list" to "running tasks list"
      _allRunningTasks.push_back(currentTask);
      _allPlannedTasks.pop_front();
    }
  }
}

ConcreteTasksScheduler::InternalTask::InternalTask(const std::function<void()>& taskCallback)
  : callback(taskCallback)
{}
