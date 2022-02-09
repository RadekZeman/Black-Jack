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
        a = "prohra"
        print(a)
    elif krupierbody > 21:
        a = "vyhra"
        print(a)
    elif hracbody > krupierbody:
        a = "vyhra"
        print(a)
    elif hracbody == krupierbody:
        a = "remiza"
        print(a)
    else:
        a = "prohra"
        print(a)
    return a


if __name__ == '__main__':
    penize = 0
    while 1:
        sazka = input("tvoje sazka:")
        sazka = int(sazka)
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
        vydelekpojistka = 0
        if protivnik == 11:
            text2 = """
                    Muzes koupit pojistku- vsadit na to, ze krupier dostane Blackjack.
                    0 = nechci kooupit
                    1 = chci koupit
                    """
            print(text2)
            pojistka = input("pojistka:")
            pojistka = int(pojistka)
            if pojistka == 1:
                sazkapojistka = input("kolik chces vsadit:")
                sazkapojistka = int(sazkapojistka)
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
                print(f"Split muzes zahrat jenom kdyz mas stejny karty. Zadej jine cislo. ")
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
                sazka1 = sazka
                if rozhodnutihrace1 == 1:
                    hrac1, a = hit(hrac1, a)
                if rozhodnutihrace1 == 2:
                    double(hrac1)
                    a += 1
                    sazka1 *= 2
                if rozhodnutihrace1 == 4:
                    print(f"s hracem 1 jsi se vzdal")
                    c = 0
                    sazka1 = sazka1 / 2
                    vysledek1 = "prohra"
                rozhodnutihrace2 = input("tvoje rozhodnuti pro hrace 2 (cislo):")
                rozhodnutihrace2 = int(rozhodnutihrace2)
                sazka2 = sazka
                if rozhodnutihrace2 == 1:
                    hrac2, a = hit(hrac2, a)
                if rozhodnutihrace2 == 2:
                    double(hrac2)
                    a += 1
                    sazka2 *= 2
                if rozhodnutihrace2 == 4:
                    print(f"s hracem 2 jsi se vzdal")
                    d = 0
                    sazka2 = sazka2 / 2
                    vysledek2 = "prohra"
                if rozhodnutihrace1 != 4:
                    hrac1body = sum(hrac1)
                    print(f"soucet hrace1 je {hrac1body}")
                if rozhodnutihrace2 != 4:
                    hrac2body = sum(hrac2)
                    print(f"soucet hrace2 je {hrac2body}")
                break
        if rozhodnuti == 1:
            hrac, a = hit(hrac, a)
        if rozhodnuti == 2:
            double(hrac)
            a += 1
            sazka *= 2
        if rozhodnuti == 4:
            print(f"vzdal ses")
            b = 0
            sazka = sazka/2
            vysledek = "prohra"
        hracbody = sum(hrac)
        if rozhodnuti != 4 or rozhodnuti != 3:
            print(f"tvuj soucet je {hracbody}")
        if b or pojistka == 1:
            x = krupier(karty, protivnik, a)
            krupierbody = sum(x)
            print(f"krupieruv soucet je {krupierbody}")
            if rozhodnuti == 3:
                if c:
                    print(f"vyhodnoceni hrace 1")
                    vysledek1 = vyhodnoceni(hrac1, krupierbody)
                if d:
                    print(f"vyhodnoceni hrace 2")
                    vysledek2 = vyhodnoceni(hrac2, krupierbody)
            elif rozhodnuti == 4:
                vysledek = "prohra"
            else:
                vysledek = vyhodnoceni(hrac, krupierbody)
            if pojistka == 1:
                if krupierbody == 21:
                    vydelekpojistka = sazkapojistka
                    print(f"pojistka vyhra, vydelal sis {sazkapojistka}")
                else:
                    vydelekpojistka = -sazkapojistka
                    print(f"pojistka prohra, prodelal sis {sazkapojistka}")
        if rozhodnuti == 3:
            if vysledek1 == "vyhra":
                vydelek1 = sazka1
            elif vysledek1 == "remiza":
                vydelek1 = 0
            elif vysledek1 == "prohra":
                vydelek1 = -sazka1
            if vysledek2 == "vyhra":
                vydelek2 = sazka2
            elif vysledek2 == "remiza":
                vydelek2 = 0
            elif vysledek2 == "prohra":
                vydelek2 = -sazka2
            vydelek = vydelek1 + vydelek2
            print(f"vydelal sis {vydelek}")
        else:
            if vysledek == "vyhra":
                vydelek = sazka
                print(f"vydelal sis {sazka}")
            elif vysledek == "remiza":
                vydelek = 0
                print(f"tva sazka se ti vraci")
            elif vysledek == "prohra":
                vydelek = -sazka
                print(f"prodelal sis {sazka}")
        vydelekcelkem = vydelek + vydelekpojistka
        penize += vydelekcelkem
        print(f"celkem sis vydelal {penize}")
