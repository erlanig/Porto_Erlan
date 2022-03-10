# Nama file : max3.py
# Pembuat : Erlan Irhab Ghalib
# Tanggal : 3 September 2021
# Deskripsi : meenentukan nilai maksimum dari 3 bilangan integer

# Defisi dan spesifikasi daari fungsi max3(a,b,c) adalah :
# max3 : integer --> integer
#   max3(a,b,c) menentukan nilai maksimum dari 3 bilangan integer a, b dan c, menggunakan fungsi antara max2(a,b)

# max2 : integer --> integer
#   max2(a,b)menentukan nilai maksimum dari 2 bilangan integer a dan b

# Realisasi
def max2(a,b):
    return((a+b) + abs(a-b)) // 2

def max3(a,b,c):
    return max2(max2(a,b),c)

# Aplikasi
print(max3(4,9,-10))
print(max3(100,-20,300))


