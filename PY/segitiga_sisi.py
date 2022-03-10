# Nama file: segitiga_sisi.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 11 September 2021
# Deskripsi : mengecek apakah benar sisi yang dimasukkan membentuk segitiga sama sisi

# Definisi dan Spesifikasi:
# seg_samasisi = 3 integer>0 --> boolean
#   {seg_samasisi(a,b,c) bernilai True jika a=b=c}

# Return
def seg_samasisi(a, b, c) :
    if a==b==c :
        return True
        
    else :
        return False

# Aplikasi
print(seg_samasisi(1, 1, 1))
print(seg_samasisi(1, 2, 3))
print(seg_samasisi(2, 2, 2))