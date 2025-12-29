s1=0
s2=0
s=0
n=int(input('Nhap n'))
for i in range(1,n+1):
    s1+=i
print(s1)

for j in range(2,n+1):
    if n%2==0: s2 +=j
    else: s2 +=n
print(s2)
s=s1/s2
print(s)