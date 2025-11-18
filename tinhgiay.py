def tinh_giay(a,b,c):
    return a,b,c
a=int(input('nhập số giờ '))
b=int(input('Nhập số phút '))
c=int(input('Nhập số giây '))
tong=a*60*60+b*60+c
print(tong,'giây')