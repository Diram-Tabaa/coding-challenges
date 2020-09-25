import math
import os
import random
import re
import sys
#if needed ^


def merge_the_tools(string, k):
    #take string and k as input first
    for i in range(0,len(string),k):

        sub = string[i:i+k]

        count = 0
        sub2 = list(sub)
        co = []
        for j in sub:
            if count == sub.find(j):
                co.append(j)
            count += 1
        print("".join(co))

def python_lists(N):
    #if you want to run this code, take N as an input first
    list = []
    for i in range(N):
        string = input()
        strl = string.split(" ")
        if strl[0] == "append":
            list.append(int(strl[1]))
        elif strl[0] == "insert":
            list.insert(int(strl[1]), int(strl[2]))
        elif strl[0] == "remove":
            list.remove(int(strl[1]))
        elif strl[0] == "pop":
            list.pop()
        elif strl[0] == "reverse":
            list.reverse()
        elif strl[0] == "sort":
            list.sort()
        elif strl[0] == "print":
            print(list)

def compareTriplets(a, b):
    # you can find code below to run this challenge
    al = 0
    bo = 0
    for n in range(len(a)):
        if a[n]>b[n]:
            al += 1
        elif a[n]<b[n]:
            bo += 1
    return str(al) + str(bo)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     a = list(map(int, input().rstrip().split()))
#
#     b = list(map(int, input().rstrip().split()))
#
#     result = compareTriplets(a, b)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
