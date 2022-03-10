# Nama file: MakeIntersect.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  1 November 2021
# Deskripsi: Menggunakan fungsi-fungsi yang berhubungan dengan set

# Definisi dan Spesifikasi
# MakeIntersect : 2 set --> set
# MakeIntersetct(H1,H2) membuat interaksi H1 dengan H2 : yaitu set baru dengan
# anggota elemen yang menggunakan anggota H1 dan juga anggota H2

# Realisasi
def IsEmpty(L):
    if L == []:
        return True
    else:
        return False

def FirstElmt(L):
    if not(IsEmpty(L)):
        return L[0]
        
def Tail(L):
    if not(IsEmpty(L)):
        return L[1:]

def IsMember(x, L):
    if (IsEmpty(L)):
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            return IsMember(x, Tail(L))

def Konso(E,L):
    if E == []:
        return L
    elif L == []:
        return [E]
    else:
        return [E] + L

def MakeIntersect(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif (not IsEmpty(H1)) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and (not IsEmpty(H2)):
        return []
    elif (not IsEmpty(H1)) and (not IsEmpty(H2)):
        if IsMember(FirstElmt(H1),H2):
            return Konso(FirstElmt(H1),MakeIntersect(Tail(H1),H2))
        else:
            return MakeIntersect(Tail(H1),H2)

# Aplikasi
M = [1,2,3,4]
N = [2,4,6,8]
O = [2,2,2]
P = [1,1,1]
 
print(MakeIntersect(M,N))
print(MakeIntersect(O,P))