class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {}
        brackets['('] = ')'
        brackets['{'] = '}'
        brackets['['] = ']'
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if len(stack) > 0 and brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0