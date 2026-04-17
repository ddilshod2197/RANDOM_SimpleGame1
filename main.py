import random

def oyin():
    computer = random.sample(range(1, 21), 5)

    print("1 dan 20 gacha 5 ta son kiriting:")
    user = []
    for i in range(5):
        son = int(input(f"{i+1}-son: "))
        user.append(son)

    togri = [x for x in user if x in computer]

    print("Kompyuter tanlagan sonlar:", computer)
    print("Siz topgan sonlar:", togri)
    print("To‘g‘ri topilganlar soni:", len(togri))


oyin()
