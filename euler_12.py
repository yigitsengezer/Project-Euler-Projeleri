# 500 den fazla boleni olan ilk ucgensel sayi


def ucgensayi(a):
   return sum(range(1, a+1))

bolen=0
sayi=0
deneme=0

while bolen<=500:
   bolen=0
   sayi+=1
   deneme=ucgensayi(sayi)

   i=1
   while i<=deneme**0.5:
      if deneme%i==0:
         bolen+=1
      i+=1

      #karekokune kadar kontrol edilince bolenlerin yarisi bulunmus olur

   bolen*=2
   


print(deneme)