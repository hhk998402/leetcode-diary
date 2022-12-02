class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i,ele in reversed(list(enumerate(digits))):
            digits[i] = ele + (i//(n-1) if n>1 else 1) + carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
        return [carry] + digits if carry != 0 else digits