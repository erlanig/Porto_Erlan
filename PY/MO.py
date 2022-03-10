# Nama file : MO.py
# Pembuat : Erlan Irhab Ghalib
# Tanggal : 3 September 2021
# Deskripsi : menghitung rata-rata dari dua buah bilangan integer, yang bukan maksimum dan bukan minimum dari 4 buah integer: (u+v+w+x-min4 (u,v,w,x)-max(u,v,w,x))/2

# Defisi dan spesifikasi dari fungsi MO(u,v,w,x) adalah :
# max4 : 4 integer>0 --> integer
#   max4(i,j,k,l) menentukan nilai maksimum dari 4 bilangan integer i,j,k, dan l

# min4 : 4 integer>0 --> integer
#   min4(i,j,k,l) menentukan nilai minimum dari 4 bilangan integer i,j,k, dan l

# max2 : 2 integer>0 --> integer
#   max2(a,b)menentukan nilai maksimum dari 2 bilangan integer a dan b

# min2 : 2 integer>0 --> integer
#   min(a,b)menentukan nilai minimum dari 2 bilangan integer a dan b

# Realisasi
def max2(a,b):
    return((a+b) + abs(a-b))/2

def min2(a,b):
    return((a+b) - abs(a-b))/2

def max4(i,j,k,l):
    return max2(max2(i,j),max2(k,l))

def min4(i,j,k,l):
    return min2(min2(i,j),min2(k,l))

def MO(u,v,w,x) :
    return(u+v+w+x-min4(u,v,w,x)-(max(u,v,w,x))) /2

# Aplikasi
print(MO(8,12,10,30))
