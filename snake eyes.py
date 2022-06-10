import random

random.seed(None)
eye1 = random.randint(1, 6)
eye2 = random.randint(1, 6)

while(eye1 != 1 or eye2 != 1):
    print(f"not eyes, it's {eye1} - {eye2} ,try again \n")
    eye1 = random.randint(1, 6)
    eye2 = random.randint(1, 6)

print(f"YO IT'S SNAKE EYE'S, LOOK AT IT{eye1}-{eye2}")