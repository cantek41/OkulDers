boy=input("boy girin ")
kilo=input("kilo: ")

boy=float(boy)/100
ke=int(kilo)/boy**2

if ke<19:
    print("Zayıf")
elif ke<25:
    print("Orta")
elif ke<30:
    print("Şişko")
else:
    print("Obez")
print(ke)
