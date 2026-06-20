from utils.fungsi import g1, g2, g3, f
import os

def PilihanTampilan():
    os.system("cls")
    print("="*80)
    print("Pilihlah dari 3 bentuk g(x):")
    print("="*80)
    print("1. (x³ + x + 3) / (4x)")
    print("2. √((x³ + x + 3)/4)")
    print("3. (x³ - 4x² + 5x + 3)/4")
    print("4. Exit")
    print("="*80)

def Sederhana(x, galat, maxIter):
    while True:  # Loop untuk menu
        PilihanTampilan()
        
        try:
            pilihan = int(input("Masukkan Pilihan: "))
        except ValueError:
            print("Input harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")
            continue
        
        # Reset iterasi untuk setiap pilihan
        iterasi = 0
        x_awal = x  # Simpan nilai x awal
        
        match pilihan:
            case 1:
                os.system("cls")
                print("="*80)
                print("Hasil Dari Metode Iterasi Sederhana - g(x) = (x³ + x + 3) / (4x)")
                print("="*80)
                print(f"{'iterasi':>8} {'x':>10} {'g(x)':>10} {'f(x)':>10} {'abs(fx)':>10} {'Keterangan':>12}")
                print("-"*80)
                
                while iterasi <= maxIter:
                    gx = g1(x_awal)
                    fx = f(x_awal)
                    fx_abs = abs(fx)
                    
                    if fx_abs <= galat:
                        print(f"{iterasi:>8} {x_awal:>10.4f} {gx:>10.4f} {fx:>10.4f} {fx_abs:>10.4f} {'BERHENTI':>12}")
                        print(f"\n✓ Akar ditemukan: x = {x_awal:.4f}")
                        break
                    else:
                        print(f"{iterasi:>8} {x_awal:>10.4f} {gx:>10.4f} {fx:>10.4f} {fx_abs:>10.4f} {'LANJUT':>12}")
                        x_awal = gx
                        iterasi += 1
                else:
                    print(f"\n✗ Gagal konvergen setelah {maxIter} iterasi!")
                input("\nTekan Enter untuk kembali ke menu...")
                
            case 2:
                os.system("cls")
                print("="*80)
                print("Hasil Dari Metode Iterasi Sederhana - g(x) = √((x³ + x + 3)/4)")
                print("="*80)
                print(f"{'iterasi':>8} {'x':>10} {'g(x)':>10} {'f(x)':>10} {'abs(fx)':>10} {'Keterangan':>12}")
                print("-" * 70)
                while iterasi <= maxIter:
                    gx = g2(x_awal)
                    fx = f(x_awal)
                    fx_abs = abs(fx)
                    if fx_abs <= galat:
                        print(f"{iterasi:>8} {x_awal:>10.4f} {gx:>10.4f} {fx:>10.4f} {fx_abs:>10.4f} {'BERHENTI':>12}")
                        print(f"\n✓ Akar ditemukan: x = {x_awal:.4f}")
                        break
                    else:
                        print(f"{iterasi:>8} {x_awal:>10.4f} {gx:>10.4f} {fx:>10.4f} {fx_abs:>10.4f} {'LANJUT':>12}")
                        x_awal = gx
                        iterasi += 1
                else:
                    print(f"\n✗ Gagal konvergen setelah {maxIter} iterasi!")
                input("\nTekan Enter untuk kembali ke menu...")
                
            case 3:
                os.system("cls")
                print("="*80)
                print("Hasil Dari Metode Iterasi Sederhana - g(x) = (x³ - 4x² + 5x + 3)/4")
                print("="*80)
                print(f"{'iterasi':>8} {'x':>10} {'g(x)':>10} {'f(x)':>10} {'abs(fx)':>10} {'Keterangan':>12}")
                print("-" * 70)
                while iterasi <= maxIter:
                    gx = g3(x_awal)
                    fx = f(x_awal)
                    fx_abs = abs(fx)
                    if fx_abs <= galat:
                        print(f"{iterasi:>8} {x_awal:>10.4f} {gx:>10.4f} {fx:>10.4f} {fx_abs:>10.4f} {'BERHENTI':>12}")
                        print(f"\n✓ Akar ditemukan: x = {x_awal:.4f}")
                        break
                    else:
                        print(f"{iterasi:>8} {x_awal:>10.4f} {gx:>10.4f} {fx:>10.4f} {fx_abs:>10.4f} {'LANJUT':>12}")
                        x_awal = gx
                        iterasi += 1
                else:
                    print(f"\n✗ Gagal konvergen setelah {maxIter} iterasi!")
                input("\nTekan Enter untuk kembali ke menu...")
                
            case 4:
                os.system("cls")
                print("="*80)
                print("Terima kasih telah menggunakan program ini!")
                print("="*80)
                return  # Keluar dari fungsi
            
            case _:
                print("Pilihan tidak valid! Silakan pilih 1-4.")
                input("Tekan Enter untuk melanjutkan...")