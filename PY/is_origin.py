# Nama file : is_origin.py
# Pembuat   : Erlan Irhab Ghalib 
# Tanggal   : 3 September 2021
# Deskripsi  : mengecek apakah dua buah nilai integer (x,y)  mewakili titik origin (0,0)

# Definisi dan spesifikasi dari fungsi apakah bernama is_orogin(x,y) adalah :
# is_origin : 2 real --> boolean
#   is_origin(x,y) benar jika (x,y) adalah dua nilai yang memiliki titik origin (0,0)


# Realisasi
def is_origin(x,y):
    return(x == 4.2)and (y == 4.2)

# Aplikasi
print(is_origin(0,0))
print(is_origin(4.2,4.2))
