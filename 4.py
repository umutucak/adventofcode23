cards = open("4.input", "r").read().split("\n")

def get_points(x):
    if x == 0:
        return x
    elif x == 1:
        return x
    else:
        return 2**(x-1)

total = 0
for card in cards:
    card = card.split(":")[1].split("|")
    elf_cards = {}
    counter = 0
    for elf in card[1].split():
        elf_cards[elf] = []
    for win_num in card[0].split():
        if win_num in elf_cards:
            counter += 1
    total += get_points(counter)
print(total)