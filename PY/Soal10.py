# Nama file: Soal10.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# DeretNo10 : integer --> integer
#   DeretNo10(n) menghitung deret bilangan: 1 + 4 + 9 + 16 + ....

# Realisasi
def DeretNo10(n):
    if n == 0:
        return 0
    else:
        return DeretNo10(n-1) + n**2

# Aplikasi
print(DeretNo10(1))
print(DeretNo10(2))
print(DeretNo10(3))