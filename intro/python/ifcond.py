from branch import Branch


class IfCond(Branch):
    def __init__(self, cond, then_b, else_b):
        super().__init__(cond)
        self.then_b = then_b
        self.else_b = else_b

    def toString(self):
        return 'IfCond(' + self.cond + ", " + self.then_b \
            + ", " + self.else_b + ")"
