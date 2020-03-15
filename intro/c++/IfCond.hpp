#include "Branch.hpp"
#include <string>

using namespace std;

#ifndef _IfCond_hpp
#define _IfCond_hpp

class IfCond : public Branch {
public:
    IfCond(string& cond, string& then_b, string& else_b):
        Branch(cond), then_b(then_b), else_b(else_b) {}

    string toString() {
        return "IfCond: (" + cond + ", " + then_b + ", " + else_b + ")";
    }

private:
    string& then_b;
    string& else_b;
};

#endif
