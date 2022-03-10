# Nama file: segitiga_kaki.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 11 September 2021
# Deskripsi : mengecek apakah benar sisi yang dimasukkan membentuk segitiga sama kaki

# Definisi dan Spesifikasi:
# seg_samakaki = 3 integer>0 --> boolean
#   {seg_samakaki(a,b,c) bernilai True jika a=b tetapi baik a maupun b tidak sama dengan c,
#   b=c tetapi baik b maupun c tidak sama dengan a, a=c tetapi bai k a dan c tidak sama dengan b}

# Realisasi
def seg_samakaki(a, b, c) :
    if (a == b and a != c and b != c) :
        return True

    elif (b == c and b !=a and c != a) :
        return True

    elif (a == c and a != b and c != b) :
        return True

    else :
        return False 

# Aplikasi
print(seg_samakaki(1, 1, 1))
print(seg_samakaki(5, 5, 3))
print(seg_samakaki(4, 6, 6))
print(seg_samakaki(1, 2, 1))