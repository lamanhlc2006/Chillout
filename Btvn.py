import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

def save_data():
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

    file_path = "thong_tin_nhan_vien.csv"
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False, encoding="utf-8")
    else:
        df.to_csv(file_path, mode="a", header=False, index=False, encoding="utf-8")

    messagebox.showinfo("Thành công", "Dữ liệu đã được lưu vào file CSV!")

def convert_csv_to_excel():
    csv_file = "thong_tin_nhan_vien.csv"  
    excel_file = "thong_tin_nhan_vien.xlsx" 

    if not os.path.exists(csv_file):
        messagebox.showerror("Lỗi", "Không tìm thấy file CSV!")
        return

    df = pd.read_csv(csv_file, encoding="utf-8")
    df.to_excel(excel_file, index=False, engine='openpyxl')  

    messagebox.showinfo("Thành công", f"Dữ liệu đã được chuyển sang file Excel: {excel_file}")

chill = tk.Tk()
chill.title("Nhập dữ liệu")
chill.geometry("800x300")

tt = tk.Label(chill, text="Thông tin nhân viên", font=("Arial", 16, "bold"))
tt.place(x=7, y=20)

b1 = tk.BooleanVar()
b2 = tk.BooleanVar()

a1 = tk.Checkbutton(chill, text="Là khách hàng", variable=b1)
a1.place(x=250, y=25)

a2 = tk.Checkbutton(chill, text="Là nhà cung cấp", variable=b2)
a2.place(x=400, y=25)

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

gt1 = tk.Label(chill, text="Giới tính")
gt1.place(x=540, y=60)

gender_var = tk.StringVar(value="Nam")
nam = tk.Radiobutton(chill, text="Nam", variable=gender_var, value="Nam")
nam.place(x=540, y=80)

nu = tk.Radiobutton(chill, text="Nữ", variable=gender_var, value="Nữ")
nu.place(x=600, y=80)

dv1 = tk.Label(chill, text="Đơn vị*")
dv1.place(x=7, y=105)
dv2 = tk.Entry()
dv2.place(x=10, y=125, width=330, height=20)

cn1 = tk.Label(chill, text="Chức năng")
cn1.place(x=9, y=150)
cn2 = tk.Entry()
cn2.place(x=10, y=170, width=330, height=20)

so1 = tk.Label(chill, text="Số CCCD")
so1.place(x=378, y=105)
so2 = tk.Entry()
so2.place(x=380, y=125, width=200, height=20)

ncc1 = tk.Label(chill, text="Ngày cấp")
ncc1.place(x=590, y=105)
ncc2 = tk.Entry()
ncc2.place(x=590, y=125, width=120, height=20)

nc1 = tk.Label(chill, text="Nơi cấp")
nc1.place(x=376, y=150)
nc2 = tk.Entry()
nc2.place(x=380, y=170, width=330, height=20)

btn_save = tk.Button(chill, text="Lưu dữ liệu", command=save_data, font=("Arial", 10))
btn_save.place(x=10, y=220)

btn_convert = tk.Button(chill, text="Chuyển sang Excel", command=convert_csv_to_excel, font=("Arial", 10))
btn_convert.place(x=150, y=220)

chill.mainloop()
