#!/usr/bin/env python3
"""
Konfigurasi Mikrotik via SSH
IP: 10.20.99.6
User: admin
Password: (kosong)
"""

import paramiko
import sys

def configure_mikrotik():
    # Konfigurasi koneksi
    hostname = "10.20.99.6"
    username = "admin"
    password = ""  # Kosong seperti yang diminta
    
    try:
        # Membuat koneksi SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print("Menghubungkan ke Mikrotik...")
        client.connect(hostname, username=username, password=password)
        
        print("Koneksi berhasil!")
        
        # Mengeksekusi perintah untuk mengatur gateway dan DNS
        commands = [
            "/ip route add gateway=10.20.99.30",  # Set gateway
            "/ip dns set servers=1.1.1.1"         # Set DNS
        ]
        
        print("Melakukan konfigurasi...")
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            if error:
                print(f"Error pada perintah '{command}': {error}")
            else:
                print(f"Perintah '{command}' berhasil dijalankan")
                
        # Mengecek konfigurasi
        print("\n=== Cek Konfigurasi ===")
        
        # Cek route
        stdin, stdout, stderr = client.exec_command("/ip route print")
        routes = stdout.read().decode()
        print("Route:")
        print(routes)
        
        # Cek DNS
        stdin, stdout, stderr = client.exec_command("/ip dns print")
        dns = stdout.read().decode()
        print("\nDNS:")
        print(dns)
        
        # Cek interface
        stdin, stdout, stderr = client.exec_command("/interface print")
        interfaces = stdout.read().decode()
        print("\nInterfaces:")
        print(interfaces)
        
        client.close()
        print("\nKonfigurasi selesai!")
        
    except paramiko.AuthenticationException:
        print("Autentikasi gagal. Pastikan user dan password benar.")
        return False
    except paramiko.SSHException as e:
        print(f"SSH Error: {e}")
        return False
    except Exception as e:
        print(f"Error umum: {e}")
        return False
        
    return True

if __name__ == "__main__":
    print("=== Konfigurasi Mikrotik ===")
    print("IP: 10.20.99.6")
    print("User: admin")
    print("Password: (kosong)")
    print()
    
    configure_mikrotik()