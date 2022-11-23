rng1=int(input("Rango inferior:"))
rng2=int(input("Rango superior:"))
dvs=int(input("Divisor:"))

for i in range(rng1,rng2+1):
    if(i%dvs==0):
        print(i)