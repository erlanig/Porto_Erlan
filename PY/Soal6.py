# Nama file: Soal6.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# PerkalianTiga : integer --> integer
#   PerkalianTiga(n) menghitung perkalian dengan 3 atau f(n) = 3 * n

# Realiasi
def PerkalianTiga(n):
    if n == 0:
        return 0
    else:
        return PerkalianTiga(n-1) + 3

# Aplkasi
print(PerkalianTiga(1))
print(PerkalianTiga(2))
print(PerkalianTiga(3))