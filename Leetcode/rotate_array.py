class Solution(object):
    def rotate(self, nums, k):
        k = k% len(nums)
        j = len(nums) - k


        nums[:] = nums[j:] + nums[:j]
        print(nums)

sol = Solution()
print(sol.rotate([-1,-100,3,99],2))

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # print('a')
    # Determine if two movie runtimes add up to the flight length
    for i in range(0,len(movie_lengths)):
        for j in range(i+1,len(movie_lengths)):
            if(movie_lengths[i] + movie_lengths[j] == flight_length):
                return True;


    return False




