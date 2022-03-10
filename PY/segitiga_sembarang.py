# Nama file: segitiga_sembarang.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 11 September 2021
# Deskripsi : mengecek apakah benar sisi yang dimasukkan membentuk segitiga sembarang

#Definisi dan Spesifikasi:
# seg_sembarang = 3 integer>0 --> boolean
#   {seg_sembarang(a,b,c) bernilai True jika memenuhi ketiga syarat berikut yakni a+b >c , a+c>b  , b+c>a}

# Realisasi
def seg_sembarang (a, b, c) :
    if ((a !=b != c) and (a + b > c) and (a + c > b) and (b + c > a))  :
        return True
    else :
        return False
        
# Aplikasi
print(seg_sembarang(1, 2, 3))
print(seg_sembarang(1, 1, 1))
print(seg_sembarang(4, 5, 3))