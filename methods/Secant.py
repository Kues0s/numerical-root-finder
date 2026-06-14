from utils.fungsi import f

def secant(x0, x1, galat, maxIter):
  iterasi = 0
  print("="*120)
  print("Hasil Iterasi Metode Secant")
  print("="*120)
  print("")
  print(f" {"iterasi":>8} {"x0":>8} {"x1":>8} {"f(x0)":>8} {"f(x1)":>8} {"xnew":>8} {"error":>8} {"keterangan":>8}")
  while iterasi <= maxIter:
    f_x0 = f(x0)
    f_x1 = f(x1)
    xnew = x1 - f_x1*(x1-x0)/(f_x1-f_x0)
    error = abs(xnew - x1)
    if error < galat:
      keterangan = "Berhenti"
      print(f" {iterasi:>8}  {x0:>8.3f}  {x1:>8.3f}  {f_x0:>8.3f}  {f_x1:>8.3f}  {xnew:>8.3f}  {error:>8.3f}  {keterangan}")
      break
    else:
      keterangan = "Lanjutkan"
      print(f" {iterasi:>8}  {x0:>8.3f}  {x1:>8.3f}  {f_x0:>8.3f}  {f_x1:>8.3f}  {xnew:>8.3f}  {error:>8.3f}  {keterangan}")
      x0 = x1
      x1 = xnew
      iterasi += 1
  print("")
  print(f"Akar yang ditemukan adalah {xnew:.3f}")