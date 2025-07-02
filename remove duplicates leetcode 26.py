from collections import Counter

#2 pointer solution
l = 1

nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    for r in range(1, len(nums)):
        if nums[l] != nums[r-1]:
             nums[l] = nums[r]
             l += 1
    return l 



#correct answer

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        return k + 1
    

