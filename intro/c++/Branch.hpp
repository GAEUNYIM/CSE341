#include <string>

using namespace std;

#ifndef _Branch_hpp
#define _Branch_hpp

class Branch {
public:
    Branch(string& cond) : cond(cond) {}

    string toString() {
        return "Branch: " + cond;
    }

protected:
    string& cond;
};

#endif
