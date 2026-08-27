#!/usr/bin/env python3
"""
Monitoring Mikrotik system via SSH
IP: 10.20.99.6
User: admin
Password: (kosong)
"""

def show_mikrotik_info():
    print("=== Informasi Mikrotik ===")
    print("Target IP: 10.20.99.6")
    print("User: admin")
    print("Password: (kosong)")
    print()
    
    print("Perintah yang akan dijalankan:")
    print("1. /ip route print     # Melihat routing table")
    print("2. /ip dns print       # Melihat DNS configuration")
    print("3. /interface print    # Melihat interface")
    print("4. system resource print  # Melihat resource")
    print("5. system health print   # Melihat health")
    print()
    
    print("Catatan:")
    print("- File konfigurasi ini bisa diubah jika ingin menambahkan perintah lain")
    print("- Pastikan Anda memiliki akses SSH ke perangkat Mikrotik ini")
    print("- Library paramiko (python-ssh) harus diinstal untuk koneksi otomatis")
    print()
    
    print("Untuk menginstal dependensi:")
    print("pip3 install paramiko")
    print("Atau:")
    print("sudo apt install python3-paramiko")
    print()

if __name__ == "__main__":
    show_mikrotik_info()