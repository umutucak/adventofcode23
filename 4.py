cards = open("4.input", "r").read().split("\n")

def p1():
    def get_points(x):
        if x == 0:
            return x
        elif x == 1:
            return x
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

def p2():
    card_winnings = {}
    total_cards = {}
    id = 1
    for i, card in enumerate(cards):
        total_cards[i+1] = 1
    
    for card in cards:
        card_winnings[id] = 0
        card = card.split(":")[1].split("|")
        elf_cards = {}
        for elf in card[1].split():
            elf_cards[elf] = []
        for win_num in card[0].split():
            if win_num in elf_cards:
                card_winnings[id]+=1
        for i in range(id+1, id+card_winnings[id]+1):
            total_cards[i]+=total_cards[id]
        id+=1
    print(sum(total_cards.values()))
                    
p2()