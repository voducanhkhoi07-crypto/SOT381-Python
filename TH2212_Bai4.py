def sln(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max
def sbn(a,b,c):
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    return min
#Nhap du lieu
a=int(input('nhap a '))
b=int(input('nhap b '))
c=int(input('nhap c '))


nmax=sln(a,b,c)
print(f"so lon nhat la {nmax}")

nmin=sbn(a,b,c)
print(f"so nho nhat la {nmin}")