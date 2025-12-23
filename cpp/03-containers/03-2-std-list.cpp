
#include <cstdio> // <= EXIT_SUCCESS
#include <iostream>
#include <string>
#include <list>
// #include <cstring>
#include <algorithm> // std::find, std::sort
#include <cassert>
#include <stdint.h>

int main()
{

    {
        // PUSH BACK (FAST)

        std::list<int32_t> myIntList;

        assert(myIntList.size() == 0);

        myIntList.push_back(1); // FAST

        assert(myIntList.size() == 1);

        myIntList.push_back(2); // FAST

        assert(myIntList.size() == 2);

        myIntList.push_back(3); // FAST

        assert(myIntList.size() == 3);

        myIntList.push_back(4); // FAST

        assert(myIntList.size() == 4);

        auto it = myIntList.begin();
        assert((*it) == 1);
        ++it;
        assert((*it) == 2);
        ++it;
        assert((*it) == 3);
        ++it;
        assert((*it) == 4);
    }

    {
        // PUSH FRONT (FAST -> and simpler/faster to achieve than with std::vector)

        std::list<int32_t> myIntList;

        assert(myIntList.size() == 0);

        myIntList.push_front(1); // FAST

        assert(myIntList.size() == 1);

        myIntList.push_front(2); // FAST

        assert(myIntList.size() == 2);

        myIntList.push_front(3); // FAST

        assert(myIntList.size() == 3);

        myIntList.push_front(4); // FAST

        assert(myIntList.size() == 4);

        auto it = myIntList.begin();
        assert((*it) == 4); // is now first
        ++it;
        assert((*it) == 3); // is now second
        ++it;
        assert((*it) == 2); // is now third
        ++it;
        assert((*it) == 1); // is now last
    }

    {
        // LOOP (SLOW -> memory is NOT aligned/contiguous -> many "memory jumps" -> std::vector is FASTER)

        std::list<int32_t> myIntList;
        myIntList.push_back(1); // FAST
        myIntList.push_back(2); // FAST
        myIntList.push_back(3); // FAST
        myIntList.push_back(4); // FAST

        // iterator for loop (SLOW)
        int32_t valIndex = 1;
        for (auto it = myIntList.begin(); it != myIntList.begin(); ++it) {
            assert((*it) == (valIndex++));
        }

        // shorthand for loop (SLOW)
        valIndex = 1;
        for (int32_t currVal : myIntList) {
            assert(currVal == (valIndex++));
        }
    }

    {
        // LOOP (SLOW -> memory is NOT aligned/contiguous -> many "memory jumps" -> std::vector is FASTER)

        std::list<int32_t> myIntList;
        myIntList.push_back(1); // FAST
        myIntList.push_back(2); // FAST
        myIntList.push_back(3); // FAST
        myIntList.push_back(4); // FAST

        auto it = std::find(myIntList.begin(), myIntList.end(), 3);

        if (it == myIntList.end()) {
            // not found
        } else {
            // found
            assert((*it) == 3);
        }
    }

    {
        // LOOP (SLOW -> memory is NOT aligned/contiguous -> many "memory jumps" -> std::vector is FASTER)

        std::list<int32_t> myIntList;
        myIntList.push_back(1); // FAST
        myIntList.push_back(2); // FAST
        myIntList.push_back(3); // FAST
        myIntList.push_back(4); // FAST

        auto it = std::find_if(myIntList.begin(), myIntList.end(), [](int32_t currVal) -> bool {
            return currVal == 3;
        });

        if (it == myIntList.end()) {
            // not found
        } else {
            // found
            assert((*it) == 3);
        }
    }

    {
        // ERASE ANYWHERE (FAST -> no reallocation needed -> std::vector is SLOWER)

        std::list<int32_t> myIntList;
        myIntList.push_back(1); // FAST
        myIntList.push_back(2); // FAST
        myIntList.push_back(3); // FAST
        myIntList.push_back(4); // FAST

        assert(myIntList.size() == 4);

        auto it = myIntList.begin();
        assert((*it) == 1);
        ++it;
        assert((*it) == 2);
        ++it;
        assert((*it) == 3);
        ++it;
        assert((*it) == 4);

        it = myIntList.begin();
        ++it; // is now second element

        myIntList.erase(it); // remove "2", no realloc (FAST)

        assert(myIntList.size() == 3);

        it = myIntList.begin();
        assert((*it) == 1);
        ++it;
        assert((*it) == 3);
        ++it;
        assert((*it) == 4);
    }

    {
        // SORT (SLOW -> memory is NOT aligned/contiguous -> many "memory jumps" -> std::vector is FASTER)

        std::list<int32_t> myIntList;
        myIntList.push_back(4); // FAST
        myIntList.push_back(3); // FAST
        myIntList.push_back(2); // FAST
        myIntList.push_back(1); // FAST

        assert(myIntList.size() == 4);
        auto it = myIntList.begin();
        assert((*it) == 4);
        ++it;
        assert((*it) == 3);
        ++it;
        assert((*it) == 2);
        ++it;
        assert((*it) == 1);

        // std::list expose a sort(...) method, this help since std::sort will not work on std::list
        myIntList.sort([](int32_t leftVal, int32_t rightVal) -> int {
            // return negative val -> means left < right
            // return zero val -----> means left == right
            // return positive val -> means left > right

            // shortcut: "right value subtract left value" -> ascending sorting order
            return rightVal - leftVal;

            // // shortcut: "left value subtract right value" -> descending sorting order
            // return leftVal - rightVal;
        });

        assert(myIntList.size() == 4);
        it = myIntList.begin();
        assert((*it) == 1);
        ++it;
        assert((*it) == 2);
        ++it;
        assert((*it) == 3);
        ++it;
        assert((*it) == 4);
    }

    return EXIT_SUCCESS;
}
