def IsEmptyLoL(S):
    return S == []

def FirstList(S):
    if not(IsEmptyLoL(S)):
         return S[0] 
     
def Tail(S):
    if not(IsEmptyLoL(S)):
        return S[1:]

def JmlElmt(S):
    if not(IsEmptyLoL(S)):
        return 0
    else:
        return 1 + JmlElmt(Tail(S))

def IsAtom(e):
    if (type(e) == int):
        return True
    else:
        return False
    
L1 = [1,2,3]
print(IsAtom(FirstList(L1)))