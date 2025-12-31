
#include "MyImplClass.hpp"

#include "./TraceLogger.hpp"

#include <iostream>

//
// here the implementation is very simple
// the main objective of using pimpl should be to separate any source code that
// is "weighting heavily on the compile time".
//
// Advisable usecases usually include:
// -> large (and slow to compile) third parties (ex: boost::asio templated logic)
// -> any justifiable "separation of concern" (implementation being unreachable)
// -> etc.
//

MyImplClass::MyImplClass()
{
  D_MYLOG("MyImplClass::ctor()");
}

MyImplClass::~MyImplClass()
{
  D_MYLOG("MyImplClass::dtor()");
}

void MyImplClass::myMethod()
{
  D_MYLOG("MyImplClass::myMethod()");
}
