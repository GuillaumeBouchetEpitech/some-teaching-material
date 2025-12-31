
#pragma once

#include <cstring> // <= strrchr()
#include <iostream>

class TraceLogger
{
public:
  static std::string getTime();
};

// this will reduce the "__FILE__" macro to it's filename -> friendlier to read
#define D_MYLOG_FILENAME (strrchr(__FILE__, '/') ? strrchr(__FILE__, '/') + 1 : __FILE__)

// this is just to make the "D_MYLOG" macro source code easier to read
#define D_MYLOG_STACK D_MYLOG_FILENAME << "|" << __func__ << "|" << __LINE__

#define D_MYLOG_PREFIX "[" << TraceLogger::getTime() << "] (" << D_MYLOG_STACK << ") -> "

// one line logging macro
#define D_MYLOG(streamMsg)               \
  {                                      \
    std::cout << D_MYLOG_PREFIX << streamMsg << std::endl; \
  }

// one line logging macro
#define D_MYERR(streamMsg)               \
  {                                      \
    std::cerr << D_MYLOG_PREFIX << streamMsg << std::endl; \
  }
