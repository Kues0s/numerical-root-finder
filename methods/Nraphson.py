from utils.fungsi import f, f1, f2
import os 

def nraph(x, galat, maxIter):
  while True:
    os.system("cls")
    print("="*40 + "Metode Newton Rapshon" +"="*40)
    print("1. Cek Konvergensi")
    print("2. Hitung N Rapshon")
    print("3. Kembali")
    print("="*80)
    try:
      pilihan = int(input("Masukkan Pilihan :"))
    except ValueError:
      print("Masukkan hanya angka")
      input("Tekan Enter untuk kembali")
      continue

    iterasi = 0
    match pilihan:
      case 1:
        fx = f(x)
        fx_1 = f1(x)
        fx_2 = f2(x)
        nilai = abs(fx*fx_2/pow(fx_1,2))
        if fx != 0 and fx_1 != 0 and nilai < 1:
          keterangan = "Konvergen"
          os.system("cls")
          print("="*40 + "Hasil Cek Konvergen" + "="*40)
          print(f"{"x":>10} {"f(x)":>10} {"f'(x)":>10} {"f''(x)":>10} {"Konvergen":>10} {"Keterangan":>10}")
          print(f"{x:>10} {fx:>10.4f} {fx_1:>10.4f} {fx_2:>10.4f} {nilai:>10.4f} {keterangan:>10}")
          input("tekan Enter untuk lanjut....")
        else:
          keterangan = "Divergen / Tidak Konvergen"
          os.system("cls")
          print("="*40 + "Hasil Cek Konvergen" + "="*40)
          print(f"{"x":>10} {"f(x)":>10} {"f'(x)":>10} {"f''(x)":>10} {"Konvergen":>10} {"Keterangan":>10}")
          print(f"{x:>10} {fx:>10.4f} {fx_1:>10.4f} {fx_2:>10.4f} {nilai:>10.4f} {keterangan:>10}")
          input("tekan enter untuk kembali...")
      case 2:
        os.system("cls")
        print("="*40 + "Hasil Perhitungan Metode Newton Rapshoo" + "="*40)
        print(f"{"iterasi":>10} {"x_old":>10} {"f(x)":>10} {"f'(x)":>10} {"x(new)":>10} {"abs(fx)":>10} {"Keterangan":>10}")
        print("=" * 80)
        x_old = x
        while iterasi <= maxIter :
          fx = f(x_old)
          fx_1 = f1(x_old)
          xnew = x_old-(fx/fx_1)
          absolut = abs(fx)

          if absolut <= galat:
            keterangan = "Berhenti"
            print(f"{iterasi:>10} {x_old:>10.4f} {fx:>10.4f} {fx_1:>10.4f} {xnew:>10.4f} {absolut:>10.4f} {keterangan:>10}")
            input("Tekan Enter untuk Kembali...")
            break
          else:
            keterangan = "Lanjutkan"
            print(f"{iterasi:>10} {x_old:>10.4f} {fx:>10.4f} {fx_1:>10.4f} {xnew:>10.4f} {absolut:>10.4f} {keterangan:>10}")
            x_old = xnew
            iterasi += 1
      case 3:
        os.system("cls")
        print("="*80)
        print("Terimakasih Telah Menggunakan Program kami")
        print("="*80)
        input("Tekan Enter untuk Kembali ke Menu Utama....")
        return

