# Nama file : IsPositif.py
# Pembuat : Erlan Irhab Ghalib
# Tanggal : 3 September 2021
# Deskripsi : menghasilkan sebuah nilai boolean yang bernilai benar jika bilangan
# tersebut positif atau False jika bilangan tersebut negatif

# Defisi dan spesifikasi dari fungsi IsPositif(x) adalah :
# IsPositif : integer --> boolean
#       IsPositif (x) benar jika x positif
# Realisasi
def IsPositif(x):
    return x>=0

# Aplikasi
print(IsPositif(1))
print(IsPositif(0))
print(IsPositif(-1))
