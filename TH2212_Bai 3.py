#nhap du lieu
a=int(input('nhap a '))
b=int(input('nhap b '))
c=int(input('nhap c '))
max =a
min =a
#TINH TOASN
if b>max:
    max=b
if c>max:
    max=c
if b<min:
    min=b
if c<min:
    min=c
#XUAT DL
print('so be nhat la: ',min)
print('so lon nhat la: ',max)