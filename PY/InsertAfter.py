def InsertAfter(L,x,e):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L)== e:
            return Konsa(x,FirstElmt(L),InsertAfter(Tail(L),x,e))
        else:
            return Konso(FirstElmt(L),InsertAfter(Tail(L),x,e))
            '''
            Konso(1,InserAfter([2,3],4,3))
            Konso(1(Konso(2,InsertaAfter([3],4,3)))
            konso(1(Konso(2(Konsa(4,3,InsertAfter([],4,3))))))
            [1,2,3,4]
            '''

# Aplikasi
L1 = [1,2,3]
L2 = [2,3,4,6]
print(InsertAfter(L1,4,3))
print(InsertAfter(L2,5,4))