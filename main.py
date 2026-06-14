from methods.Secant import secant
import os

print("Pencari Akar - Metode Numerik")
print("-------------------------------------")
print("")
print("Pilih Metode:")
print("1. Iterasi Sederhana")
print("2. Metode Newton-Raphson")
print("3. Metode Secant")
print("4. Quit")

pilihan = int(input("Masukkan Pilihan : "))

match pilihan:
  case 1:
    # iterasi_sederhana()
    pass
  case 2:
    # newton_raphson()
    pass
  case 3:
    os.system("cls")
    x0 = float(input("Masukkan x0 : "))
    x1 = float(input("Masukkan x1 : "))
    galat = float(input("Masukkan galat : "))
    iterasi = int(input("Masukkan iterasi : "))
    os.system("cls")
    secant(x0, x1, galat, iterasi)
  case 4:
    quit()
  case _:
    print("Pilihan tidak ada")