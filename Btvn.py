import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Hàm lưu dữ liệu vào file CSV
def save_data():
    # Thu thập dữ liệu từ các Entry và Checkbutton
    ma = ma2.get()
    ten = ten2.get()
    ngay_sinh = ns2.get()
    gioi_tinh = gender_var.get()
    don_vi = dv2.get()
    chuc_nang = cn2.get()
    so_cccd = so2.get()
    ngay_cap = ncc2.get()
    noi_cap = nc2.get()
    la_khach_hang = "Có" if b1.get() else "Không"
    la_nha_cung_cap = "Có" if b2.get() else "Không"

    # Kiểm tra các trường bắt buộc
    if not ma or not ten or not don_vi:
        messagebox.showerror("Lỗi", "Các trường Mã, Tên và Đơn vị là bắt buộc!")
        return

    # Tạo dataframe chứa dữ liệu
    data = {
        "Mã": [ma],
        "Tên": [ten],
        "Ngày sinh": [ngay_sinh],
        "Giới tính": [gioi_tinh],
        "Đơn vị": [don_vi],
        "Chức năng": [chuc_nang],
        "Số CCCD": [so_cccd],
        "Ngày cấp": [ngay_cap],
        "Nơi cấp": [noi_cap],
        "Là khách hàng": [la_khach_hang],
        "Là nhà cung cấp": [la_nha_cung_cap]
    }

    df = pd.DataFrame(data)

    # Lưu dữ liệu vào file CSV
    file_path = "thong_tin_nhan_vien.csv"
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False, encoding="utf-8")
    else:
        df.to_csv(file_path, mode="a", header=False, index=False, encoding="utf-8")

    messagebox.showinfo("Thành công", "Dữ liệu đã được lưu vào file CSV!")

# Hàm chuyển dữ liệu từ CSV sang Excel
def convert_csv_to_excel():
    # Đọc dữ liệu từ file CSV
    csv_file = "thong_tin_nhan_vien.csv"  # Tên file CSV
    excel_file = "thong_tin_nhan_vien.xlsx"  # Tên file Excel muốn xuất ra

    if not os.path.exists(csv_file):
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV!")
        return

    # Đọc dữ liệu từ CSV và lưu vào file Excel
    df = pd.read_csv(csv_file, encoding="utf-8")
    df.to_excel(excel_file, index=False, engine='openpyxl')  # Xuất file Excel

    messagebox.showinfo("Thành công", f"Dữ liệu đã được chuyển sang file Excel: {excel_file}")

# Tạo cửa sổ chính
chill = tk.Tk()
chill.title("Nhập dữ liệu")
chill.geometry("800x300")

# Tiêu đề
tt = tk.Label(chill, text="Thông tin nhân viên", font=("Arial", 16, "bold"))
tt.place(x=7, y=20)

# Checkbutton
b1 = tk.BooleanVar()
b2 = tk.BooleanVar()

a1 = tk.Checkbutton(chill, text="Là khách hàng", variable=b1)
a1.place(x=250, y=25)

a2 = tk.Checkbutton(chill, text="Là nhà cung cấp", variable=b2)
a2.place(x=400, y=25)

# Các ô nhập liệu
ma1 = tk.Label(chill, text="Mã*")
ma1.place(x=7, y=60)
ma2 = tk.Entry()
ma2.place(x=10, y=80, width=120, height=20)

ten1 = tk.Label(chill, text="Tên*")
ten1.place(x=140, y=60)
ten2 = tk.Entry()
ten2.place(x=140, y=80, width=200, height=20)

ns1 = tk.Label(chill, text="Ngày sinh")
ns1.place(x=380, y=60)
ns2 = tk.Entry()
ns2.place(x=380, y=80, width=120, height=20)

# Giới tính (RadioButton)
gt1 = tk.Label(chill, text="Giới tính")
gt1.place(x=540, y=60)

gender_var = tk.StringVar(value="Nam")
nam = tk.Radiobutton(chill, text="Nam", variable=gender_var, value="Nam")
nam.place(x=540, y=80)

nu = tk.Radiobutton(chill, text="Nữ", variable=gender_var, value="Nữ")
nu.place(x=600, y=80)

# Đơn vị
dv1 = tk.Label(chill, text="Đơn vị*")
dv1.place(x=7, y=105)
dv2 = tk.Entry()
dv2.place(x=10, y=125, width=330, height=20)

# Chức năng
cn1 = tk.Label(chill, text="Chức năng")
cn1.place(x=9, y=150)
cn2 = tk.Entry()
cn2.place(x=10, y=170, width=330, height=20)

# Số CCCD
so1 = tk.Label(chill, text="Số CCCD")
so1.place(x=378, y=105)
so2 = tk.Entry()
so2.place(x=380, y=125, width=200, height=20)

# Ngày cấp
ncc1 = tk.Label(chill, text="Ngày cấp")
ncc1.place(x=590, y=105)
ncc2 = tk.Entry()
ncc2.place(x=590, y=125, width=120, height=20)

# Nơi cấp
nc1 = tk.Label(chill, text="Nơi cấp")
nc1.place(x=376, y=150)
nc2 = tk.Entry()
nc2.place(x=380, y=170, width=330, height=20)
5
# Nút lưu dữ liệu
btn_save = tk.Button(chill, text="Lưu dữ liệu", command=save_data, font=("Arial", 10))
btn_save.place(x=10, y=220)

# Nút chuyển CSV sang Excel
btn_convert = tk.Button(chill, text="Chuyển sang Excel", command=convert_csv_to_excel, font=("Arial", 10))
btn_convert.place(x=150, y=220)

# Chạy ứng dụng
chill.mainloop()
