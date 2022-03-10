# Nama file: Soal5.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# perpangkatan : 2 integer --> integer
#   perpangkatan(x,y) memangkatkan dua buah bilangan yaitu a dengan b dengan mengalikan a terhadap a sebanyak b-kali secara rekursif

# Realisasi 
def perpangkatan(x, y):
    if y == 0:
        return 1
    else:
        return perpangkatan(x, y-1) * x

# Aplikasi
print(perpangkatan(2,2))
print(perpangkatan(4,2))