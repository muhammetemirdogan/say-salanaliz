import math
x=math.pi/5
n=int(input("girmek istediğiniz terim="))
toplam=0
sign=1
for i in range(n):
    toplam=toplam+sign*(x**(2*i))/math.factorial(2*i)
    sign=(-1)*sign
    gercek=math.cos(x)
    print("yaklasik deger=",toplam)
    print("cos(x) gercek degeri=",gercek)
    kesmehatasi=(gercek-toplam)
    print("kesme hatasi=",kesmehatasi)
