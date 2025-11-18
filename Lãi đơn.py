def lai(a,b,c):
    return a,b,c
a=int(input('Nhập số tiền gửi (VND) '))
b=float(input('Nhập lãi suất (%/năm) '))
c=int(input('Nhập số tháng gửi (tháng) '))
Lai=(a*(b/100)*c)/12
print('Lãi: ',Lai,'VND')
