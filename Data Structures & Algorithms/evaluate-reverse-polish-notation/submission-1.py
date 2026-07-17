import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
                }
        for char in tokens:
            if char in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                result = ops[char](num1, num2)
                stack.append(int(result))
            else:
                stack.append(int(char))
        return stack[0]
        