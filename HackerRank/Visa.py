#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here
    if k in arr:
        print("YES")
    else:
        print("NO")

# findNumber([1,2,3],3)

#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    # Write your code here
    list = []
    for i in  range(l,r+1):
        if i % 2 == 1:
            list.append(i)
    return list

# print(oddNumbers(3,5))

def maxTickets(tickets):
    tickets=tickets.sort()
    list = []
    counter = 1
    for i in range(len(tickets)):
        if helper(tickets[i],tickets[i+1]):
            list.append(tickets[i])
            counter += 1
        else:
            list.append(counter)
            counter = 1
    return max(list)



def helper(a,b):
    return abs(a-b) <= 1
