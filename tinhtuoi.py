def tinhtuoi(a,b):
    return a,b
a=int(input('Nhập năm sinh'))
if a<1800:
    print('vui lòng nhập lại năm sinh')
else:
    b=2025
    tuoi= b-a
    print("tuổi",tuoi)