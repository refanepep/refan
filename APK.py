import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import Label

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "refan" and password == "refan123":
        messagebox.showinfo("Login", "Login berhaasil!")
    else:
        messagebox.showerror("Login", "Login gagal. Coba lagi!")
        l_UI.call("wm","iconphoto", l_UI._w,PhotoImage(file="icon/green2.png"))

# Membuat jendela
root = tk.Tk()
root.title("Login")

img = PhotoImage(file='green2.png')
img_resize = img.subsample(5,5)
Label(root,image=img_resize,bg='white').pack(pady=6)

# Membuat label dan entry untuk username
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Membuat label dan Entry untuk password
label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*") # Untuk menyembunyikan karakter password
entry_password.pack()

# Membuat tombol untuk login
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()