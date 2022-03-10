# Def Spek
# type PohonBiner: <A: elemen, L: PohonBiner, R: PohonBiner>
# <A,L,R> adalah type bentukan pohon biner dimana A adalah root, L adalah daun kiri, dan R adalah daun kanan
class PohonBiner:
    def __init__(self, A, L, R):
        self.A = A
        self.L = L
        self.R = R
        
#Def Spek 
#MakPB: 3 integer --> PohonBiner
#MakePb(A,L,R) Menghasilkan sebuah pohon biner dengan A adalah root, L adalah daun kiri, dan R adalah daun kanan
def MakePB(A, L, R):
    return PohonBiner(A,L,R)        

# Fungsi root
# Def Spek
# root(P) pohon biner tak kosong --> pohon biner
def root(P):
    return P.A
        
# Fungsi Left
# Defspek
# Left: pohon biner tak kosong -->pohon biner
# Left (P) adalah sub pohon kiri dari P jika /L, A, R\ maka left (P) adalah L       
def Left(P):
    return P.L

# Fungsi right 
# defspek
# Right: pohon biner tak kosong --> pohon biner
# Right(P) adalah sub pohon dari P jika /L, A, R\ maka right (P) adalah R
def Right(P):
    return P.R    

# Fungsi IsTreeEmpty
# Defspek
# IsTreeEmpty : pohon biner --> boolean
# IsTreeEmpty (P) bernilai benar jika P kosong
def IsTreeEmpty(P):
    if P == None :
        return True
    else:
        return False

# Fungsi IsBiner
# Defspek
# IsBiner : PohonBiner tidak kosong → boolean
# IsBiner(P) true jika P mengandung sub pohon kiri dan sub pohon kanan : (//L A R\\)
def IsBiner(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False
    
# Fungsi IsOneElmtPB
# Defspek
# IsOneElmtPB: pohon biner --> boolean
# IsOneElmtPB (P) bernilai benar jika P hanya mempunyai satu elemen yaitu /A
def IsOneElmtPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
        return True
    else:
        return False

# Fungsi IsUnerLeftPB
# Defspek
# IsUnerLeftPB : pohon biner --> boolean
# IsUnerLeftPB (P) bernilai benar jika p mengandung sub pohon kiri
def IsUnerLeftPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False
    
# Fungsi IsUnerRightPB
# Defspek
# IsUnerRightPB : pohon biner --> boolean
# IsUnerRightPB (P) bernilai benar jika P mengandung sub pohon kanan
def IsUnerRightPB(P):
    if (not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
        return True
    else:
        return False
    
# Fungsi AddX
# Defspek
# AddX: BinSearchTree, elemen → PohonBiner
# AddX(P,X) Menghasilkan sebuah pohon Binary Search Tree P dengan tambahan simpul
# X. Belum ada simpul P yang bernilai X 
def AddX(P,X):
    if IsTreeEmpty(P):
        return MakePB(X, None, None)
    else:
        if root(P) > X:
            return MakePB(root(P), AddX(Left(P), X), Right(X))
        else:
            return MakePB(root(P), Left(P), AddX(Right(P), X))
        
        '''
        ((2,none,none),3)
        MakePB()
        
        '''
    
def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmtPB(P):
        return 1
    else:
        if IsBiner(P):
            return NbElmt(Left(P)) + 1 + NbElmt(Right(P))
        elif IsUnerLeftPB(P):
            return NbElmt(Left(P)) + 1
        elif IsUnerRightPB(P):
            return NbElmt(Right(P)) + 1
        else:
            return 0
        
def NbElement(P):
    if IsTreeEmpty(P):
        return 0
    else:
        NbElement(Left(P)) + 1 + NbElement(Right(P))

def NbDaun(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmtPB(P):
        return 1
    else:
        if IsBiner(P):
            return NbDaun(Left(P)) + NbDaun(Right(P))
        elif IsUnerLeftPB(P):
            return NbDaun(Left(P))
        elif IsUnerRightPB(P):
            return NbDaun(Right(P))
        
       
        
        
        
'''   4
2     6'''

P3 = MakePB(1,MakePB(4,MakePB(3,None,None),None), MakePB(2,MakePB(9,None,None),None))
P5 = MakePB(11,MakePB(9,MakePB(8,MakePB(7,None,None),None),None), MakePB(6,MakePB(3,MakePB(10,None,None),None),None))
P4 = MakePB(4,MakePB(2,None,None),MakePB(6,None,None))
P6 = MakePB(3,None,None)

'''
(4,(2,None,None)(None,)
(1,4(3,None,None),2(9,None,None))

'''
print(root(P3))
print(root(P5))
print(Left(P4))
print(Right(P4))
print(IsTreeEmpty(P4))
print(root(P5))
print(IsOneElmtPB(P6))