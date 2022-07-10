class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        ptr = 0
        while(i < (len(nums))):
            curr = nums[i]
            # nxt = nums[i+1]
            if(nums[ptr] == curr):
                i+=1

            else:
                nums[ptr+1] = nums[i]
                i+=1
                ptr +=1

        return ptr+1

sol = Solution()
print(sol.removeDuplicates([1,1,2]))
