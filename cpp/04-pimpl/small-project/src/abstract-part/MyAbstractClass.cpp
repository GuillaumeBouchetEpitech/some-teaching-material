
#include "MyAbstractClass.hpp"

#include "./internals/MyImplClass.hpp"

std::shared_ptr<MyAbstractClass> MyAbstractClass::createAsShared()
{
  // expose MyAbstractClass, while under the hood it's MyImplClass
  return std::make_shared<MyImplClass>();
}

std::unique_ptr<MyAbstractClass> MyAbstractClass::createAsUnique()
{
  // expose MyAbstractClass, while under the hood it's MyImplClass
  return std::make_unique<MyImplClass>();
}
