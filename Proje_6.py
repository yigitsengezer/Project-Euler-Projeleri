#ilk 100 doğal sayının kareleri toplamı ile ilk 100 sayının toplamının karesinin farkını hesaplayan algoritma


karetoplamı=0
yuzekadartoplam=0

for i in range(1,101):
    yuzekadartoplam+=i
toplamkaresi=yuzekadartoplam**2

for i in range(1,101):
    karetoplamı+=i**2
print(toplamkaresi-karetoplamı)

