
#pragma once

#include "utilities/NonCopyable.hpp"

#include <condition_variable>
#include <mutex>

// this class handle all locking and conditional variable interactions
class ThreadSynchronizer : public utils::NonCopyable
{
public:
  // this class act like a scoped lock but notify the condvar just before unlocking
  // -> it avoid forgetting to notify just before a scoped lock is destroyed
  class ScopedLockedNotifier {
    // friendship since we need access to the _mutex of the ThreadSynchronizer class
    friend ThreadSynchronizer;

  private:
    ThreadSynchronizer& _synchronizer;

  private:
    ScopedLockedNotifier(ThreadSynchronizer& synchronizer);

  public:
    ~ScopedLockedNotifier();
  };

public:
  ThreadSynchronizer() = default;

public:
  bool waitUntilNotified(std::unique_lock<std::mutex>& lock, float seconds = 0.0f);
  void notify();

public:
  std::unique_lock<std::mutex> makeScopedLock();
  ScopedLockedNotifier makeScopedLockNotifier();
  bool isNotified() const;

private:
  std::mutex _mutex;
  std::condition_variable _condVar;
  bool _isNotified = false;
};
