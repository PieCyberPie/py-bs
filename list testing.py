list0 = ["Adam", "john", "BOMB"]
print(list0)
i = -1
for idx in list0:
    print(idx)
    print(list0[i + 1].upper())
    i += 1

list1 = [1, 2, 3, 4, 5]
list2 = list1
list3 = [1, 2, 3, 4, 5, 6, 7]
print(list1, id(list1))
print(list2, id(list2))

list1.append(6)
print(list1, id(list1))
print(list2, id(list2))

list2.append(7)
print(list1, id(list1))
print(list2, id(list2))

print(list1 is list2, list1 == list2)
print(list1 is list3, list1 == list3)

sentence = "omg it's working? i hope so"

split_sentence = sentence.split(" ")

print("!!!".join(split_sentence))