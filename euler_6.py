# ilk 100 sayının toplamının karesinin ilk 100 sayının karesi toplamının farkı
karetoplam = 0
toplamkare = 0

for i in range(1,101):
    karetoplam += i**2
for i in range(1,101):
    toplamkare+=i

toplamkare = toplamkare**2

sonuc=toplamkare-karetoplam
print(sonuc)
