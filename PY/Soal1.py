# Nama file: Soal1.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 22 Oktober 2021
# Deskripsi: Membuat fungsi-fungsi operasi dalam matematika dengan menggunakan rekursi

# Definisi dan Spesifikasi
# pengurangan : 2 integer --> integer
#   pengurangan(a, b) mengurangkan dua buah bilangan yaitu a dengan b

# Realisasi
def pengurangan(x,y):
    if y == 0:
        return x
    else:
        return pengurangan(x, y-1) - 1

# Aplikasi
print(pengurangan(8,4))
'''
peng(8,3)-1
peng(8,2)-1-1
peng(8,1)-1-1-1
peng(8,0)-1-1-1-1
'''
print(pengurangan(12,4))