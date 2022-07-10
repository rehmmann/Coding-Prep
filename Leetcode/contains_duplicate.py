class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for item in nums:
            if(item not in dic):
                dic[item] = 0

            elif(dic[item] == 0):
                dic[item] = 1

        for key,val in dic.items():
            if val == 1:
                return True
        return False



sol = Solution()
print(sol.containsDuplicate([1,2,3]))

