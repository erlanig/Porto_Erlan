# Nama file : pangkat3_v2.py
# Pembuat : Erlan Irhab Ghalib
# Tanggal : 3 September 2021
# Deskripsi : menghitung nilai pangkat 3 dari sebuah masukan integer melalui fungsi antara

# Defisi dan spesifikasi daari fungsi pangkat2 bernama fx3v1 adalah :
# fx3v2 : integer --> integer
#   fx3v2 (x) menghitung pangkat tiga dari x, sebuah bilangan integer, menggunakan fungsi antara fx2(x)

# fx2 : integer --> integer
#   fx2(x) menghitung pangkat dua dari x, sebuah bilangan integer

# Realisasi
def fx2(x) :
    return(x*x)

def fx3v2(x) :
    return(x*fx2(x))

# Aplikasi
print(fx3v2(4))
print(fx3v2(4+2))
