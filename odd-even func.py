def isodd(number):
    if(number % 2 == 1):
        return True
    else:
        return False

user_input = int(input("Input number and i'll tell you is this odd or not: "))

if isodd(user_input):
    print("it's odd!")
else:
    print("it's not odd :(( ")