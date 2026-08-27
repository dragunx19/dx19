#!/usr/bin/env python3
"""
Aplikasi Matematika Sederhana - Versi Ringkas
"""

def show_menu():
    print("\n=== Aplikasi Matematika ===")
    print("Fungsi yang tersedia:")
    print("1. Penjumlahan")
    print("2. Pengurangan") 
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol"
    return x / y

def main():
    print("Aplikasi Matematika Siap Digunakan")
    print("Fitur dasar sudah tersedia")
    
    # Demonstrasi beberapa fungsi
    print("\n--- Contoh Penggunaan ---")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 × 7 = {multiply(6, 7)}")
    print(f"15 ÷ 3 = {divide(15, 3)}")
    
    print("\nAplikasi siap digunakan. Untuk menjalankan menu interaktif:")
    print("1. Jalankan dengan: python3 simple_math.py")
    print("2. Buka aplikasi melalui shortcut 'dx19-math' di menu aplikasi")

if __name__ == "__main__":
    main()