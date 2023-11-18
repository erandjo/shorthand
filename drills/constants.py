import random

ld_cons = ['k', 'g', 'r', 'l', 'd', 't', 'n', 'm', 'th'];
ud_cons = ['p', 'b', 'f', 'v', 'j', 'h', 'he', 'I', 'ch', 's', 'sh', 'ng', 'nk'];
cons = ld_cons + ud_cons;

weights = [100] * len(cons);

def increase_probability(idx):
    weights[idx] = weights[idx] * 2

def decrease_probability(idx):
    weights[idx] = weights[idx] / 2

instructions = """
Type q to exit at any time.")
Type:
    - 1 if you knew the stroke
    - 2 if you didn't know the stroke
"""

def probability_based():
    while True:
        print(instructions)
        character = random.choices(cons, weights, k=1)[0]
        print("practice the stroke:", character, "\n")
        res = input("$ ")
        match res:
            case '1':
                decrease_probability(cons.index(character))
            case '2':
                increase_probability(cons.index(character))
            case 'q':
                break


def one_round():
    while True:
        print(instructions)
        choice = random.choices(cons, weights, k=1)
        if len(choice) < 1:
            print("Well done you have now practiced all consonants!")
        character = choice[0]
        print("Practice the stroke:", character, "\n")
        res = input("$ ")
        match res:
            case '1':
                weights[cons.index(character)] = 0
            case '2':
                weights[cons.index(character)] = 100
            case 'q':
                break


modes = """
Do you whish to:
    1. practice until you quit, or
    2. practice all consonants once?
      
"""

mode = input(modes)
probability_based() if mode == '1' else one_round()
