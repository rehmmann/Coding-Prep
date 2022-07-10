#!/bin/python3



dict = []

def repeatedString(s, n):
    count1 = 0
    count2 = 0
    str_Len = len(s)
    repetitions = n // str_Len # Calculates number of full cycles of s
    elements_Left = n % str_Len
    str_Left = s[:elements_Left]
    for i in s:
        if i == "a":
            count1 += 1
    for i in str_Left:
        if i == "a":
            count2 += 1
    # print(count1,repetitions,count2)
    return count1 * repetitions + count2

# print(repeatedString("aba",10))

def countSwaps(a):
    total = len(a)
    count = 0
    for i in range(total):
        for j in range(total-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

countSwaps([6,4,1])


