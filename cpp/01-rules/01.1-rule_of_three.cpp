
#include <iostream>
#include <cstdlib>

//
//
//

//
//
//

class RuleOfThree {

public:
  // default constructor
  // ---> note: we could have used a std::string_view here
  RuleOfThree(const std::string& message) {
    std::cout << "DEFAULT CTOR (" << message << ")" << std::endl;
    _message = message; // this will make a hard copy
  }

  // copy constructor
  RuleOfThree(const RuleOfThree& other) {
    std::cout << "COPY CTOR (this=" << _message << ", other=" << other._message << ")" << std::endl;
    // private attribute"_message" from "other" is accessible
    // -> this is because we're technically "inside" a method of RuleOfThree
    _message = other._message; // this will make a hard copy
  }

  // copy operator assignment
  RuleOfThree& operator=(const RuleOfThree& other) {
    std::cout << "ASSIGN OPERATOR (this=" << _message << ", other=" << other._message << ")" << std::endl;
    // private attribute"_message" from "other" is accessible
    // -> this is because we're technically "inside" a method of RuleOfThree
    _message = other._message; // this will make a hard copy
    // must return a reference
    return *this;
  }

  // destructor
  ~RuleOfThree() {
    std::cout << "DTOR (" << _message << ")" << std::endl;
    // usually for manual deallocation of anything manually allocated
    // -> we got none of that... ¯\_(ツ)_/¯
  }

public:
  // getter with;
  // -> "return is a reference"
  // ----> no copy, no creation, no slow (re-)allocation
  // -> "return is const"
  // ----> will make teh reference "readonly" to the "outside class/world"
  // -> "the method itself is const"
  // ----> this will ensure that only "const" method are allowed
  // ----> in short, it's the same as saying that the "this" itself is const
  const std::string& getMessage() const {
    return _message;
  }

private:
  std::string _message;

};

//
//
//

//
//
//

int main() {

  std::cout << "start" << std::endl;

  {
    std::cout << " ========= SCOPE 1 (COPY CTOR) ========= " << std::endl;

    RuleOfThree classA("A");
    RuleOfThree classB(classA);

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;
  }

  {
    std::cout << " ========= SCOPE 2 (OP ASSIGN) ========= " << std::endl;

    RuleOfThree classA("A");
    RuleOfThree classB("B");

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;

    classA = classB;

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;
  }

  std::cout << "start" << std::endl;


  return EXIT_SUCCESS;
}
