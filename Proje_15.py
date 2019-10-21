#20x20 gridde kac farkli yoldan gidilir
import math as mat
kenarsayisi1=20
kenarsayisi2=20
toplam=kenarsayisi1+kenarsayisi2
yol=mat.factorial(toplam)/(mat.factorial(kenarsayisi1)*mat.factorial(kenarsayisi2))

print(yol)