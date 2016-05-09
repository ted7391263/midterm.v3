class BinaryGate:
    def __init__(self, a, b):
        self.pinA = a
        self.pinB = b


class XORGate(BinaryGate):
    def __init__(self,a,b):
        BinaryGate.__init__(self, a, b)

    def performGateLogic(self):

        if self.pinA == self.pinB:
            return 0
        else:
            return  1

    def output(self):
        self.output = self.performGateLogic()
        return self.output


g = XORGate(0,0)
print(g.output())
g = XORGate(0,1)
print(g.output())
g = XORGate(1,0)
print(g.output())
g = XORGate(1,1)
print(g.output())
