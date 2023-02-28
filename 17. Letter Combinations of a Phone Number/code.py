class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []
        self.res = []
        d = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5": ["j","k","l"]}
        d["6"] = ["m","n","o"]
        d["7"] = ["p","q","r","s"]
        d["8"] = ["t","u","v"]
        d["9"] = ["w","x","y","z"]

        oldLetters = d[digits[0]]
        if(len(self.res) == 0):
            for idx,l1 in enumerate(oldLetters):
                self.res.append(l1)
        for i in range(1,len(digits)):
            newLetters = d[digits[i]]
            self.createCombos(newLetters)

        return self.res

    def createCombos(self, newLetters):
        resultArr = []
        for l2 in newLetters:
            for val in self.res:
                resultArr.append(val + l2)
        self.res = resultArr
        print(self.res, resultArr)