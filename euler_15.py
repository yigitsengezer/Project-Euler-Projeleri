# 20x20 lik alanda kac farkli gidis yolu vardir

# formul olarak (toplam kenar sayisi)!/(1. kenar sayisi)! * (2.kenar sayisi)!

from math import factorial

print(int(factorial(40)/(factorial(20)*factorial(20))))
