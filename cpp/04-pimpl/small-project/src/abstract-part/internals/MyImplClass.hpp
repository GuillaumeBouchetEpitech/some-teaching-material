
#pragma once

#include "../MyAbstractClass.hpp"

#include <memory> // -> std::shared_ptr

class MyImplClass : public MyAbstractClass
{
public:
  MyImplClass();

  // avoid the "virtual" keyword in a child class if the parent already made it virtual
  ~MyImplClass();

public:
  // avoid the "virtual" keyword in a child class if the parent already made it virtual
  // the override keyword is mostly so that the compiler can check for errors
  void myMethod() override;
};
