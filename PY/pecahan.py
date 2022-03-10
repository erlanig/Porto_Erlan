# Nama file: pecahan.PY
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 25 September 2021
# Deskripsi: Membuat tipe bentukan pecahan beserta dengan konstruktor dan selektornya

# Definisi dan Spesifikasi Tipe
# type pecahan: <n: integer, d: integer>
# {<n:integer>= 0, d: integer>0>n adalah pembilang(numerator) dan d adalah penyebut(denumerator). Penyebut sebuah pecahan tidak boleh nol} 

# Definisi dan Spesifikasi Konstuktor
# MakeP : integer>=0, integer>0 --> pecahan
#   {MakeP(x, y) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x dan y adalah integer}

# Realisasi
def MakeP(P1, P2):
    return (P1, P2)

class Pecahan :
    def __init__(self, n, d):
        self.penyebut = n
        self.pembilang = d

# Definisi dan Spesifikasi Selektor dengan Fungsi
# Pemb : pecahan --> integer>=0
#   {Pemb(p) memberikan numerator pembilang n dari pecahan tersebut}
# Peny : Pecahan --> integer>=0
#   {Pemb(p) memberikan denumerator pembilang n dari pecahan tersebut}

# Realisasi
def Peny(pecahan) :
    return pecahan.penyebut
def Pemb(pecahan):
    return pecahan.pembilang

# DEFINISI dan Spesifikasi Operator Terhadap Pecahan
# {Operator aritmatika pecahan}
# AddP: 2 pecahan --> pecahan
#   {AddP(P1, P2): Menambahkan dua buah pecahan P1 dan P2: n1/d1+n2/d2 = (n1*d2+n2*d1)/d1*d2}
# SubP: 2 pecahan --> pecahan
#   {SubP(P1, P2): Mengurangkan dua buah pecahan P1 dan P2.
#   Mengurangkan dua pecahan: n1/d1 - n2/d2 = (n1*d2 - n2*d1)/d1*d2}
# MulP: 2 pecahan --> pecahan
#   {MulP(P1, P2): Mengalikan dua buah pecahan P1 dan P2
#   Mengalikan dua pecahan: n1/d1*n2/d2 = n1*n2/d1*d2}
# DivP: 2 pecahan --> pecahan
#   {DivP(P1,P2): Membagi dua buah pecahan P1 dan P2
#   Membagi dua pecahan: (n1/d1)/(n2/d2) == n1*d2/d1*d2}
# RealP: pecahan --> real
#   {Menuliskan bilangan pecahan dalam notasi desimal}

# Realisasi
def AddP(P1, P2):
    return ((Peny(P1)*Pemb(P2) + Peny(P2)*Pemb(P1))/(Pemb(P1)*Pemb(P2)))
def SubP(P1, P2):
    return ((Peny(P1)/Pemb(P2) - Peny(P2)*Pemb(P1))/Pemb(P1)*Pemb(P2))
def MulP(P1, P2):
    return (Peny(P1)*Peny(P2))/(Pemb(P1)*Pemb(P2))
def DivP(P1, P2):
    return (Pemb(P1) * Peny(P2))/(Peny(P1)*Pemb(P2))
def RealP(P):
    return (Pemb(P)/Peny(P))

# Definisi dan Spesifikasi Predikat
# IsEqP?: 2 pecahan --> boolean
#   {IsEqP?(p1, p2) true jika p1 = p2
#   Membandingkan apakah dua buah pecahan sama nilainyaL n1/d1 = n2/d2 jika dan hanya jika n1d2 = n2d1}
# IsLtP?: 2 pecahan --> boolean
#   {IsLtP?(p1, p2) true jika p1 < p2
#   Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 < n2/d2 jika dan hanya jika n1d2 < n2d1}
# IsGtP?: 2 pecahan --> boolean
#   {IsGtP?(p1,p2) true jika p1 > p2
#   Membandingkan nilai dua puluh, apakah p1 lebih besar nilainya dari p2: n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1}

# Realisasi
def IsEqP (P1, P2):
    return Pemb(P1)*Peny(P2) == Peny(P1)*Pemb(P2)
def IsLtP (P1, P2):
    return Pemb(P1)*Peny(P2) < Peny(P1)*Pemb(P2)
def IsGtP (P1, P2):
    return Pemb(P1)*Peny(P2) > Peny(P1)*Pemb(P2)

# Aplikasi
P1 = Pecahan(3, 3)
P2 = Pecahan(4, 4)
P = Pecahan (5,5)

print(MakeP(P1, P2))
print(AddP(P1, P2))
print(SubP(P1, P2))
print(MulP(P1, P2))
print(DivP(P1, P2))
print(RealP(P))
print(IsEqP(P1, P2))
print(IsLtP(P1, P2))
print(IsGtP(P1, P2))