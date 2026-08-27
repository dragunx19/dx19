#!/usr/bin/env python3
"""
Aplikasi Matematika GUI dengan Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("dx19-math - Aplikasi Matematika")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Membuat frame utama
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Judul
        title_label = ttk.Label(main_frame, text="=== Aplikasi Matematika ===", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Frame untuk kalkulator dasar
        calc_frame = ttk.LabelFrame(main_frame, text="Kalkulator Dasar", padding="10")
        calc_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Input untuk kalkulator
        ttk.Label(calc_frame, text="Angka 1:").grid(row=0, column=0, sticky=tk.W)
        self.num1_entry = ttk.Entry(calc_frame, width=20)
        self.num1_entry.grid(row=0, column=1, padx=(5, 0))
        
        ttk.Label(calc_frame, text="Angka 2:").grid(row=1, column=0, sticky=tk.W)
        self.num2_entry = ttk.Entry(calc_frame, width=20)
        self.num2_entry.grid(row=1, column=1, padx=(5, 0))
        
        # Tombol kalkulator
        calc_button_frame = ttk.Frame(calc_frame)
        calc_button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Button(calc_button_frame, text="Tambah (+)", command=self.add).pack(side=tk.LEFT, padx=5)
        ttk.Button(calc_button_frame, text="Kurang (-)", command=self.subtract).pack(side=tk.LEFT, padx=5)
        ttk.Button(calc_button_frame, text="Kali (×)", command=self.multiply).pack(side=tk.LEFT, padx=5)
        ttk.Button(calc_button_frame, text="Bagi (÷)", command=self.divide).pack(side=tk.LEFT, padx=5)
        
        # Hasil kalkulator
        self.calc_result = ttk.Label(calc_frame, text="Hasil akan muncul di sini", font=("Arial", 10, "bold"))
        self.calc_result.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        
        # Frame untuk fungsi lainnya
        func_frame = ttk.LabelFrame(main_frame, text="Fungsi Lain", padding="10")
        func_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Tombol fungsi lain
        ttk.Button(func_frame, text="Akar Kuadrat", command=self.sqrt).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(func_frame, text="Pangkat", command=self.power).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(func_frame, text="Faktorial", command=self.factorial).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(func_frame, text="Cek Prima", command=self.is_prime).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(func_frame, text="Konversi Satuan", command=self.convert_unit).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(func_frame, text="Luas Persegi Panjang", command=self.calculate_area).grid(row=1, column=2, padx=5, pady=5)
        
        # Frame untuk konversi satuan
        unit_frame = ttk.LabelFrame(main_frame, text="Konversi Satuan", padding="10")
        unit_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(unit_frame, text="Nilai:").grid(row=0, column=0, sticky=tk.W)
        self.unit_value_entry = ttk.Entry(unit_frame, width=20)
        self.unit_value_entry.grid(row=0, column=1, padx=(5, 0))
        
        ttk.Label(unit_frame, text="Dari:").grid(row=1, column=0, sticky=tk.W)
        self.from_unit = ttk.Combobox(unit_frame, values=["mm", "cm", "m", "km", "inch", "ft"], width=12)
        self.from_unit.grid(row=1, column=1, padx=(5, 0))
        self.from_unit.set("m")
        
        ttk.Label(unit_frame, text="Ke:").grid(row=2, column=0, sticky=tk.W)
        self.to_unit = ttk.Combobox(unit_frame, values=["mm", "cm", "m", "km", "inch", "ft"], width=12)
        self.to_unit.grid(row=2, column=1, padx=(5, 0))
        self.to_unit.set("cm")
        
        self.unit_result = ttk.Label(unit_frame, text="Hasil konversi akan muncul di sini", font=("Arial", 10, "bold"))
        self.unit_result.grid(row=3, column=0, columnspan=2, pady=(10, 0))
        
        # Frame untuk luas dan volume
        area_volume_frame = ttk.LabelFrame(main_frame, text="Luas & Volume", padding="10")
        area_volume_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(area_volume_frame, text="Panjang:").grid(row=0, column=0, sticky=tk.W)
        self.length_entry = ttk.Entry(area_volume_frame, width=15)
        self.length_entry.grid(row=0, column=1, padx=(5, 0))
        
        ttk.Label(area_volume_frame, text="Lebar:").grid(row=1, column=0, sticky=tk.W)
        self.width_entry = ttk.Entry(area_volume_frame, width=15)
        self.width_entry.grid(row=1, column=1, padx=(5, 0))
        
        ttk.Label(area_volume_frame, text="Tinggi:").grid(row=2, column=0, sticky=tk.W)
        self.height_entry = ttk.Entry(area_volume_frame, width=15)
        self.height_entry.grid(row=2, column=1, padx=(5, 0))
        
        ttk.Button(area_volume_frame, text="Hitung Luas", command=self.calculate_area).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(area_volume_frame, text="Hitung Volume", command=self.calculate_volume).grid(row=3, column=1, padx=5, pady=5)
        
        self.area_volume_result = ttk.Label(area_volume_frame, text="Hasil akan muncul di sini", font=("Arial", 10, "bold"))
        self.area_volume_result.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        
        # Frame untuk informasi
        info_frame = ttk.LabelFrame(main_frame, text="Informasi", padding="10")
        info_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.info_text = tk.Text(info_frame, height=8, width=70)
        self.info_text.grid(row=0, column=0)
        self.info_text.insert(tk.END, "Aplikasi Matematika dengan GUI\n\nFitur:\n- Kalkulator dasar (penjumlahan, pengurangan, perkalian, pembagian)\n- Operasi matematika lanjutan (akar kuadrat, pangkat, faktorial)\n- Konversi satuan panjang (mm, cm, m, km, inch, ft)\n- Hitung luas dan volume\n- Cek bilangan prima\n\nVersi 1.1 - Fitur Tambahan")
        
        # Tombol keluar
        ttk.Button(main_frame, text="Keluar", command=root.quit).grid(row=6, column=0, columnspan=3, pady=(10, 0))
        
        # Membuat konfigurasi agar grid meresize dengan window
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")
            return None, None
    
    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 + num2
            self.calc_result.config(text=f"Hasil: {result}")
    
    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 - num2
            self.calc_result.config(text=f"Hasil: {result}")
    
    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = num1 * num2
            self.calc_result.config(text=f"Hasil: {result}")
    
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            if num2 == 0:
                self.calc_result.config(text="Error: Pembagian dengan nol")
            else:
                result = num1 / num2
                self.calc_result.config(text=f"Hasil: {result}")
    
    def sqrt(self):
        try:
            num = float(self.num1_entry.get())
            if num < 0:
                messagebox.showerror("Error", "Akar dari bilangan negatif")
            else:
                result = math.sqrt(num)
                messagebox.showinfo("Hasil", f"Akar kuadrat {num} = {result}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")
    
    def power(self):
        try:
            base = float(self.num1_entry.get())
            exp = float(self.num2_entry.get())
            result = base ** exp
            messagebox.showinfo("Hasil", f"{base} ^ {exp} = {result}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")
    
    def factorial(self):
        try:
            num = int(self.num1_entry.get())
            if num < 0:
                messagebox.showerror("Error", "Faktorial dari bilangan negatif")
            else:
                result = math.factorial(num)
                messagebox.showinfo("Hasil", f"{num}! = {result}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan bilangan bulat yang valid")
    
    def is_prime(self):
        try:
            num = int(self.num1_entry.get())
            if num < 2:
                result = False
            else:
                result = True
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        result = False
                        break
            messagebox.showinfo("Hasil", f"{num} {'adalah' if result else 'bukan'} bilangan prima")
        except ValueError:
            messagebox.showerror("Error", "Masukkan bilangan bulat yang valid")
    
    def convert_unit(self):
        try:
            value = float(self.unit_value_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            
            # Konversi ke meter sebagai unit dasar
            to_meter = {
                'mm': 0.001,
                'cm': 0.01,
                'm': 1,
                'km': 1000,
                'inch': 0.0254,
                'ft': 0.3048
            }
            
            if from_unit not in to_meter or to_unit not in to_meter:
                self.unit_result.config(text="Satuan tidak didukung")
                return
            
            meter_value = value * to_meter[from_unit]
            result = meter_value / to_meter[to_unit]
            self.unit_result.config(text=f"{value} {from_unit} = {result:.4f} {to_unit}")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai yang valid")
    
    def calculate_area(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            area = length * width
            self.area_volume_result.config(text=f"Luas persegi panjang: {area}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai yang valid")
            
    def calculate_volume(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())
            volume = length * width * height
            self.area_volume_result.config(text=f"Volume balok: {volume}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai yang valid")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()