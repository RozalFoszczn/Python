import random
name = input("Podaj swoje imie: ")
        
 
 
wyborg = input("Wybierz kamien, nozyce lub papier: ")
 
 
 
wyborl = ["kamien", "nozyce", "papier"]
wybork = wyborl[random.randint(0, 2)]
 
wynikg = 0
wybikk = 0
 
 
 
 
if (wyborg == wybork):
    print("Komputer wybrał: " , wybork )
    print("remis")
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
elif (wyborg == "papier") and (wybork == "kamien"):
    wynikg = wynikg + 1
    print("Komputer wybrał: " , wybork )
    print("Wygrałes " + name)
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
elif (wyborg == "kamien") and (wybork == "papier"):
    wybikk = wybikk + 1
    print("Komputer wybrał: " , wybork )
    print("Przegrałes " + name)
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
elif (wyborg == "nozyce") and (wybork == "kamien"):
    wybikk = wybikk + 1
    print("Komputer wybrał: " , wybork )
    print("Przegrałes " + name)
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
elif (wyborg == "kamien") and (wybork == "nozyce"):
    wynikg = wynikg + 1
    print("Komputer wybrał: " , wybork )
    print("Wygrałes " + name)
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
elif (wyborg == "papier") and (wybork == "nozyce"):
    wybikk = wybikk + 1
    print("Komputer wybrał: " , wybork )
    print("Przegrałes " + name)
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
elif (wyborg == "nozyce") and (wybork == "papier"):
    wynikg = wynikg + 1
    print("Komputer wybrał: " , wybork )
    print("Wygrałes " + name)
    print ("Ty " , wynikg , " : " , "komputer" , wybikk)
else:
    print("wpisales zla fraze")
