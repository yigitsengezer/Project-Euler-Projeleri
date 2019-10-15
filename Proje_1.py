
#1000 sayisina kadar 3 ve 5 in butun 
#katlarinin toplamaini bulan algoritma

toplam=0

for i in range(1000):
	if(i%3==0 or i%5==0):
		toplam+=i

print(toplam)
