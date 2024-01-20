
import os
play = True
while play:
    def spr():
        if R<=0:
            print("Taka figura nie istnieje")
            
        elif H<=0:
            print("Taka figura nie istnieje")
            
        elif a<=0:
            print("Taka figura nie istnieje")
            
        elif b<=0:
            print("Taka figura nie istnieje")
            
        elif Pp<=0:
            print("Taka figura nie istnieje")
            
        else:
            print(V)

    bryla=input("podaj bryle(1=kula, 2=stozek, 3=walec, 4=prostopadloscian, 5=graniastoslop, 6=ostroslup): ")

    if bryla == "1":
        R=int(input("podaj promien: "))
        H=1
        a=1
        b=1
        Pp=1
        
        pi=3.14159
        V=pi*R*R*R*4/3
        spr()
    elif bryla=="2":
        pi=3.14159
        H=int(input("podaj wysokosc bryly: "))
        R=int(input("podaj promien: "))
        a=1
        b=1
        Pp=1

        V=pi*H*R*R/3
        spr()
    elif bryla=="3":
        pi=3.14159
        H=int(input("podaj wysokosc bryly: "))
        R=int(input("podaj promien: "))
        a=1
        b=1
        Pp=1
        
        V=pi*R*R*H
        spr()

    elif bryla=="4":
        H=int(input("podaj wysokosc bryly: "))
        a=int(input("podaj pierwsza dlugosc podstawy: "))
        b=int(input("podaj druga dlugosc podstawy: "))
        R=1
        Pp=1
        
        V=a*b*H
        spr()
        
    elif bryla=="5":
        Pp=int(input("podaj pole podstawy: "))
        H=int(input("podaj wysokosc bryly: "))
        a=1
        b=1
        R=1
        
        V=Pp*H
        spr()
          
    elif bryla =="6":
        Pp=int(input("podaj pole podstawy: "))
        H=int(input("podaj wysokosc bryly: "))
        R=1
        a=1
        b=1
        
        V=H*Pp/3
        spr()
           
    else:
        print("nie moge obliczyc objetosci tej figury")
    
    wbr=int(input("Jesli chcesz obliczyc cos jeszcze, wpisz liczbe rozna od 0, a jesli chcesz zakonczyc, wpisz 0: "))
    if wbr == 0:
        break