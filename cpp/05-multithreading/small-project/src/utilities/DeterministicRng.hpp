
#pragma once

#include <cstdint>

namespace utils {

class DeterministicRng {
public:
  DeterministicRng() = default;

public:
  void setSeed(int32_t seed);

public:
  int getValue();
  constexpr int64_t getMaxValue() const { return k_randMax; }

public:
  float getNormalizedValue();
  int getRangedValue(int minVal, int maxVal);
  float getRangedValue(float minVal, float maxVal);

private:
  static constexpr int64_t k_randMax = 2147483648;
  uint64_t _seed = 1;
};

} // namespace utils
