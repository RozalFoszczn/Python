import os

wyb=input("gra jednoosobowa czy wieloosobowa? (wielo/jedno): ")
play = True
while play:
    if wyb=="jedno":

        import random

        print("Witaj graczu. Twoim zadaniem bedzie odgadnac losowe haslo. W haslach nie ma duzych liter i polskich znakow.")

        lista = ["romus", "luminescencja", "magnetoelektryczny", "malkontenctwo", "primaaprilisowy", "kociak", "zwierzchnictwo", "lumpenproletariat", "deoksyrybonukleinowy", "krztusiec", "prokrastynacja", "ekwilibrystyka", "transcendencja", "somnambulizm", "tromtadracja", "plenipotencja", "dezynwoltura", "poliandria", "kuriozum", "luminarz", "mizogin", "egzegeza", "arywizm", "ryba", "wyimaginowany", "imponderabilia", "metamorfozowanie", "malkontent", "emulgacja", "oksymoron", "ekstrapolacja", "europarlamentarzysta", "ortodoksyjny", "apartamentowiec", "ekwilibrystyka", "franczyzobiorca", "ambiwalentny", "konfabulacja", "wyselekcjonowany", "niezdyscyplinowanie", "dezaprobatywnie", "ekstraterestrialny", "kontrrewolucjonista", "parafrazowanie", "ksylografowanie", "konserwatywnie", "superpozycjonowanie", "zindywidualizowany", "dekoncentracja", "eksterminacyjny", "monopolizacyjny", "wzajemnopomocowy", "dekonstrukcjonizm", "egzemplifikacyjny", "znormalizowany", "egzekucjonowanie", "bibliomaniak", "kameleoniczny", "oksfordzki"]

        haslo = str(lista[random.randint(0, len(lista) - 1)])
        tablica = list(haslo)


        for i in range(len(haslo)):
            tablica[i] = "_"

        zycia = 10

        while zycia > 0:
            print("")
            print(" pozostalo ci ", zycia, " zyc")
            print("")
            print(" ".join(tablica))
            print(" ")


            print("Podaj swoja litere: ")
            litera = input()


            if litera in haslo:

                for i in range(len(haslo)):
                    if haslo[i] == litera:
                        tablica[i] = litera
    
 
                if "".join(map(str, tablica)) == haslo:
                    print("")
                    print(" pozostalo ci ", zycia, " zyc")
                    print("")
                    print(" ".join(tablica))
                    print(" ")
                    print(" wygrales!")
                    break
            else:
                    zycia -= 1
        if zycia == 0:
            print("przegrales")
        wbg=int(input("Jesli chcesz grac dalej, wpisz liczbe rozna od 0. Jesli chcesz skonczyc gre, wpisz 0: "))
        if wbg==0:
            print("koniec gry")
            break
    elif wyb=="wielo":

        print("Witajcie gracze. Waszym zadaniem bedzie odgadniecie hasel, ktore wymyslicie nawzajem.")

        lista = input("podaj haslo dla drugiego gracza: ")

        haslo = str(lista)
        tablica = list(haslo)


        for i in range(len(haslo)):
            tablica[i] = "_"

        zycia = 10

        while zycia > 0:
            print("")
            print(" pozostalo ci ", zycia, " zyc")
            print("")
            print(" ".join(tablica))
            print(" ")


            print("Podaj swoja litere: ")
            litera = input()


            if litera in haslo:

                for i in range(len(haslo)):
                    if haslo[i] == litera:
                        tablica[i] = litera
    
 
                if "".join(map(str, tablica)) == haslo:
                    print("")
                    print(" pozostalo ci ", zycia, " zyc")
                    print("")
                    print(" ".join(tablica))
                    print(" ")
                    print(" wygrales!")
                    break
            else:
                zycia -=1
        if zycia == 0:
            print("przegrales")
        wbgg=int(input("Jesli chcesz grac dalej, wpisz liczbe rozna od 0. Jesli chcesz skonczyc gre, wpisz 0: "))
        if wbgg==0:
            print("koniec gry")
            break