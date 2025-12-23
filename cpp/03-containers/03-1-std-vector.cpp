
#include <cstdio> // <= EXIT_SUCCESS
#include <iostream>
#include <string>
#include <vector>
// #include <cstring>
#include <algorithm> // std::find, std::sort
#include <cassert>
#include <stdint.h>

int main()
{

    {
        // DEFAULT CAPACITY

        std::vector<int32_t> myIntVector;

        assert(myIntVector.size() == 0);
        assert(myIntVector.capacity() == 0);

        myIntVector.push_back(1); // will realloc (capacity < to new size)

        assert(myIntVector.size() == 1);
        assert(myIntVector.capacity() == 1);

        myIntVector.push_back(2); // will realloc (capacity < to new size)

        assert(myIntVector.size() == 2);
        assert(myIntVector.capacity() == 2);

        myIntVector.push_back(3); // will realloc (capacity < to new size)

        assert(myIntVector.size() == 3);
        assert(myIntVector.capacity() == 4); // /!\ HIGHER CAPACITY -> is power of 2 (<- 1,2,4,8,16)

        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 4); // DID NOT CHANGE -> was high enough
    }

    {
        // PRE-ALLOCATED CAPACITY

        std::vector<int32_t> myIntVector;

        assert(myIntVector.size() == 0);
        assert(myIntVector.capacity() == 0);

        myIntVector.reserve(10); // this will pre-allocate 10 elements

        assert(myIntVector.size() == 0);
        assert(myIntVector.capacity() == 10);

        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 10); // DID NOT CHANGE -> was high enough
    }

    {
        // ERASE LAST

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 10);

        myIntVector.pop_back(); // remove last, will never realloc (FAST)

        assert(myIntVector.size() == 3);
        assert(myIntVector.capacity() == 10);
    }

    {
        // ERASE ANYWHERE (SLOW)

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 10);
        assert(myIntVector.at(0) == 1);
        assert(myIntVector.at(1) == 2);
        assert(myIntVector.at(2) == 3);
        assert(myIntVector.at(3) == 4);

        myIntVector.erase(myIntVector.begin() + 1); // remove "2", will always realloc (SLOW)

        assert(myIntVector.size() == 3);
        assert(myIntVector.capacity() == 10);
        assert(myIntVector.at(0) == 1);
        assert(myIntVector.at(1) == 3);
        assert(myIntVector.at(2) == 4);
    }

    {
        // ERASE ANYWHERE (FAST)

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 10);
        assert(myIntVector.at(0) == 1);
        assert(myIntVector.at(1) == 2);
        assert(myIntVector.at(2) == 3);
        assert(myIntVector.at(3) == 4);

        std::swap(myIntVector.at(1), myIntVector.back()); // swap element at index 1 (value 1) with last element (value 4)
        myIntVector.pop_back(); // remove last, will never realloc (FAST)

        assert(myIntVector.size() == 3);
        assert(myIntVector.capacity() == 10);
        assert(myIntVector.at(0) == 1);
        assert(myIntVector.at(1) == 4); // used to be the last element before being swapped
        assert(myIntVector.at(2) == 3);
    }

    {
        // LOOP

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        // counting for loop (FAST)
        for (std::size_t ii = 0; ii < myIntVector.size(); ++ii) {
            assert(myIntVector.at(ii) == int32_t(ii + 1));
        }

        // iterator for loop (FAST)
        int32_t valIndex = 1;
        for (auto it = myIntVector.begin(); it != myIntVector.begin(); ++it) {
            assert((*it) == (valIndex++));
        }

        // shorthand for loop (FAST)
        valIndex = 1;
        for (int32_t currVal : myIntVector) {
            assert(currVal == (valIndex++));
        }
    }

    {
        // FIND (FAST)

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        auto it = std::find(myIntVector.begin(), myIntVector.end(), 3);

        if (it == myIntVector.end()) {
            // not found
        } else {
            // found
            assert((*it) == 3);
        }
    }

    {
        // FIND_IF (FAST)

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)

        auto it = std::find_if(myIntVector.begin(), myIntVector.end(), [](int32_t currVal) {
            return currVal == 3;
        });

        if (it == myIntVector.end()) {
            // not found
        } else {
            // found
            assert((*it) == 3);
        }
    }

    {
        // SORT (FAST)

        std::vector<int32_t> myIntVector;
        myIntVector.reserve(10); // this will pre-allocate 10 elements
        myIntVector.push_back(4); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(3); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(2); // will NOT realloc (capacity >= to new size)
        myIntVector.push_back(1); // will NOT realloc (capacity >= to new size)

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 10);
        assert(myIntVector.at(0) == 4);
        assert(myIntVector.at(1) == 3);
        assert(myIntVector.at(2) == 2);
        assert(myIntVector.at(3) == 1);

        std::sort(myIntVector.begin(), myIntVector.end(), [](int32_t leftVal, int32_t rightVal) {
            // return negative val -> means left < right
            // return zero val -----> means left == right
            // return positive val -> means left > right

            // shortcut: "right value subtract left value" -> ascending sorting order
            return rightVal - leftVal;

            // // shortcut: "left value subtract right value" -> descending sorting order
            // return leftVal - rightVal;
        });

        assert(myIntVector.size() == 4);
        assert(myIntVector.capacity() == 10);
        assert(myIntVector.at(0) == 1);
        assert(myIntVector.at(1) == 2);
        assert(myIntVector.at(2) == 3);
        assert(myIntVector.at(3) == 4);
    }

    return EXIT_SUCCESS;
}
