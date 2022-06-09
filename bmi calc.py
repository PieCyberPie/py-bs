weight = int(input("write ur weight in kg \n"))
height = int(input("write ur height in cm \n"))

height_in_meters = height/100

bmi = weight/height_in_meters**2

print(f"ur bmi is {bmi}")