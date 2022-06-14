from warnings import catch_warnings


input_string = str(input())
char = 0
temp_rep = 0
max_rep = 0

while char < len(input_string):
    try:
        if input_string[char] == input_string[char+1]:
            temp_rep += 1
            if temp_rep > max_rep:
                max_rep = temp_rep
        if input_string[char] != input_string[char+1]:
            temp_rep = 0
    except:
        break
    char += 1

print(int(max_rep)+1)