from branch import Branch


class Loop(Branch):
    def __init__(self, cond, body):
        super().__init__(cond)
        self.body = body

    def toString(self):
        return 'Loop(' + self.cond + ", " + self.body + ")"
