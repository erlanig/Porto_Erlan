# Nama file : IsValid.py
# Pembuat : Erlan Irhab Ghalib
# Tanggal : 3 September 2021
# Deskripsi : menghasilkan sebuah nilai boolean yang bernilai benar jika (x) bernilai lebih kecil daari 5 atau lebih besar dari 500

# Defisi dan spesifikasi dari fungsi IsValid (x) adalah :
# IsValid : integer --> boolean
#       IsValid(x) benar jika (x) bernilai lebih kecil daari 5 atau lebih besar dari 500
# Realisasi
def IsValid(x) :
    return x<5 or x>500
    
# Aplikasi
print(IsValid(5))
print(IsValid(0))
print(IsValid(500))
print(IsValid(6000))
