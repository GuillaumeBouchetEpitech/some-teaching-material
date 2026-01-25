
#include "TaskRunner.hpp"


TaskRunner::TaskRunner(IObserverTaskScheduler& taskScheduler)
  : _taskScheduler(taskScheduler)
{
  auto setupLock = _setupSynchronizer.makeScopedLock();

  _isRunning = false; // the TaskRunner's thread will set it to true

  // launch the thread
  _thread = std::thread(&TaskRunner::_threadedMethod, this);

  // here we wait for the thread to be running and notify us to stop blocking

  // wait -> release the lock for other thread(s)
  _setupSynchronizer.waitUntilNotified(setupLock);
}

TaskRunner::~TaskRunner()
{
  shutdown();
}

void TaskRunner::execute(const std::function<void()>& taskCallback)
{
  auto lockNotifier = _taskSynchronizer.makeScopedLockNotifier();

  // this part is locked and will notify at the end of the scope

  _callback = taskCallback;
}

void TaskRunner::shutdown()
{
  if (!_isRunning)
  {
    // we're not running -> simple return
    // -> we could throw an exception but since this method is also called in the destructor it's best avoided
    // ---> thrown exceptions while in a destruction = undefined behaviour
    return;
  }

  // stop the runner thread (consumer)
  {
    auto lockNotifier = _taskSynchronizer.makeScopedLockNotifier();

    // this part is locked and will notify at the end of the scope

    _isRunning = false;
  }

  if (_thread.joinable()) {
    _thread.join();
  }
}


bool TaskRunner::isRunning() const
{
  return _isRunning;
}

bool TaskRunner::isAvailable() const
{
  return !_taskSynchronizer.isNotified();
}


void TaskRunner::_threadedMethod()
{
  auto taskLock = _taskSynchronizer.makeScopedLock();

  // this part is locked

  {
    auto setupLockNotifier = _setupSynchronizer.makeScopedLockNotifier();

    // this part is locked and will notify at the end of the scope

    // done to tell the runner to stop blocking in his constructor
    _isRunning = true;
  }

  // we're still locked

  while (_isRunning)
  {
    // wait -> release the lock for other thread(s)
    _taskSynchronizer.waitUntilNotified(taskLock);

    // this part is locked again

    if (!_isRunning) {
      // the shutdown() method was called
      break;
    }

    // the actual running of the task
    _callback();

    // task is now done, notify the scheduler
    // -> so this runner might be reassigned to another task
    _taskScheduler._notifyTaskCompleted(this);
  }
}

