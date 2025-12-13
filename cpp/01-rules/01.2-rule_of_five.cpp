
#include <iostream>
#include <cstdlib>

//
//
//

//
//
//

class RuleOfFive {

public:
  // default constructor
  // ---> note: we could have used a std::string_view here
  RuleOfFive(const std::string& message) {
    std::cout << "DEFAULT CTOR (" << message << ")" << std::endl;
    _message = message; // this will make a hard copy
  }

  // copy constructor
  RuleOfFive(const RuleOfFive& other) {
    std::cout << "COPY CTOR (this=" << _message << ", other=" << other._message << ")" << std::endl;
    // private attribute"_message" from "other" is accessible
    // -> this is because we're technically "inside" a method of RuleOfFive
    _message = other._message; // this will make a hard copy
  }

  // move constructor
  RuleOfFive(RuleOfFive&& other) {
    std::cout << "MOVE CTOR (this=" << _message << ", other=" << other._message << ")" << std::endl;
    // private attribute"_message" from "other" is accessible
    // -> this is because we're technically "inside" a method of RuleOfFive

    // this will NOT make a hard copy but "swap" the variables and the owners of their allocated memory
    _message = std::move(other._message);
  }

  // copy operator assignment
  RuleOfFive& operator=(const RuleOfFive& other) {
    std::cout << "ASSIGN OPERATOR (this=" << _message << ", other=" << other._message << ")" << std::endl;
    // private attribute"_message" from "other" is accessible
    // -> this is because we're technically "inside" a method of RuleOfFive
    _message = other._message; // this will make a hard copy
    // must return a reference
    return *this;
  }

  // move operator assignment
  RuleOfFive& operator=(RuleOfFive&& other) {
    std::cout << "MOVE ASSIGN OPERATOR (this=" << _message << ", other=" << other._message << ")" << std::endl;
    // private attribute"_message" from "other" is accessible
    // -> this is because we're technically "inside" a method of RuleOfFive

    // this will NOT make a hard copy but "swap" the variables and the owners of their allocated memory
    _message = std::move(other._message);

    // must return a reference
    return *this;
  }

  // destructor
  ~RuleOfFive() {
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
  std::string _message = "<default value>";

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

    RuleOfFive classA("A");
    RuleOfFive classB(classA);

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;
  }

  {
    std::cout << " ========= SCOPE 2 (OP ASSIGN) ========= " << std::endl;

    RuleOfFive classA("A");
    RuleOfFive classB("B");

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;

    classA = classB;

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;
  }

  {
    std::cout << " ========= SCOPE 3 (MOVE CTOR) ========= " << std::endl;

    RuleOfFive classA("A");
    RuleOfFive classB(std::move(classA));

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;
  }

  {
    std::cout << " ========= SCOPE 4 (Move OP ASSIGN) ========= " << std::endl;

    RuleOfFive classA("A");
    RuleOfFive classB("B");

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;

    classA = std::move(classB);

    std::cout << "classA.getMessage() => " << classA.getMessage() << std::endl;
    std::cout << "classB.getMessage() => " << classB.getMessage() << std::endl;
  }

  std::cout << "start" << std::endl;


  return EXIT_SUCCESS;
}
