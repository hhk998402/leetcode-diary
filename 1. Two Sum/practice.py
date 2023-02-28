def findIndices(nums, target):
    d = {}
    for idx,i in enumerate(nums):
        if i not in d:
            d[target - i] = idx
        else:
            print(idx, d[i])

nums = [2,7,11,15]
target = 9

findIndices(nums, target)
findIndices([3,2,4], 6)
findIndices([3,3], 6)