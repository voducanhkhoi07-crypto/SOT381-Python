
# Nhập số nguyên
n = int(input("Nhập một số nguyên: "))

# Kiểm tra chia hết cho 3 và 5
if n % 3 == 0 and n % 5 == 0:
    print(n, "chia hết đồng thời cho 3 và 5")
else:
    print(n, "không chia hết đồng thời cho 3 và 5")
