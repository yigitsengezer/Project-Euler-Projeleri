# eğer sayi cift ise sayi/2   tek ise 3xsayi+1 alinarak 1 e kadar giden serinin uzunlugu en buyuk olani bul max sayi 1.000.000

max=0
uzunluk=1
sayi=0
for j in range(2,1000000):
    i=j
    while i!=1:
        if i%2==0:
            i=i/2
            uzunluk+=1
        else:
            i=i*3+1
            uzunluk+=1

    if uzunluk>max:
        max=uzunluk
        sayi=j
        print(max)
    uzunluk=1
print(sayi)
