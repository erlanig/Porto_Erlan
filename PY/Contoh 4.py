# Nama file: Contoh 4.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  9 November 2021
# Deskripsi: Menghapus sebuah elemen(atom) dari list of list

# Definisi dan Spesifikasi
# Rember : elemen, List of list --> List of list
# Rember(a,S) menghapus sebuah elemen bernilai a dari semua list S

# Realisasi
def IsEmptyLoL(S):
    return S == [] 

def FirstElement(S):
    if not(IsEmptyLoL(S)):
         return S[0]

def Tail(S):
    if not(IsEmptyLoL(S)):
        return S[1:]
    
def IsList(E):
    if (type(E)==list):
        return True
    else:
        return False

def KonsLo(L,S):
    if IsEmptyLoL(S):
        return [L]
    else:
        return [L] + S
    
print(KonsLo(2,[3]))
        
def KonsLi(L,S):
    if IsEmptyLoL(S):
        return [L]
    else:
        return S + [L]
print(KonsLi(2,[3]))    
    
def Rember(a, S):
    if IsEmptyLoL(S):
        return S
    else:
        if IsList(FirstElement(S)):
            return KonsLo(Rember(a,FirstElement(S)), Rember(a, Tail(S)))
        else:
            if FirstElement(S) == a:
                return Rember(a, Tail(S))
            else:
                return KonsLo(FirstElement(S), Rember(a, Tail(S)))
# Aplikasi                    
E1 = 1
L1 = [[1,2],[3,4,5]]
E2 = "IF"
L2 = [10,2,4,["IF",20]]
print(Rember(E1,L1))
print(Rember(E2,L2))
        
    
