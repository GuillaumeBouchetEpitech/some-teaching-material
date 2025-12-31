
#pragma once

#include <memory> // -> std::shared_ptr/unique_ptr

class MyAbstractClass
{
public:
  MyAbstractClass() = default;

  // the destructor MUST be virtual
  // -> if not done, the destructor of the "child class" is not called...
  virtual ~MyAbstractClass() = default;

  // disallow copy/move constructor (this is done...  ...just because)
  MyAbstractClass(const MyAbstractClass&) = delete;
  MyAbstractClass(MyAbstractClass&&) = delete;

  // disallow assignment operator (this is done...  ...just because)
  MyAbstractClass& operator=(const MyAbstractClass&) = delete;
  MyAbstractClass& operator=(MyAbstractClass&&) = delete;

public:
  // here we have a "virtual pure method"
  virtual void myMethod() = 0;

public:
  // static method that instantiate the implementation behind the abstract class
  static std::shared_ptr<MyAbstractClass> createAsShared();
  static std::unique_ptr<MyAbstractClass> createAsUnique();

};
