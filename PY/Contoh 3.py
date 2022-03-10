# Nama file: Contoh 3.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  9 November 2021
# Deskripsi: Mencek apakah sebuah List merupakan elemen dari sebuah list yang elemennya list

# Definisi dan Spesifikasi
# IsMemberLS : List, List of list --> boolean
# IsMemberLS(L,S) true jika L adalah anggota S

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
    elif (not IsEmptyLoL(S1)) and (not IsEmptyLoL(S1)):
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            return FirstList(S1) ==  FirstList(S1) and IsEqS(Tail(S1), Tail(S2)) 
        elif IsList(FirstList(S1)) and IsList(FirstList(S1)):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(Tail(S1), Tail(S2))
        else:
            return False

def IsMemberLS(L, S):
        if IsEmptyLoL(L) and IsEmptyLoL(S):
            return True
        elif (not IsEmptyLoL(L)) and IsEmptyLoL(S):
            return False
        elif IsEmptyLoL(L) and (not IsEmptyLoL(S)):
            return False
        elif (not IsEmptyLoL(L)) and (not IsEmptyLoL(S)):
            if IsAtom(FirstList(S)): 
                return IsMemberLS(L, Tail(S))
            else:
                if IsEqS(L, FirstList(S)):
                    return True
                else:
                    return IsMemberLS(L, Tail(S))

# Aplikasi                
L1 = [3,2,1]
S1 = [[3,2,1],["Mulai"]]
L2 = [99]
S2 = [[88,8],[1,2,3]]
print(IsMemberLS(L1,S1))
print(IsMemberLS(L2,S2))
