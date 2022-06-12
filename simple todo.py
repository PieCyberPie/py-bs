print("""_________ _______         ______   _______            _       _________ _______  _________
\__   __/(  ___  )       (  __  \ (  ___  )          ( \      \__   __/(  ____ \ \__   __/
   ) (   | (   ) |       | (  \  )| (   ) |          | (         ) (   | (    \/    ) (   
   | |   | |   | | _____ | |   ) || |   | |          | |         | |   | (_____     | |   
   | |   | |   | |(_____)| |   | || |   | |          | |         | |   (_____  )    | |   
   | |   | |   | |       | |   ) || |   | |          | |         | |         ) |    | |   
   | |   | (___) |       | (__/  )| (___) |          | (____/\___) (___/\____) |    | |   
   )_(   (_______)       (______/ (_______)          (_______/\_______/\_______)    )_(   
                                                                                         """)

user_input = ""
todolist = []
completedlist = []

while True:
    user_input = input("Type in 'h for help: ")

    if user_input == 'h':
        print("To add your task just print it, to delete it from your list, type in it's number, print 'q' to quit")

    if user_input == 'q':
        user_input = int(1)
        for task in completedlist:
            print(f"{user_input}. {task}")
            user_input += 1
        break

    if user_input.isnumeric():
        user_input = int(user_input)
        if user_input < len(todolist)+1:
            completedlist.append(todolist.pop(user_input-1))
        else:
            print("Error! No task found, try again! ")

    else:
        todolist.append(user_input)
    print("Here is your tasks list: ")
    user_input = int(1)
    for task in todolist:
        print(f"{user_input}. {task}")
        user_input += 1