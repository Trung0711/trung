'''
a=int(input('nhap gia tri a:'))
b= int(input('nhap gia tri b:'))
ep=  float(input('nhap gia tri ep:'))
import math

n = (math.log(b-a)-math.log(ep)/math.log(2))
if f(a)*f(b)==0:
   if f(a)==0:
        print(" phuong trinh nhan nghiem chinh xac la gia tri a",a)
   else:
        print(" phuong trinh nhan nghiem chinh xac la gia tri b",b)
elif f(a)*f(b)>0:
    print(" toi k gia phuong trinh nay")
else:
    for i in n:
        Xm= (a+b)/2
        if f(Xm)==0:
            print(" phuong trinh co nghiem chinh xac la Xm",Xm)
        else:
            if f(Xm)*f(a)<0:
                b=Xm
            else:
                a=Xm
if f(Xm)==0:
    print(" phuong trinh co nghiem gan dung la Xm",Xm)
'''
from random import*
l=['trung','hiếu']

def ran(a):
   y=len(a)
   z=randrange(0,y-1)
   return a[z]

