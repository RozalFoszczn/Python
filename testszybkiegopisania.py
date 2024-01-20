
import random
import time
import os
print("witaj.Za chwile rozpocznie sie twoj test szybkiego pisania.")
play=True
while play:
    lista = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    zd = lista[random.randint(0, 25)]
    za = lista[random.randint(0, 25)]
    zs = lista[random.randint(0, 25)]
    zf = lista[random.randint(0, 25)]
    zg = lista[random.randint(0, 25)]
    zh = lista[random.randint(0, 25)]
    zj = lista[random.randint(0, 25)]
    zk = lista[random.randint(0, 25)]
    zl = lista[random.randint(0, 25)]
    zz = lista[random.randint(0, 25)]
    print(zd)
    print(za)
    print(zs)
    print(zf)
    print(zg)
    print(zh)
    print(zj)
    print(zk)
    print(zl) 
    print(zz)
    st=int(input("wpisz 1, kiedy bedziesz gotow, nastepnie przepisz litery z gory: "))
    if st == 1:
        start=time.time()
        i=input("przepisz tekst z gory: ")
        o=input()
        p=input()
        a=input()
        s=input()
        d=input()
        f=input()
        g=input()
        h=input()
        j=input()
        if i== zd and o == za and p== zs and a==zf and s==zg and d==zh and f==zj and g==zk and h==zl and j==zz:
            end=time.time()
            print(end-start)
            a=(end-start)
            if a<=2.25:
                print("pieszesz mistrzowsko (ok. 6 znakow na sekunde)")
            elif a<=2.5 and a>2.25:
                print("Piszesz super szybko (ok. 5 znakow na sekunde)")
            elif a<=3 and a>2.5:
                print("piszesz bardzo szybko (ok. 4 znaki na sekunde)")
            elif a<=4.13 and a>3:
                print("piszesz szybko (ok. 3 znaki na sekunde)")
            elif a<=5.5 and a>4.13:
                print("piszesz średnio szybko (ok. 2 znaki na sekunde)")
            elif a<=10.4 and a>5.5:
                print("piszesz powoli (ok. 1 znak na sekunde)")
            else:
                print("piszesz bardzo powoli (mniej niż 1 znak na sekunde)")
            break
        else:
            print("zle przepisales tekst. Sproboj jeszcze raz.")

        
        
