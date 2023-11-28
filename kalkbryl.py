
bryla=input("podaj bryle(1=kula, 2=stozek, 3=walec, 4=prostopadloscian, 5=graniastoslop, 6=ostroslup): ")

if bryla == "1":
    R=input("podaj promien: ")
    pi=3,14159
    R == R*R*R
    V=pi*R*4/3
    print(V)
elif bryla=="2":
    pi=3,14159
    H=int(input("podaj wysokosc bryly: "))
    R=int(input("podaj promien: "))
    R == R*R
    V=pi*H*R/3
    print(V)
elif bryla=="3":
    pi=3,14159
    H=int(input("podaj wysokosc bryly: "))
    R=int(input("podaj promien: "))
    R == R*R
    V=pi*R*H
    print(V)
elif bryla=="4":
    H=int(input("podaj wysokosc bryly: "))
    a=int(input("podaj pierwsza dlugosc podstawy: "))
    b=int(input("podaj druga dlugosc podstawy: "))
    V=a*b*H
    print(V)
elif bryla=="5":
    Pp=int(input("podaj pole podstawy: "))
    H=int(input("podaj wysokosc bryly: "))
    V=Pp*H
    print(V)
elif bryla =="6":
    Pp=int(input("podaj pole podstawy: "))
    H=int(input("podaj wysokosc bryly: "))
    V=(H*Pp)/3
    print(V)
else:
    print("nie moge obliczyc objetosci tej figury")
