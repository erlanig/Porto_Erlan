# Nama file: Contoh 1.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  8 November 2021
# Deskripsi: Mencek kesamaan dua buah list of list

# Definisi dan Spesifikasi
# IsEqS : 2 List of list --> boolean
# IsEqS(S1,S2) true jika S1 identik dengan S2 : semua elemennya sama

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
    
def IsEqS(S1,S2):
    if IsEmptyLoL(S1) and IsEmptyLoL(S2):
        return True
    elif (not IsEmptyLoL(S1)) and IsEmptyLoL(S2):
        return False
    elif IsEmptyLoL(S1) and (not IsEmptyLoL(S2)):
        return False
    elif (not IsEmptyLoL(S1)) and (not IsEmptyLoL(S2)):
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            return FirstList(S1) ==  FirstList(S2) and IsEqS(Tail(S1), Tail(S2)) 
        elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(Tail(S1), Tail(S2))
        else:
            return False
        
# Aplikasi
L1 = ["IF",[8,11,2021]]
L2 = ["IF",[8,11,2021]]
L3 = [[10,11,12],2021]
L4 = [[11,11,11],2021]
print(IsEqS(L1,L2))
print(IsEqS(L3,L4))
