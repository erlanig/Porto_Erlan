# Nama file: Soal8.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# DeretArit : integer --> integer
#   DeretArit(n) menghitung deret bilangan arimatika: 3 + 6 + 9 + 12 + ....

# Realisasi
def DeretArit(n):
    if n == 0:
        return 0
    else:
        return DeretArit(n-1) + n*3

# Aplikasi
print(DeretArit(1))
print(DeretArit(2))
print(DeretArit(3))