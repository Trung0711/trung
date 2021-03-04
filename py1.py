a=int(input('nhap a='))
b=int(input('nhap b= '))
c=int(input('nhap gia tri c:'))
import math
if a==0:
    if b==0:
        if c==0:
            print("phuong trinh vo so nghiem")
        else:
            print(" phuong trinh vo nghiem")
    else:
        x=(-c)/(b)
        print(" phuong trinh co nghiem  la: ",x)
else:
    delta= b*b- 4*a*c
    if delta==0:
        x=(-b)/(2*a)
        print("phuong trinh co nghiem kep la : ", x)
    elif delta <0:
        print(" phuong trinh vo nghiem")
    else:
        x1=(-b+ math.sqrt(delta))/(2*a)
        x2=(-b- math.sqrt(delta))/(2*a)
        print("nghiem cua phuong trinh laf : ",x1,"va",x2)
