import re

class Solution(object):

    def calculate(self, s):
        op_pat = re.compile(r"[+-/*]+")
        val_pat = re.compile(r"[\w]+")
        ops = op_pat.findall(s)
        vals = [int(x) for x in val_pat.findall(s)]

        for i, op in enumerate(ops):
            if ops[i] == '*':
                ops[i] = ops[i - 1] if i - 1 >= 0 else '+'
                vals[i + 1] = vals[i] * vals[i + 1]
                vals[i] = 0
            elif ops[i] == '/':
                ops[i] = ops[i - 1] if i - 1 >= 0 else '+'
                vals[i + 1] = vals[i] / vals[i + 1]
                vals[i] = 0

        total = vals[0]
          
        for i, v in enumerate(ops):
            if ops[i] == '+':
                total += vals[i+1]
            elif ops[i] == '-':
                total -= vals[i+1]

        return total
                            
        
    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """
        expr = self.parse(s)
        ev_expr = expr.ev()
        return ev_expr.n
        
    def parse(self, s):
        s = s.strip()

        for i, c in reversed(list(enumerate(s))):
            if c == '+':
                return Plus(self.parse(s[:i]), self.parse(s[i+1:]))
            elif c == '-':
                return Sub(self.parse(s[:i]), self.parse(s[i+1:]))

        for i, c in reversed(list(enumerate(s))):
            if c == '*':
                return Mul(self.parse(s[:i]), self.parse(s[i+1:]))
            elif c == '/':
                return Div(self.parse(s[:i]), self.parse(s[i+1:]))

        return Num(int(s))
    
class AST(object):

    def ev(self):
        return None

class Num(AST):

    def __init__(self, n):
        self.n = n

    def ev(self):
        return self

    def __str__(self):
        return str(self.n)

class BinOp(AST):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(BinOp, self)
    
    def __str__(self):
        return '(' + str(self.a) + ' ' + self.name() + ' ' + str(self.b) + ')'


class Plus(BinOp):

    def ev(self):
        return Num(self.a.ev().n + self.b.ev().n)

    def name(self):
        return 'PLUS'


class Sub(BinOp):

    def ev(self):
        return Num(self.a.ev().n - self.b.ev().n)

    def name(self):
        return 'Sub'

class Mul(BinOp):

    def ev(self):
        return Num(self.a.ev().n * self.b.ev().n)

    def name(self):
        return 'Mul'

class Div(BinOp):

    def ev(self):
        return Num(self.a.ev().n // self.b.ev().n)

    def name(self):
        return 'Div'

        
