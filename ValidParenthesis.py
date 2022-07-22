class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        
        for i in range(n):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            if len(stack) != 0:
                if s[i] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        break
                elif s[i] == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        break
                elif s[i] == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        break
            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
        
