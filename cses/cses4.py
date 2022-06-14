listlen = int(input())

temp_input = str(input())
list1 = temp_input.split()
map_object = map(int, list1)
num_list = list(map_object)

turn = 0
idx = listlen-1
""" while True:
    try:
        while num_list[idx] > num_list[idx+1]:
            previous_list = num_list
            num_list[idx+1] += 1
            idx += 1
            if previous_list == num_list:
                break
            print(num_list)
            turn += 1 
        else:
            idx += 1
    except:
        idx = 0 """



previous_list = num_list
print(previous_list == num_list)
num_list[1] += 1
print(previous_list == num_list)
print(turn)