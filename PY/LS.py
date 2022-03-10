# Nama file : LS.py
# Pembuat : Erlan Irhab Ghalib
# Tanggal : 5 September 2021
# Deskripsi : menghasilkan sebuah nilai real yang pengertiannya adalah
# dua pasang titik pada koordinat kartesian, dan menghasilkan sebuah bilangan
# riil yang merupakan jarak dari kedua titik tersebut

# Defisi dan spesifikasi dari fungsi LS(x1,x2,y1,y2) adalah :
# LS : 4 real --> real
#       LS(x1,x2,y1,y2) aadalah jarak anatara dua buah titik (x1,x2) dengan (y1,y2)

# dif2 : 2 real --> real
#       dif2(x,y) adalah kaudrat dari selisih antara x dan y

# FX2 : real --> real
#       FX2(x) adalah hasil kuadrat dari x

# Realisasi
def fx2(x):
    return(x*x)
def dif2(x,y):
    return fx2(x-y)
def LS(x1,y1,x2,y2):
    return (dif2(y2,y1) + dif2(x2,x1))**0.5

# Aplikasi
print(LS(1,3,5,6))
