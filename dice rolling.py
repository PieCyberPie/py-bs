import random

dice_num = int(input("How many dice are we rolling? "))
sides_num = int(input("How many sides on each die? "))

print(f" \nNumber of dices: {dice_num} \nNumber of sides: {sides_num}")

reroll = ""

while reroll != 'q':
    print("\nYour roll of dice is: ")
    for i in range(0, dice_num):
        print(f"{random.randint(1, sides_num)} | ", end='')
    reroll = input("\nContinue? Press q to exit ")
