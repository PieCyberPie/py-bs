weight = int(input("write ur weight in kg \n"))
height = int(input("write ur height in cm \n"))

height_in_meters = height/100

bmi = weight/height_in_meters**2

print(f"ur bmi is {bmi}")

if(bmi<16.0):
    print("You are severely underweight! ")
elif(bmi>16.0 and bmi<18.4):
    print("You are underweight")
elif(bmi>18.5 and bmi<24.9):
    print("You are normal")