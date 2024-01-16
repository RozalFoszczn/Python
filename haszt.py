import time
n=int(input("Podaj liczbę całkowitą: "))
start=time.time()
for i in range(n):
    for j in range(n):
        print("#", end='')
    print()
 
end=time.time()
print(end-start)