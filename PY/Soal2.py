# Nama file: Soal2.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# perkalian : 2 integer --> integer
#   perkalian(x,y) mengalikan dua buah bilangan yaitu a dengan b dengan menjumlahkan a terhadap a sebanyak b-kali secara rekursif

# Realisasi 
def perkalian(x,y):
    if y == 1:
        return x
    else:
        return x + perkalian(x,y-1)

# Aplikasi
print(perkalian(5,3))
print(perkalian(10,3))

