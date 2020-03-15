from branch import Branch
from ifcond import IfCond
from loop import Loop

if __name__ == '__main__':
    cond = 'x > 0'
    branch = Branch(cond)
    print(branch.toString())

    then_b = 'x++;'
    else_b = 'x--;'
    ifcond = IfCond(cond, then_b, else_b)
    print(ifcond.toString())

    body = 'y++;'
    loop = Loop(cond, body)
    print(loop.toString())
