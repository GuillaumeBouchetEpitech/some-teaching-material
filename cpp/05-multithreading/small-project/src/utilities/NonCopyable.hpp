
#pragma once

namespace utils {

  class NonCopyable
  {
  public:
    NonCopyable() = default;
    virtual ~NonCopyable() = default;

  public:
    // disable copy
    NonCopyable(const NonCopyable& other) = delete;
    NonCopyable& operator=(const NonCopyable& other) = delete;

    // disable move semantic
    NonCopyable(NonCopyable&& other) = delete;
    NonCopyable& operator=(NonCopyable&& other) = delete;
  };

};
