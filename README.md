# SOT381-Python
Nơi lưu và quản lý phiên bản  mã nguồn, lập trình python nhập môn tin học A
# Bài 1: Tính tiền điện
so_dien = int(input("Nhập số điện đã dùng: "))

tien = 0
s = so_dien

if s > 50:
    tien += 50 * 1678
    s -= 50
else:
    tien += s * 1678
    s = 0

if s > 50:
    tien += 50 * 1734
    s -= 50
else:
    tien += s * 1734
    s = 0

if s > 100:
    tien += 100 * 2014
    s -= 100
else:
    tien += s * 2014
    s = 0

if s > 150:
    tien += 150 * 2536
    s -= 150
else:
    tien += s * 2536
    s = 0

tien += s * 2927  # còn lại

print(f"Tiền điện phải trả: {tien:,} VND")

# Bài 2: Quản lý điểm học sinh
ten = input("Nhập tên học sinh: ")
toan = float(input("Điểm Toán: "))
ly = float(input("Điểm Lý: "))
hoa = float(input("Điểm Hóa: "))

dtb = (toan + ly + hoa) / 3

if dtb >= 8:
    xep_loai = "Giỏi"
elif dtb >= 6.5:
    xep_loai = "Khá"
elif dtb >= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print("\n----- KẾT QUẢ -----")
print(f"Học sinh: {ten}")
print(f"Điểm trung bình: {dtb:.2f}")
print(f"Xếp loại: {xep_loai}")
print("--------------------")


# Bài 3: Chuyển đổi nhiệt độ
nhiet_do = float(input("Nhập nhiệt độ: "))
loai = input("Nhập loại (C/F/K): ").upper()

if loai == "C":
    F = nhiet_do * 9/5 + 32
    K = nhiet_do + 273.15
    print(f"{nhiet_do}°C = {F:.2f}°F = {K:.2f}K")

elif loai == "F":
    C = (nhiet_do - 32) * 5/9
    K = C + 273.15
    print(f"{nhiet_do}°F = {C:.2f}°C = {K:.2f}K")

elif loai == "K":
    C = nhiet_do - 273.15
    F = C * 9/5 + 32
    print(f"{nhiet_do}K = {C:.2f}°C = {F:.2f}°F")

else:
    print("Loại nhiệt độ không hợp lệ!")
