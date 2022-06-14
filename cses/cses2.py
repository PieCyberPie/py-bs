list_size = 0
num_list = []

list_size = int(input())
#for idx in range(1, list_size):
#    num_list.append(int(input()))

input2 = str(input())
list1 = input2.split()
map_object = map(int, list1)
num_list = list(map_object)

n = len(num_list)
total = (n+1)*(n+2)/2
sum_of_len = sum(num_list)
print(int(total-sum_of_len))
