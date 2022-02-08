import random


def krupier(karty, krupier, a):
    b = krupier + karty[a]
    c = [krupier, karty[a]]
    print(f"krupierova karta je {krupier}")
    print(f"krupierova karta je {karty[a]}")
    a += 1
    if b == 22:
        c[0] = 1
        b = 12
    while b < 17:
        print(f"krupierova karta je {karty[a]}")
        b += karty[a]
        c.append(karty[a])
        a += 1
        if b > 21:
            for i in c:
                d = 0
                if i == 11:
                    d += 1
                    c.remove(i)
                    c.insert(d, 1)
                    b -= 10
    return(c)


def hit(hrac, a):
    rozhodnuti = 1
    while rozhodnuti == 1:
        hrac.append(karty[a])
        print(hrac)
        a = a+1
        print("Pokud chces dalsi kartu zadej 1. Pokud chces skoncit zadej 0.")
        rozhodnuti = input("tvoje rozhodnuti (cislo):")
        rozhodnuti = int(rozhodnuti)
    return (hrac, a)


def double(hrac):
    hrac.append(karty[a])
    print(hrac)
    return hrac


def vyhodnoceni(hrac, krupierbody,):
    hracbody = sum(hrac)
    if hracbody > 21:
        for i in hrac:
            if i == 11:
                hracbody -= 10
                break
    if hracbody > 21:
        print(f"prohra")
    elif krupierbody > 21:
        print(f"vyhra")
    elif hracbody > krupierbody:
        print(f"vyhra")
    elif hracbody == krupierbody:
        print(f"remiza")
    else:
        print(f"prohra")


if __name__ == '__main__':
    karty = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    random.shuffle(karty)
    protivnik = karty[0]
    hrac = [karty[1], karty[2]]
    a = 3
    print(hrac)
    print(f"krupierova prvni karta je {protivnik}")
    c = 1
    b = 1
    d = 1
    pojistka = 0
    if protivnik == 11:
        text2 = """
                   Muzes koupit pojistku- vsadit na to, ze krupier dostane Blackjack.
                   0 = nechci kooupit
                   1 = chci koupit
                   """
        pojistka = input("pojistka:")
        pojistka = int(pojistka)
    text1 = """
           moznosti hrace:
           0 = Stand: Zůstat stát, ukončit hru.
           1 = Hit: Vzít od krupiéra další kartu.
           2 = Double: Zdvojnásobit vsazenou částku.Hrac dostane od krupiéra ještě jednu kartu a hra končí.
           3 = Split: Rozdělit hru.
           4 = Vzdat hru: Hrac ztrácí polovinu vsazené částky.
           """
    print(text1)
    rozhodnuti = input("tvoje rozhodnuti (cislo):")
    rozhodnuti = int(rozhodnuti)
    while rozhodnuti == 3:
        if hrac[0] != hrac[1]:
            print(f"Split muzes zahrat jenom kdzy mas stejny karty, zadej jine cislo. ")
            rozhodnuti = input("tvoje rozhodnuti (cislo):")
            rozhodnuti = int(rozhodnuti)
        else:
            hrac1 = [hrac[0]]
            hrac1.append(karty[a])
            print(hrac1)
            a += 1
            hrac2 = [hrac[1]]
            hrac2.append(karty[a])
            print(hrac2)
            a += 1
            rozhodnutihrace1 = input("tvoje rozhodnuti pro hrace 1 (cislo):")
            rozhodnutihrace1 = int(rozhodnutihrace1)
            rozhodnutihrace2 = input("tvoje rozhodnuti pro hrace 2 (cislo):")
            rozhodnutihrace2 = int(rozhodnutihrace2)
            if rozhodnutihrace1 == 1:
                hrac1, a = hit(hrac1, a)
            if rozhodnutihrace1 == 2:
                double(hrac1)
                a += 1
            if rozhodnutihrace1 == 4:
                print(f"s hracem 1 jsi se vzdal")
            c = 0
            if rozhodnutihrace2 == 1:
                hrac1, a = hit(hrac2, a)
            if rozhodnutihrace2 == 2:
                double(hrac2)
                a += 1
            if rozhodnutihrace1 == 4:
                print(f"s hracem 2 jsi se vzdal")
            d = 0
            break
    if rozhodnuti == 1:
        hrac, a = hit(hrac, a)
    if rozhodnuti == 2:
        double(hrac)
        a += 1
    if rozhodnuti == 4:
        print(f"vzdal ses")
        b = 0
    if b:
        x = krupier(karty, protivnik, a)
        krupierbody = sum(x)
        print(f"krupieruv soucet je {krupierbody}")
        if rozhodnuti == 3:
            if c:
                print(f"vyhodnoceni hrace 1")
                vyhodnoceni(hrac1, krupierbody)
            if d:
                print(f"vyhodnoceni hrace 2")
                vyhodnoceni(hrac2, krupierbody)
        else:
            vyhodnoceni(hrac, krupierbody)
        if pojistka:
            if krupierbody == 21:
                print(f"pojistka vyhra")
            else:
                print(f"pojistka prohra")
