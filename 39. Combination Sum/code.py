class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.dfs(candidates, target, 0, output, [])
        return(output)
    
    def dfs(self, candidates, target, idx, output, path):
        if(target < 0):
            return #Backtrack
        elif target == 0:
            output.append(path)
            return
        else:
            for i in range(idx,len(candidates)):
                self.dfs(candidates, target-candidates[i], i, output, path + [candidates[i]])
        return
