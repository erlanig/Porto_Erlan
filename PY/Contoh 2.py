# Nama file: Contoh 2.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  8 November 2021
# Deskripsi: Mencek apakah sebuah atom merupakan elemen dari sebuah list

# Definisi dan Spesifikasi
# IsMemberS : elemen, List of list --> boolean
# IsMemberS(A,S) true jika A adalah anggota S

# Realisasi
def IsEmptyLoL(S):
    return S == [] 

def FirstList(S):
    if not(IsEmptyLoL(S)):
         return S[0]

def Tail(S):
    if not(IsEmptyLoL(S)):
        return S[1:]
    
def JmlList(S):
    if IsEmptyLoL(S):
        return 0
    else:
        return 1 + JmlList(Tail(S))
    
def KonsLo(L, S):
    if IsEmptyLoL(S):
        return [L]
    else:
        return [L]
    

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

def IsMemberS(A, S):
    if IsEmptyLoL(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if A == FirstList(S):
                return True
            else:
                return IsMemberS(A, Tail(S))
        elif IsList(FirstList(S)):
            if IsMemberS(A, FirstList(S)):
                return True
            else:
                return IsMemberS(A, Tail(S))
            
# Aplikasi
L1 = [55,["Erlan",77,99],'E'] 
L2 = [[1,2],[3,4,5]]                      
print(IsMemberS("Erlan",L1))
print(IsMemberS(6,L2))
