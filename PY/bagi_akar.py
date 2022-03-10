# Nama file: bagi_akar.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 19 September 2021
# Deskripsi : menghitung hasil bagi akar persamaan kuadrat

# Definisi dan Spesifikasi:
# akar_positif : 3 integer> 0 --> real
#   {akar_positif(a,b,c) menghitung nilai akar tambah dari persamaan ax^2+bx+c menggunakan
#   rumus abc}
# akar_negatif : 3 integer > 0 --> real
#   {akar_negatif(a,b,c) menghitung nilai akar kurang dari persamaan ax^2+bx+c menggunakan
#   rumus abc}
# bagi_akar : 3 integer >0 --> real
#   {bagi_akar(g,h,i) menghitung nilai bagi dari akar_positif dan akar_negatif}

# Realisasi
def akar_positif(a,b,c):
    return (b*(-1) + (b**2-4*a*c)**0.5)//(2*a)
def akar_negatif(a,b,c):
    return (b*(-1) - (b**2-4*a*c)**0.5)//(2*a)
def bagi_akar(g,h,i):
    if akar_positif(g,h,i) >= akar_negatif(g,h,i):
        return akar_positif(g,h,i)/ akar_negatif(g,h,i)
    else :
        return akar_negatif(g,h,i)/ akar_negatif(g,h,i)

# Aplikasi
print(akar_positif(1,4,3))
print(akar_negatif(1,-6,8))
print(bagi_akar(1,4,3))