player1_name = input("Input 1st player name: ")
player2_name = input("Input 2nd player name: ")

toothpicks_num = 13
toothpicks_take = 0
while True:

    for i in range(1,toothpicks_num):
        print("| ", end='')
    print(f"There are {toothpicks_num} toothpicks left")

    toothpicks_take = int(input(f"{player1_name}, please input number of toothpicks you will take: "))
    while toothpicks_take > 3 or toothpicks_take < 1 or toothpicks_num-toothpicks_take < 0:
        toothpicks_take = int(input(f"Error! please input number from 1 to 3 and not bigger, than left toothpicks: "))

    toothpicks_num -= toothpicks_take
    if(toothpicks_num == 0):
        print(f"Congratulations! {player1_name} win!")
        break



    for i in range(1, toothpicks_num):
        print("| ", end='')
    print(f"There are {toothpicks_num} toothpicks left")

    toothpicks_take = int(input(f"{player2_name}, please input number of toothpicks you will take: "))
    while toothpicks_take > 3 or toothpicks_take < 1 or toothpicks_num - toothpicks_take < 0:
        toothpicks_take = int(input(f"Error! Please input number from 1 to 3 and not bigger, than left toothpicks: "))

    toothpicks_num -= toothpicks_take
    if (toothpicks_num == 0):
        print(f"Congratulations! {player2_name} win!")
        break
