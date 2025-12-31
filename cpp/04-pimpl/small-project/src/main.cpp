
#include "./abstract-part/MyAbstractClass.hpp"

#include <iostream>
#include <cstdlib> // EXIT_SUCCESS

int main()
{
  std::cout << "BEGIN" << std::endl;

  {
    std::cout << "===== ===== ===== ===== =====" << std::endl;
    std::cout << "MyAbstractClass::createAsShared()" << std::endl;
    auto myInstance = MyAbstractClass::createAsShared();
    myInstance->myMethod();
  }

  {
    std::cout << "===== ===== ===== ===== =====" << std::endl;
    std::cout << "MyAbstractClass::createAsUnique()" << std::endl;
    auto myInstance = MyAbstractClass::createAsUnique();
    myInstance->myMethod();
  }

  std::cout << "END" << std::endl;

  return EXIT_SUCCESS;
}
