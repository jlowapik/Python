import random

def small_chest(n):

    items = ['white', 'green', 'red']
    weights = [77.373974208, 21.688159437, 0.937866354 ]

    whites = greens = reds = 0

    for i in range(n):
        item = random.choices(items, weights=weights, k=1)[0]
        match item:
            case 'white':
                whites += 1
            case 'green':
                greens += 1
            case 'red':
                reds += 1
    return f'white: {whites}, green: {greens}, red: {reds}'

def big_chest(n):

    items = ['white', 'green', 'red']
    weights = [0, 82.222222222, 17.777777777]

    whites = greens = reds = 0

    for i in range(n):
        item = random.choices(items, weights=weights, k=1)[0]
        match item:
            case 'white':
                whites += 1
            case 'green':
                greens += 1
            case 'red':
                reds += 1
    return f'white: {whites}, green: {greens}, red: {reds}'

def small_chest_mbr():

    items = ['mbr', 'not_mbr']
    weights = [0.0309375, 99.9690625]

    item = ''
    count = 0

    while item != 'mbr':
        item = random.choices(items, weights=weights, k=1)[0]
        count += 1
    return count

def big_chest_mbr():

    items = ['mbr', 'not_mbr']
    weights = [0.625, 99.375]

    item = ''
    count = 0

    while item != 'mbr':
        item = random.choices(items, weights=weights, k=1)[0]
        count += 1
    return count


lst = []

for i in range(100):
    lst.append(big_chest_mbr())

print(lst)
print(round(sum(lst) / len(lst)))

