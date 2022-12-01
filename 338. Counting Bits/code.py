class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for x in range(n+1)]
        nearest_power_of_2 = 1
        for i in range(1,n+1):
            if(nearest_power_of_2 * 2 == i):
                #Update nearest power of 2
                nearest_power_of_2 = i
            res[i] = res[i-nearest_power_of_2] + 1
        return res