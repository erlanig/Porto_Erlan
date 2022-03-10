# Nama file: Tugas1-3.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal:  26 Oktober 2021
# Deskripsi: menentukan apakah sebuah list sama dengan list yang lainnya

# Definisi dan Spesifikasi
# is_inverse : 2 List --> boolean
#   is_inverse(L) true jika L2 adalah list dengan urutan elemen terbalik dibandingkan
#   L1, dengan perkataan lain adalah hasil inverse dari L1

# Realisasi
def is_empty(L):
    if L == []:
        return True
    else:
        return False

def first_element(L):
    if not(is_empty(L)):
        return L[0]

def last_element(L):
    if not(is_empty(L)):
        return L[-1]

def tail_element(L):
    if not(is_empty(L)):
        return L[1:]

def is_member(L, x):
    if (is_empty(L)):
        return False
    else:
        if first_element(L) == x:
            return True
        else:
            return is_member(tail_element(L), x)

def NB_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NB_element(tail_element(L))

def head(L):
    if not(is_empty(L)):
        return L[:-1]

def prec(n):
    return n-1

def is_inverse(L1,L2):
    if NB_element(L1) == NB_element(L2):
        if is_empty(L1) and is_empty(L2):
            return True
        else:
            return first_element(L1) == last_element(L2) and is_inverse(head(tail_element(L1)), head(tail_element(L2)))
    else:
        return False

# Aplikasi
L1 = ['e',3,7,9,"Informatika"]
L2 = [1,5,"FSM",12,]
L3 = [10,9,8,7]
L4 = [7,8,9,10]
L5 = [1,2,3]
L6 = [3,4,1]

print(is_inverse(L1,L2))
print(is_inverse(L3,L4))
print(is_inverse(L5,L6))

