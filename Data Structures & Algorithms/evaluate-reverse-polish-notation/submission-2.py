class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]
        s = []
        for t in tokens:
            if t not in operations:
                s.append(int(t))
            elif t == "+":
                s.append(s.pop()+s.pop())
            elif t == "-":
                r = s.pop()
                l = s.pop()
                s.append(l-r)
            elif t == "*":
                s.append(s.pop()*s.pop())
            elif t == "/":
                r = s.pop()
                l = s.pop()
                s.append(int(l/r))
        return s.pop()
