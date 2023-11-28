import time
print("witaj.Za chwile rozpocznie sie twoj test szybkiego pisania.")
st=int(input("wpisz 1, kiedy bedziesz gotow: "))
if st == 1:
    start=time.time()
    i=input("przepisz tekst - Wszystkie komputery powinny miec na tapetach ryby: ")
    if i=="Wszystkie komputery powinny miec na tapetach ryby":
        end=time.time()
        print(end-start)
    else:
        print("zle przepisales tekst. Sproboj jeszcze raz")
    if end-start==