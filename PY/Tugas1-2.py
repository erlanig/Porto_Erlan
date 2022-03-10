# Nama file: Tugas1-2.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal:  25 Oktober 2021
# Deskripsi: menentukan apakah X adalah elemen ke N dari sebuah list

# Definisi dan Spesifikasi
# is_x_elmt_ke_n : integer >= 0, List(tidak kosong) --> boolean
#   is_x_elmt_ke_n(X,N,L) true jika X elemen ke-N list L, N>=0, dan N <= banyaknya
#   elemen list false jika tidak

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
    return L[1:]

def is_member(L, x):
    if (is_empty(L)):
        return False
    else:
        if first_element(L) == x:
            return True
        else:
            return is_member(tail_element(L), x)

def prec(n):
    return n-1

def is_x_elmt_ke_n(X,N,L):
    if is_member(L,X):
        if N == 1 and first_element(L) == X:
            return True
        else:
            return False or is_x_elmt_ke_n(X, prec(N), tail_element(L))
    else:
        return False

# Aplikasi
E1 = 'b'
F1 = 3
F2 = 1
L1 = [1,4,'b',9]
print(is_x_elmt_ke_n(E1,F1,L1))
print(is_x_elmt_ke_n(E1,F2,L1))
