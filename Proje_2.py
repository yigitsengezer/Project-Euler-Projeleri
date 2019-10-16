# 4 milyona kadar cift sayi olan fibonacci sayilarinin toplamini bulan algoritma

toplam=0
fib1=1
fib2=1
temp=0

while fib2<4000000:
    temp=fib2
    fib2+=fib1
    if(fib2%2==0):
        toplam+=fib2
    fib1=temp

print(toplam)

