import re

def to_roman(a):
    maps = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    b = str(a)
    c = []
    # for i in b:
    #     c.append(i)


    for j in range(1, len(b) + 1):
        c.append(b[-j])

    d = []
    for i in range(len(c)):
        index = 10 ** i
        half = index * 10 / 2
        full = index * 10
        if c[i] <= '3':
            d.extend([maps.get(index) for j in range(int(c[i]))])
        elif c[i] <= '5':
            d.extend([maps.get(half)])
            d.extend([maps.get(index) for j in range(5 - int(c[i]))])
        elif c[i] <= '8':
            d.extend([maps.get(index) for j in range(int(c[i]) - 5)])
            d.extend([maps.get(half)])
        elif c[i] == '9':
            d.extend(maps.get(full))
            d.extend(maps.get(index))

    s = ''
    for i in range(1, len(d) + 1):
        s += d[-i]
    return s


def from_roman(roman):

    specialroman = (
        ('CM', 900),
        ('CD', 400),
        ('XC', 90),
        ('XL', 40),
        ('IX', 9),
        ('IV', 4)
    )

    normalroman = (
        ('M', 1000),
        ('D', 500),
        ('C', 100),
        ('L', 50),
        ('X', 10),
        ('V', 5)
        ('I', 1)
    )

    a = [roman[i] for i in range(len(roman))]
    for b in a:
        for number, integer in normalroman:
            if b == number:









