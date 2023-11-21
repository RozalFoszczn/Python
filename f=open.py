f=open("text.txt", "r")
print(f.read())

for i in f:
    print("Linijka: ", i)
f.close()

f=open("text.txt", "a")
