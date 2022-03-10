def IsEmpty(L):
    return L == []
def FirstElmt(T):
    if not IsEmpty(T):
        return T[0]
    else:
        return []
def LastElmt(L):
    if not IsEmpty(L):
        return L[-1]
    else:
        return []
def Head(L):
    if not IsEmpty(L):
        return L[:-1]
    else:
        return []
def Tail(T):
    if not IsEmpty(T):
        return T[1:]
    else:
        return []
def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))
E = 1
L1 = [1,2,3]
print(IsMember(E,L1))

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
def Konso(x, l):
	return [x] + l
def Kons(l, x):
	return l + [x]
def Konsa(x, y, l):
	return [y] + [x] + l
def OneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return 
def Rember(x, l):
    if IsEmpty(l):
        return []
    elif FirstElmt(l)==x:
        return Tail(l)
    else:
        return Konso(FirstElmt(l), Rember(x, Tail(l)))
def ApakahPrima(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    else:
        return True

#------------------------------------
def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))

vokal = ['a', 'i', 'u', 'e', 'o']

def NbVokal(L):
    if IsEmpty(L):
        return 0
    else:
        if IsMember(FirstElmt(L),vokal):
            return 1 + NbVokal(Tail(L))
        else:
            return NbVokal(Tail(L))

L1 = ['a','b','c','d','e']
'''
a',['b','c','d','e']([a,i,u,e,u,o])
return:
1 + ['b','c','d','e']([a,i,u,e,u,o])

'b',[c,d,e,]([a,i,u,e,o])
'''

print(NbVokal(L1))