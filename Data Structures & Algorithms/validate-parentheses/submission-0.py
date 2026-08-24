class Solution:
    def isValid(self, s: str) -> bool:
        """
        |[(| ]
        """
        stack = []
        open_list = ['(', '[', '{']
        # close_list = [')', ']', '}']
        for bracket in s:
            if bracket in open_list:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if (bracket == ')' and stack[-1] == '(') or (bracket == ']' and stack[-1] == '[') or (bracket == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False


            
        