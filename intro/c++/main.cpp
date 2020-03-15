#include "Branch.hpp"
#include "IfCond.hpp"
#include "Loop.hpp"
#include <iostream>

using namespace std;

int main() {
    string cond = "x > 0";
    Branch branch(cond);

    cout << branch.toString() << endl;

    string then_b = "x++;";
    string else_b = "x--;";
    IfCond ifcond(cond, then_b, else_b);

    cout << ifcond.toString() << endl;

    string body = "y++;";
    Loop loop(cond, body);

    cout << loop.toString() << endl;
}
