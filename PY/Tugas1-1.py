# Nama file: Tugas1-1.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal:  25 Oktober 2021
# Deskripsi: menentukan elemen ke N dari sebuah list

# Definisi dan Spesifikasi
# elmt_ke_n : integer >=, List(tidak kosong) --> elemen
#   elmt_ke_n(L) menghasilkan elemen ke-N list L, N >= 0, dan N <= banyaknya elemen list

# Realisasi : Dengan Konso
def is_empty(L):
    if L == []:
        return True
    else:
        return False

def first_element(L):
    if not(is_empty(L)):
        return L[0]

def tail_element(L):
    if not(is_empty(L)):
        return L[1:]

def prec(n):
    return n-1

def elmt_ke_n(N, L):
    if N == 1:
        return first_element(L)
    else:
        return elmt_ke_n(prec(N), tail_element(L))

# Aplikasi
E1 = 3
E2 = 4
L1 = [2,8,'e',14]
L2 = [1,2,3,"IF",9,8]
print(elmt_ke_n(E1, L1))
print(elmt_ke_n(E2, L2))