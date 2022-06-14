num = int(input())
print(num, end=" ")
while num != 1:
    if num % 2 == 0:
        num/=2
        num = int(num)
        print(num, end=" ")
    elif num % 2 == 1:
        num*=3
        num+=1
        num = int(num)
        print(num, end=" ")