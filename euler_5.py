# 1 den 20 e kadar bütün sayılara bölünen en küçük sayı

def bolunurmu(sayi):
    for i in range(1,21):
        if(sayi % i !=0):
            return 0
    return 1


sayi=2520

while bolunurmu(sayi)!=1:
    sayi+=20
    print(sayi)

print(sayi)



