# 600851475143 sayısının en büyük asal çarpanını bulan algoritma
sayi=600851475143
i=2
while i*i < sayi:
    while sayi%i==0:
        sayi=sayi/i
    i+=1

print(sayi)



