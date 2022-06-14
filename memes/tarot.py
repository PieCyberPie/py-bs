import random

DECK_SIZE = 78

deck = set()
for idx in range(1,DECK_SIZE+1):
    deck.add(idx)
draw = []

how_much_to_draw = int(input("сколько берёшь карт: "))
idx = 0
while idx < how_much_to_draw:
    randomed = random.randint(1, 78)
    if randomed in deck:
        deck.remove(randomed)
        draw.append(randomed)
        idx += 1
    elif randomed not in deck:
        print(end="")

print(draw)

user_input = input("Ещё брать будешь?(напиши 1, чтобы взять одну или букву чтобы закрыть)")
while user_input.isnumeric():
    idx = 0
    while idx < how_much_to_draw:
        randomed = random.randint(1, 78)
        if randomed in deck:
            deck.remove(randomed)
            draw.append(randomed)
            idx += 1
        elif randomed not in deck:
            print(end="")
    print(draw)
    user_input = input("Ещё брать будешь?(напиши скока, или букву чтобы закрыть)")