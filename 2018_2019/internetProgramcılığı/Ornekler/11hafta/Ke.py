boy=input("Boy gir: ")
kilo=input("kilo gir :")
boy=float(boy)/100
kilo=int(kilo)
ke=kilo/boy**2

if ke<18:
    print("zayıf")
elif ke<25:
    print("normal")
elif ke<30:
    print("kilolu")
else:
    print("obez")

print(ke)
