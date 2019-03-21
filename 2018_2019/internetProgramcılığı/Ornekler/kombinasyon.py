def faktorryel(a):
	fak=1;
	for i in range(a):
		fak=fak*(i+1)
	return fak;


def kom(n,r):
	return faktorryel(n)/
	(faktorryel(n-r)*faktorryel(r))


birler=kom(4,1)
onlar=kom(3,1)
yuzler=kom(3,1)

sonuc=birler*onlar*yuzler
print(sonuc)
