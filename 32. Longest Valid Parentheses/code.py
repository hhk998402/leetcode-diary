class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] #Assign a starting index
        longest = 0
        for idx,ch in enumerate(s):
            if(ch == "("):
                stack.append(idx)
            else:
                stack.pop()
                if(not stack):
                   #Create new starting index
                   stack.append(idx)
                else:
                    longest = max(longest, idx - stack[-1])
        return longest
        