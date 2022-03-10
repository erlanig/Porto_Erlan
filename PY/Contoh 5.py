# Nama file: Contoh 5.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  9 November 2021
# Deskripsi: Menghapus sebuah elemen(atom) dari list of list

# Definisi dan Spesifikasi
# Max List of list tidak kosong → integer
# Max (S) menghasilkan nilai elemen (atom) yang maksimum dari S}

# Max2 2 integer → integer
# Max2(a,b) menghasilkan nilai maksimum a dan b

# Realisasi
def IsEmptyLoL(S):
    return S == []

def FirstList(S):
    if not(IsEmptyLoL(S)):
         return S[0] 

def Tail(S):
    if not(IsEmptyLoL(S)):
        return S[1:]
    
def IsList(S):
    return not(IsAtom(S))

def JmlList(S):
    if IsEmptyLoL(S):
        return 0
    else:
        return 1 + JmlList(Tail(S))
    
def IsAtom(e):
    if (type(e) != list):
        return True
    else:
        return False

def IsList(E):
    if (type(E)==list):
        return True
    else:
        return False
    
def IsOneElmt(L):
    if not(IsEmptyLoL(L)):
        return JmlList(L) == 1
    
def Max2(a,b):
    if a >= b:
        return a
    else:
        return b

def Max(S):
    if IsOneElmt(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
            return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            return Max2(FirstList(S), Max(Tail(S)))
        else:
            return Max2(Max(FirstList(S)), Max(Tail(S)))

# Aplikasi
L1 = [[10,9,8],[1,11,12]]
L2 = [[99,100],[103,102]]
print(Max(L1))
print(Max(L2))
