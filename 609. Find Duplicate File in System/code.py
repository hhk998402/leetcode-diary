from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(set)
        for path in paths:
            data = path.split(" ")
            directory = data[0]
            for files in data[1:]:
                fileData = files.split("(")
                name = fileData[0]
                content = fileData[1]
                d[content].add(directory + "/" + name)
        res = []
        for k,v in d.items():
            if(len(v) > 1):
                res.append(list(v))
        return res