from importlib import machinery
from methods.Secant import secant
from methods.Iter import Sederhana
from methods.Nraphson import nraph
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    clear_screen()
    print("="*80)
    print("Pencari Akar - Metode Numerik")
    print("="*80)
    print("Pilih Metode:")
    print("1. Iterasi Sederhana")
    print("2. Metode Newton-Raphson")
    print("3. Metode Secant")
    print("4. Quit")
    print("="*80)

def main():
    while True:
        tampilkan_menu()
        
        try:
            pilihan = int(input("Masukkan Pilihan : "))
        except ValueError:
            print("Input harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")
            continue
            
        match pilihan:
            case 1:
                clear_screen()
                print("="*40 + "ITERASI SEDERHANA" +"="*40)
                try:
                    x = float(input("Masukkan x : "))
                    galat = float(input("Masukkan galat : "))
                    iterasi = int(input("Masukkan Maksimum iterasi : "))
                    clear_screen()
                    Sederhana(x, galat, iterasi)
                except ValueError:
                    print("Input tidak valid! Masukkan angka yang benar.")
                input("\nTekan Enter Untuk Kembali ke Menu...")
                
            case 2:
                clear_screen()
                print("="*40 +"NEWTON-RAPHSON" + "="*40)
                try:
                  x = float(input("Masukkan x : "))
                  galat = float(input("Masukkan galat : "))
                  iterasi = int(input("Masukkan Maksimum iterasi : "))
                  clear_screen()
                  nraph(x, galat, iterasi)
                except ValueError:
                  print("Input tidak valid! Masukkan angka yang benar.")
                  input("\nTekan Enter Untuk Kembali ke Menu...")
                
            case 3:
                clear_screen()
                print("=== METODE SECANT ===")
                try:
                    x0 = float(input("Masukkan x0 : "))
                    x1 = float(input("Masukkan x1 : "))
                    galat = float(input("Masukkan galat : "))
                    iterasi = int(input("Masukkan Maksimum iterasi : "))
                    clear_screen()
                    secant(x0, x1, galat, iterasi)
                except ValueError:
                    print("Input tidak valid! Masukkan angka yang benar.")
                input("\nTekan Enter Untuk Kembali ke Menu...")
                
            case 4:
                clear_screen()
                print("Terima kasih telah menggunakan program ini!")
                print("Program selesai.")
                break 
                
            case _:
                print("Pilihan tidak ada! Silakan pilih 1-4.")
                input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()