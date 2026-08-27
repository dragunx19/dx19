import tkinter as tk

def tambah(nilai):
    entry.insert(tk.END, nilai)

def hitung():
    try:
        hasil = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(hasil))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def reset():
    entry.delete(0, tk.END)

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")

# Entry untuk menampilkan input dan hasil
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Tombol angka dan operator (menambahkan 'C' agar bisa reset)
tombol = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0

for btn in tombol:
    if btn == '=':
        tk.Button(root, text=btn, font=("Arial", 18),
        command=hitung).grid(row=row, column=col, sticky="nsew", padx=2,
        pady=2)
    elif btn == 'C':
        tk.Button(root, text=btn, font=("Arial", 18),
        command=reset).grid(row=row, column=col, sticky="nsew", padx=2,
        pady=2)
    else:
        tk.Button(root, text=btn, font=("Arial", 18), command=lambda x=btn:
        tambah(x)).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    col += 1
    if col > 3:
        row += 1
        col = 0

# Mengatur ukuran kolom dan baris
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6): # Disesuaikan karena ada tombol C
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
