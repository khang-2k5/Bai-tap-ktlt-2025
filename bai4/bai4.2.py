print("Nguyễn Nhân Khang")
print("MSSV:235752020710012")
S = input('Nhap chuoi:')
for ch in S:
    if ch not in [' ', '\t']:  # Kiểm tra nếu ký tự không phải là dấu space hoặc dấu tab
        print(ch)
