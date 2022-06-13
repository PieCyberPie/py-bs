#fixed by unpacking

import random

def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total/len(args)

nums = []
num_of_nums = 0

num_of_nums = int(input("How much nums do you want? "))

idx = 0 
while idx < num_of_nums:
    nums.append(random.randint(0, 100))
    idx += 1
print(nums)
print(average(*nums))