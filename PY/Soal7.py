# Nama file: Soal7.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# DeretInt : integer --> integer
#   DeretInt(n) menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ....

# Realisasi 
def DeretInt(n):
    if n == 0:
        return 0
    else:
        return DeretInt(n-1) + n

# Aplikasi
print(DeretInt(1))
print(DeretInt(2))
print(DeretInt(3))
