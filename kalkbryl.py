
bryla=input("podaj bryle(1=kula, 2=stozek, 3=walec, 4=prostopadloscian, 5=graniastoslop, 6=ostroslup): ")

if bryla == "1":
    R=input("podaj promien: ")
    if R <= 0:
        print("Nie moge tego obliczyc")
    elif R>0:
        pi=3,14159
        R == R*R*R
        V=pi*R*4/3
        print(V)
elif bryla=="2":
    pi=3,14159
    H=int(input("podaj wysokosc bryly: "))
    R=int(input("podaj promien: "))
    if R <= 0:
        print("Nie moge tego obliczyc")
    elif H <= 0:
        print("nie moge tego obliczyc")
    elif R>0 and H>0:
        R == R*R
        V=pi*H*R/3
        print(V)
elif bryla=="3":
    pi=3,14159
    H=int(input("podaj wysokosc bryly: "))
    R=int(input("podaj promien: "))
    if R <= 0:
        print("Nie moge tego obliczyc")
    elif H <= 0:
        print("nie moge tego obliczyc")
    elif R>0 and H>0:
        R == R*R
        V=pi*R*H
        print(V)
elif bryla=="4":
    H=int(input("podaj wysokosc bryly: "))
    a=int(input("podaj pierwsza dlugosc podstawy: "))
    b=int(input("podaj druga dlugosc podstawy: "))
    if a>0 and b>0 and H>0:
        V=a*b*H
        print(V)
    else:
        print("nie moge tego obliczyc")
elif bryla=="5":
    Pp=int(input("podaj pole podstawy: "))
    H=int(input("podaj wysokosc bryly: "))
    if Pp>0 and H>0:
        V=Pp*H
        print(V)   
    else:
        print("nie moge tego obliczyc")
elif bryla =="6":
    Pp=int(input("podaj pole podstawy: "))
    H=int(input("podaj wysokosc bryly: "))
    if Pp>0 and H>0:
        V=(H*Pp)/3
        print(V)   
    else:
        print("nie moge tego obliczyc")
else:
    print("nie moge obliczyc objetosci tej figury")
