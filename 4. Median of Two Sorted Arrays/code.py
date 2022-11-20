#https://takeuforward.org/data-structure/median-of-two-sorted-arrays-of-different-sizes/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if(n1>n2):
            return self.findMedianSortedArrays(nums2,nums1)

        medianPos = (n1+n2+1)//2
        minLen = n1
        median = 0.0
        lowMerged = 0
        highMerged = minLen
        while(lowMerged <= highMerged):
            print(lowMerged,highMerged)
            leftCut = (lowMerged + highMerged)//2
            rightCut = medianPos - leftCut
            leftLow = -float('inf') if leftCut == 0 else nums1[leftCut-1]
            rightLow = -float('inf') if rightCut == 0 else nums2[rightCut-1]
            leftHigh = float('inf') if leftCut == n1 else nums1[leftCut]
            rightHigh = float('inf') if rightCut == n2 else nums2[rightCut]

            print(leftLow, rightLow, leftHigh, rightHigh)

            if(leftLow <= rightHigh and rightLow <= leftHigh):
                if((n1+n2)%2 == 0):
                    median = (max([leftLow,rightLow]) + min([leftHigh,rightHigh]))/2.0
                else:
                    median =  (max([leftLow,rightLow]))
                break
            if(leftLow > rightHigh):
                highMerged = leftCut - 1
            else:
                lowMerged = leftCut + 1
        return median 