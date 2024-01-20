import os
play = True
while play:
    ilosc=int(input("podaj ilosc: "))
    jednostka1=input("podaj jednostke poczatkowa(m, km, cm, mm, in, ft): ")
    jednostka2=input("na jaka jednostke chcesz przeliczyc(m, km, cm, mm, in, ft): ")

    if jednostka1 == "mm":
        if jednostka2=="mm":
            print(ilosc)
        elif jednostka2=="cm":
            ilosc /= 10
            print(ilosc)
        elif jednostka2=="m":
            ilosc /= 1000
            print(ilosc)
        elif jednostka2=="km":
            ilosc /= 1000000
            print(ilosc)
        elif jednostka2=="in":
            ilosc *= 0.039
            print(ilosc)
        elif jednostka2=="ft":
            ilosc *= 0.00328
            print(ilosc)  
    elif jednostka1 == "cm":
        if jednostka2=="mm":
            ilosc *= 10
            print(ilosc)
        elif jednostka2=="cm":
            print(ilosc)
        elif jednostka2=="m":
            ilosc /= 100
            print(ilosc)
        elif jednostka2=="km":
            ilosc /= 100000
            print(ilosc) 
        elif jednostka2=="in":
            ilosc *= 0.3937
            print(ilosc)
        elif jednostka2=="ft":
            ilosc *= 0.032808
            print(ilosc) 
    elif jednostka1 == "m":
        if jednostka2=="mm":
            ilosc *= 1000
            print(ilosc)
        elif jednostka2=="cm":
            ilosc *= 100
            print(ilosc)
        elif jednostka2=="m":
            print(ilosc)
        elif jednostka2=="km":
            ilosc /= 1000
            print(ilosc)
        elif jednostka2=="in":
            ilosc *= 39.37
            print(ilosc)
        elif jednostka2=="ft":
            ilosc *= 3.2808
            print(ilosc)       
    elif jednostka1 == "km":
        if jednostka2=="mm":
            ilosc *= 1000000
            print(ilosc)
        elif jednostka2=="cm":
            ilosc *= 100000
            print(ilosc)
        elif jednostka2=="m":
            ilosc *= 1000
            print(ilosc)
        elif jednostka2=="km":
            print(ilosc)
        elif jednostka2=="in":
            ilosc *= 39370.0787
            print(ilosc)
        elif jednostka2=="ft":
            ilosc *= 3280.8399
            print(ilosc)
    elif jednostka1 == "in":
        if jednostka2=="mm":
            ilosc *= 25.4
            print(ilosc)
        elif jednostka2=="cm":
            ilosc *= 2.54
            print(ilosc)
        elif jednostka2=="m":
            ilosc *= 0.0254
            print(ilosc)
        elif jednostka2=="km":
            ilosc *= 0.0000254
            print(ilosc)
        elif jednostka2=="in":
            print(ilosc)
        elif jednostka2=="ft":
            ilosc *= 0.08333
            print(ilosc)
    elif jednostka1 == "ft":
        if jednostka2=="mm":
            ilosc *= 304.8
            print(ilosc)
        elif jednostka2=="cm":
            ilosc *= 30.48
            print(ilosc)
        elif jednostka2=="m":
            ilosc *= 0.3048
            print(ilosc)
        elif jednostka2=="km":
            ilosc *= 0.0003048
            print(ilosc)
        elif jednostka2=="in":
            ilosc *= 12
            print(ilosc)
        elif jednostka2=="ft":
            print(ilosc)        
    else:
        print("nie przeliczam na taka jednostke")
    wyb=int(input("Jesli chcesz liczyc dalej wpisz liczbe rozna od 0. Jeśli chcesz zakonczyc, wpisz 0: "))
    if wyb==0:
        break