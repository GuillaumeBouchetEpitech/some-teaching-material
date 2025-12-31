

#include "TraceLogger.hpp"

#include <ctime>
#include <format>

std::string TraceLogger::getTime() {
  std::time_t rawtime = std::time(0);
  std::tm* now = std::localtime(&rawtime);

  return std::format("{:0>2}:{:0>2}:{:0>2}", now->tm_hour, now->tm_min, now->tm_sec);
}
