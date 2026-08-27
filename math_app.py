#!/usr/bin/env python3
"""
Aplikasi Matematika Sederhana
Fungsi: Kalkulator dasar, konversi satuan, dan operasi matematika lainnya
"""

import math

def add(x, y):
    """Penjumlahan"""
    return x + y

def subtract(x, y):
    """Pengurangan"""
    return x - y

def multiply(x, y):
    """Perkalian"""
    return x * y

def divide(x, y):
    """Pembagian"""
    if y == 0:
        return "Error: Pembagian dengan nol"
    return x / y

def power(x, y):
    """Pangkat"""
    return x ** y

def sqrt(x):
    """Akar kuadrat"""
    if x < 0:
        return "Error: Akar dari bilangan negatif"
    return math.sqrt(x)

def factorial(x):
    """Faktorial"""
    if x < 0:
        return "Error: Faktorial dari bilangan negatif"
    if not isinstance(x, int):
        return "Error: Faktorial hanya untuk bilangan bulat"
    return math.factorial(x)

def convert_unit(value, from_unit, to_unit):
    """Konversi satuan panjang"""
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
        return "Error: Satuan tidak didukung"
    
    # Konversi ke meter dulu, kemudian ke satuan tujuan
    meter_value = value * to_meter[from_unit]
    result = meter_value / to_meter[to_unit]
    
    return result

def calculate_area(length, width):
    """Hitung luas persegi panjang"""
    return length * width

def calculate_volume(length, width, height):
    """Hitung volume balok"""
    return length * width * height

def is_prime(n):
    """Cek apakah bilangan prima"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("=== Aplikasi Matematika ===")
    print("Pilihan:")
    print("1. Kalkulator dasar (tambah, kurang, kali, bagi)")
    print("2. Operasi matematika lanjutan")
    print("3. Konversi satuan panjang")
    print("4. Hitung luas dan volume")
    print("5. Cek bilangan prima")
    print("6. Keluar")
    
    while True:
        try:
            choice = input("\nPilih menu (1-6): ")
            
            if choice == "1":
                print("\n--- Kalkulator Dasar ---")
                x = float(input("Masukkan angka pertama: "))
                y = float(input("Masukkan angka kedua: "))
                print(f"Hasil:")
                print(f"{x} + {y} = {add(x, y)}")
                print(f"{x} - {y} = {subtract(x, y)}")  
                print(f"{x} × {y} = {multiply(x, y)}")
                print(f"{x} ÷ {y} = {divide(x, y)}")
                
            elif choice == "2":
                print("\n--- Operasi Lanjutan ---")
                x = float(input("Masukkan angka: "))
                y = float(input("Masukkan pangkat (untuk operasi pangkat): "))
                print(f"Hasil:")
                print(f"{x}^({y}) = {power(x, y)}")
                print(f"Akar kuadrat {x} = {sqrt(x)}")
                print(f"Faktorial {int(x)} = {factorial(int(x))}")
                
            elif choice == "3":
                print("\n--- Konversi Satuan ---")
                value = float(input("Masukkan nilai: "))
                from_unit = input("Dari satuan (mm, cm, m, km, inch, ft): ").lower()
                to_unit = input("Ke satuan (mm, cm, m, km, inch, ft): ").lower()
                result = convert_unit(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result} {to_unit}")
                
            elif choice == "4":
                print("\n--- Luas dan Volume ---")
                length = float(input("Panjang: "))
                width = float(input("Lebar: "))
                height = float(input("Tinggi (untuk volume): "))
                print(f"Luas persegi panjang: {calculate_area(length, width)}")
                print(f"Volume balok: {calculate_volume(length, width, height)}")
                
            elif choice == "5":
                print("\n--- Cek Bilangan Prima ---")
                n = int(input("Masukkan angka: "))
                if is_prime(n):
                    print(f"{n} adalah bilangan prima")
                else:
                    print(f"{n} bukan bilangan prima")
                    
            elif choice == "6":
                print("Terima kasih telah menggunakan aplikasi matematika!")
                break
                
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                
        except ValueError:
            print("Error: Masukkan angka yang valid")
        except KeyboardInterrupt:
            print("\n\nKeluar dari aplikasi...")
            break

if __name__ == "__main__":
    main()