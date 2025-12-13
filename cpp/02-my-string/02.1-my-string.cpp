
#include <cstdio> // <= EXIT_SUCCESS
#include <iostream>
#include <string>
#include <memory>
#include <cstring>
#include <cassert>
#include <stdint.h>


class MyString
{
private:
    std::size_t _size = 0;
    std::unique_ptr<char[]> _data;

public:
    // constructor (default)
    MyString() = default;

    // destructor (default) -> made virtual should anyone wish to use MyString as a parent class
    virtual ~MyString() = default;

    // constructor (from char pointer)
    MyString(const char* inData)
    {
        _size = strlen(inData);
        _data = std::make_unique<char[]>(_size + 1);
        std::memset(_data.get(), 0, _size + 1); // safety (overkill?)
        std::memcpy(_data.get(), inData, _size); // bytes level memory copy
    }

    // constructor (copy)
    MyString(const MyString& other)
    {
        if (this == &other)
            return;
        _size = other._size;
        _data = std::make_unique<char[]>(_size + 1);
        std::memset(_data.get(), 0, _size + 1); // safety (overkill?)
        std::memcpy(_data.get(), other._data.get(), _size); // bytes level memory copy
    }

    // constructor (move)
    MyString(MyString&& other)
    {
        if (this == &other)
            return;
        std::swap(_size, other._size);

        // special case: std::swap is overloaded by std::unique_ptr, no realloc
        std::swap(_data, other._data);
    }

public:
    // assign operator (copy)
    MyString& operator=(const MyString& other)
    {
        if (this == &other)
            return *this;

        _size = other._size;
        _data = std::make_unique<char[]>(_size + 1);
        std::memset(_data.get(), 0, _size + 1); // safety (overkill?)
        std::memcpy(_data.get(), other._data.get(), _size); // bytes level memory copy
        return *this;
    }

    // assign operator (move)
    MyString& operator=(MyString&& other)
    {
        if (this == &other)
            return *this;

        std::swap(_size, other._size);

        // special case: std::swap is overloaded by std::unique_ptr, no realloc
        std::swap(_data, other._data);

        return *this;
    }

public:
    bool operator==(const MyString& other) const
    {
        if (_size != other._size)
            return false;
        return strncmp(_data.get(), other._data.get(), _size) == 0;
    }
    bool operator<(const MyString& other) const
    {
        // the added +1 is to compare the '\0', this handle string of different size
        const std::size_t minSize = std::min(this->_size, other._size);

        // use the safe strncmp(...) -> and NOT the unsafe strcmp(...)
        const int cmpVal = std::strncmp(_data.get(), other._data.get(), minSize + 1);
        return (cmpVal < 0);
    }

    // HACK: reuse operator ==
    bool operator!=(const MyString& other) const
    {
        return !MyString::operator==(other);
    }
    // HACK: reuse operator == and <
    bool operator>(const MyString& other) const
    {
        return !MyString::operator==(other) && !MyString::operator<(other);
    }
    // HACK: reuse operator == and <
    bool operator<=(const MyString& other) const
    {
        return MyString::operator==(other) || MyString::operator<(other);
    }
    // HACK: reuse operator == and <
    bool operator>=(const MyString& other) const
    {
        return MyString::operator==(other) || !MyString::operator<(other);
    }

public:

    // specialized handling of const char pointers
    bool operator==(const char* inData) const
    {
        const std::size_t dataSize = strlen(inData);
        if (_size != dataSize)
            return false;
        return strncmp(_data.get(), inData, _size) == 0;
    }

    // specialized handling of const char pointers
    bool operator<(const char* inData) const
    {
        // the added +1 is to compare the '\0', this handle string of different size
        const std::size_t minSize = std::min(this->_size, strlen(inData));

        // use the safe strncmp(...) (and NOT the unsafe strcmp(...))
        const int cmpVal = std::strncmp(_data.get(), inData, minSize + 1);
        return (cmpVal < 0);
    }

    // HACK: reuse operator ==
    bool operator!=(const char* inData) const
    {
        return !MyString::operator==(inData);
    }
    // HACK: reuse operator == and <
    bool operator>(const char* inData) const
    {
        return !MyString::operator==(inData) && !MyString::operator<(inData);
    }
    // HACK: reuse operator == and <
    bool operator<=(const char* inData) const
    {
        return MyString::operator==(inData) || MyString::operator<(inData);
    }
    // HACK: reuse operator == and <
    bool operator>=(const char* inData) const
    {
        return MyString::operator==(inData) || !MyString::operator<(inData);
    }

public:
    friend std::ostream& operator<<(std::ostream& os, const MyString& data);
};

std::ostream& operator<<(std::ostream& os, const MyString& data)
{
    os << data._data.get();
    return os;
}

int main()
{

    {
        const char* k_value1 = "MY_VALUE_1";
        const char* k_value2 = "MY_VALUE_2";


        MyString myStr1 = k_value1;

        assert(myStr1 == k_value1);
        assert(myStr1 != k_value2);


        MyString myStr2 = k_value1;

        assert(myStr2 == k_value1);
        assert(myStr2 != k_value2);


        MyString myStr3 = k_value2;

        assert(myStr3 == k_value2);
        assert(myStr3 != k_value1);

        assert(myStr1 == myStr2);
        assert(!(myStr1 != myStr2));
        assert(myStr1 != myStr3);
        assert(myStr2 != myStr3);
        assert(!(myStr1 == myStr3));
        assert(!(myStr2 == myStr3));

        myStr2 = myStr3; // copy

        assert(myStr1 == k_value1);
        assert(myStr2 == k_value2); // now is value2
        assert(myStr3 == k_value2);
        assert(myStr2 == myStr3);
        assert(myStr1 != myStr2);
        assert(myStr1 != myStr3);

        myStr1 = std::move(myStr2); // move

        assert(myStr1 == k_value2); // now is value2
        assert(myStr2 == k_value1); // now is value1
        assert(myStr3 == k_value2);
        assert(myStr1 == myStr3);
        assert(myStr2 != myStr1);
        assert(myStr2 != myStr3);

        std::cout << "myStr1  -> " << myStr1 << std::endl;
        std::cout << "myStr2  -> " << myStr2 << std::endl;
        std::cout << "myStr3  -> " << myStr3 << std::endl;
        std::cout << "myStr1 == myStr2 -> " << (myStr1 == myStr2) << std::endl;
        std::cout << "myStr1 != myStr2 -> " << (myStr1 != myStr2) << std::endl;
        // std::cout << "myStr1 < myStr2 -> " << (myStr1 < myStr2) << std::endl;
        // std::cout << "myStr2 < myStr1 -> " << (myStr2 < myStr1) << std::endl;
    }

    std::cout << " ===== ===== ===== ===== =====" << std::endl;

    {
        const char* k_value0 = "1"; // is < to all
        const char* k_value1 = "11"; // is < to 0, is < to 2/3
        const char* k_value2 = "12"; // is > to 0/1/2, but < to 3
        const char* k_value3 = "3"; // is > to all

        std::cout << " ----- ----- -----" << std::endl;
        std::cout << "k_value1 < k_value1 -> " << bool(std::string(k_value1) < std::string(k_value1)) << std::endl;
        std::cout << "empty < k_value0 -> " << bool(std::string("") < std::string(k_value0)) << std::endl;
        std::cout << "k_value0 < k_value1 -> " << bool(std::string(k_value0) < std::string(k_value1)) << std::endl;
        std::cout << "k_value1 < k_value2 -> " << bool(std::string(k_value1) < std::string(k_value2)) << std::endl;
        std::cout << "k_value2 < k_value3 -> " << bool(std::string(k_value2) < std::string(k_value3)) << std::endl;

        std::cout << "k_value3 < k_value2 -> " << bool(std::string(k_value3) < std::string(k_value2)) << std::endl;
        std::cout << "k_value2 < k_value1 -> " << bool(std::string(k_value2) < std::string(k_value1)) << std::endl;

        std::cout << " ----- ----- -----" << std::endl;
        std::cout << "MS(k_value1) < MS(k_value1) -> " << bool(MyString(k_value1) < MyString(k_value1)) << std::endl;
        std::cout << "MS(empty) < MS(k_value1) -> " << bool(MyString("") < MyString(k_value0)) << std::endl;
        std::cout << "MS(k_value0) < MS(k_value1) -> " << bool(MyString(k_value0) < MyString(k_value1)) << std::endl;
        std::cout << "MS(k_value1) < MS(k_value2) -> " << bool(MyString(k_value1) < MyString(k_value2)) << std::endl;
        std::cout << "MS(k_value2) < MS(k_value3) -> " << bool(MyString(k_value2) < MyString(k_value3)) << std::endl;

        std::cout << "MS(k_value3) < MS(k_value2) -> " << bool(MyString(k_value3) < MyString(k_value2)) << std::endl;
        std::cout << "MS(k_value2) < MS(k_value1) -> " << bool(MyString(k_value2) < MyString(k_value1)) << std::endl;

        // empty value, left is equal to right = false
        assert((MyString("") < MyString("")) == false);
        // confirm with std::string
        assert((MyString("") < MyString("")) == (std::string("") < std::string("")));

        // same value, left is equal to right = false
        assert((MyString(k_value1) < MyString(k_value1)) == false);
        // confirm with std::string
        assert((MyString(k_value1) < MyString(k_value1)) == (std::string(k_value1) < std::string(k_value1)));

        // left is < to right = true
        assert((MyString(k_value0) < MyString(k_value1)) == true);
        // confirm with std::string
        assert((MyString(k_value0) < MyString(k_value1)) == (std::string(k_value0) < std::string(k_value1)));

        // left is < to right = true
        assert((MyString(k_value1) < MyString(k_value2)) == true);
        // confirm with std::string
        assert((MyString(k_value1) < MyString(k_value2)) == (std::string(k_value1) < std::string(k_value2)));

        // left is < to right = true
        assert((MyString(k_value2) < MyString(k_value3)) == true);
        // confirm with std::string
        assert((MyString(k_value2) < MyString(k_value3)) == (std::string(k_value2) < std::string(k_value3)));

        // left is > to right = false
        assert((MyString(k_value3) < MyString(k_value2)) == false);
        // confirm with std::string
        assert((MyString(k_value3) < MyString(k_value2)) == (std::string(k_value3) < std::string(k_value2)));

        // left is > to right = false
        assert((MyString(k_value2) < MyString(k_value1)) == false);
        // confirm with std::string
        assert((MyString(k_value2) < MyString(k_value1)) == (std::string(k_value2) < std::string(k_value1)));

        //
        // reversed test
        //

        // empty value, left is equal to right = false
        assert((MyString("") > MyString("")) == false);
        // confirm with std::string
        assert((MyString("") > MyString("")) == (std::string("") > std::string("")));

        // same value, left is equal to right = false
        assert((MyString(k_value1) > MyString(k_value1)) == false);
        // confirm with std::string
        assert((MyString(k_value1) > MyString(k_value1)) == (std::string(k_value1) > std::string(k_value1)));

        // left is < to right = true
        assert((MyString(k_value0) > MyString(k_value1)) == false);
        // confirm with std::string
        assert((MyString(k_value0) > MyString(k_value1)) == (std::string(k_value0) > std::string(k_value1)));

        // left is < to right = true
        assert((MyString(k_value1) > MyString(k_value2)) == false);
        // confirm with std::string
        assert((MyString(k_value1) > MyString(k_value2)) == (std::string(k_value1) > std::string(k_value2)));

        // left is < to right = true
        assert((MyString(k_value2) > MyString(k_value3)) == false);
        // confirm with std::string
        assert((MyString(k_value2) > MyString(k_value3)) == (std::string(k_value2) > std::string(k_value3)));

        // left is > to right = false
        assert((MyString(k_value3) > MyString(k_value2)) == true);
        // confirm with std::string
        assert((MyString(k_value3) > MyString(k_value2)) == (std::string(k_value3) > std::string(k_value2)));

        // left is > to right = false
        assert((MyString(k_value2) > MyString(k_value1)) == true);
        // confirm with std::string
        assert((MyString(k_value2) > MyString(k_value1)) == (std::string(k_value2) > std::string(k_value1)));

    }

    return EXIT_SUCCESS;
}
