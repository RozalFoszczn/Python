

import time
print("witaj.Za chwile rozpocznie sie twoj test szybkiego pisania.")
st=int(input("wpisz 1, kiedy bedziesz gotow: "))
if st == 1:
    start=time.time()
    i=input("przepisz tekst - Wszystkie komputery powinny miec na tapetach ryby: ")
    if i=="Wszystkie komputery powinny miec na tapetach ryby":
        end=time.time()
        print(end-start)
        a=(end-start)
        if a<=6:
            print("Piszesz niczym profesjonalista!")
        elif a<=9 and a>6:
            print("Piszesz bardzo szybko")
        elif a<=10:
            print("moze sproboj jeszcze raz")
        else:
            print("potrzebujesz jeszcze pocwiczyc")
    else:
        print("zle przepisales tekst. Sproboj jeszcze raz")
    str=int(input("wpisz 1, kiedy bedziesz gotow: "))
    if str == 1:
        start=time.time()
        i=input("przepisz tekst - Male ryby nurkuja w glebokiej i slodkiej wodzie: ")
        if i=="Male ryby nurkuja w glebokiej i slodkiej wodzie":
            end=time.time()
            print(end-start)
            a=(end-start)
            if a<=6:
                print("Piszesz niczym profesjonalista!")
            elif a<=7:
                print("Piszesz bardzo szybko")
            elif a<=8:
                print("Nie jest zle")
            elif a<=9:
                print("moze sproboj jeszcze raz")
            else:
                print("potrzebujesz jeszcze pocwiczyc")
        else:
            print("Znowu zle przepisales tekst. sproboj zwrocic na to wieksza uwage")
