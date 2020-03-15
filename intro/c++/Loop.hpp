#include "Branch.hpp"
#include <string>

using namespace std;

#ifndef _Loop_hpp
#define _Loop_hpp

class Loop : public Branch {
public:
    Loop(string& cond, string& body):
        Branch(cond), body(body) {}

    string toString() {
        return "Loop: (" + cond + ", " + body + ")";
    }

private:
    string& body;
};

#endif
