# Nama file: Soal3&4.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# pembagian : 2 integer --> integer
#   pembagian(x,y) membagi dua bilangan yaitu a dengan b dengan menghitung jumlah berapa kali a dikurangi b hingga a habis secara rekursif

# Realiasi
def pembagian(x, y):
    if x < y:
        return 0
    else:
        return 1 + pembagian(x-y, y)

# Aplikasi
print(pembagian(4,2))
print(pembagian(9,3))