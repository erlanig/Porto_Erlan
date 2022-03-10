# Nama file: MakeUnion.py
# Pembuat: Erlan Irhab Ghalib - 24060121140166
# Tanggal:  1 November 2021
# Deskripsi: Menggunakan fungsi-fungsi yang berhubungan dengan set

# Definisi dan Spesifikasi
# MakeUnion : 2 set --> set
# MakeUnion(H1,H2) membuat union H1 dan H2 : yaitu set baru dengan 
# semua anggota elemen H1 dan anggota H2

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

def MakeUnion(H1,H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif (not IsEmpty(H1)) and IsEmpty(H2):
        return H1
    elif IsEmpty(H1) and (not IsEmpty(H2)):
        return H2
    elif (not IsEmpty(H1)) and (not IsEmpty(H2)):
        if IsMember(FirstElmt(H1),H2):
            return MakeUnion(Tail(H1),H2)
        else:
            return Konso(FirstElmt(H1),MakeUnion(Tail(H1),H2))

# Aplikasi
M = [1,2,3,4]
N = [5,6,7,8]
O = ["Informatika", "Undip"]
P = [1, "November", 2021]
print(MakeUnion(M,N))
print(MakeUnion(O,P))
