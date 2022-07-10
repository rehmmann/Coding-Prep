class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                first = nums[i]
                second = nums[j]
                total = first + second
                if total == target:
                    return [i,j]

