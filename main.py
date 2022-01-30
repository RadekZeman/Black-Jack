import random


def krupier(karty):
    a = karty[0] + karty[1]
    print(karty[0])
    print(karty[1])
    b = 2
    c = [karty[0], karty[1]]
    if a == 22:
        c[0] = 1
        a = 12
    while a < 17:
        print(karty[b])
        a += karty[b]
        c.append(karty[b])
        b += 1
        if a > 21:
            for i in c:
                d = 0
                if i == 11:
                    d += 1
                    c.remove(i)
                    c.insert(d, 1)
                    a -= 10
    return(c)


if __name__ == '__main__':
    karty = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    random.shuffle(karty)
    print(karty)
    krupier = sum(krupier(karty))
    print(krupier)
