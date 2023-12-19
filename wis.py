wyb=input("gra jednoosobowa czy wieloosobowa? (wielo/jedno): ")

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
        print(pseudonim, " pozostalo ci ", zycia, " zyc")
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
                print(pseudonim, " pozostalo ci ", zycia, " zyc")
                print("")
                print(" ".join(tablica))
                print(" ")
                print(pseudonim, " wygrales!")
                break
  
        else:
            zycia -= 1