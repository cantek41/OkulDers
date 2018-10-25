#1/2 + 1/4 + 1/8 + 1/16

toplam=0
for i in range(4):
    toplam=toplam + 1/2**(i+1)
    #1/1 + 1/2 + 1/3 + 1/4
    #1/2 + 1/4 + 1/8 + 1/16 **
    #1/2 + 1/4 + 1/6 + 1/8 *
print(toplam)
