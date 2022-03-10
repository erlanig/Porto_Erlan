# Nama file: Soal9.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# DeretGeo : integer --> integer
#   DeretGeo(n) menghitung deret bilangan geometri: 1 + 3 + 9 + 27 + ....

# Realisasi
def DeretGeo(n):
    if n == 0:
        return 0
    else:
        return DeretGeo(n-1) + 3**(n-1)

# Aplikasi
print(DeretGeo(1))
print(DeretGeo(2))
print(DeretGeo(3))