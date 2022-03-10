# Nama file: NextNSecond.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 8 Oktober 2021
# Deskripsi: membuat tipe bentukan time beserta konstruktor dan selektornya

# Definisi dan Spesifikasi

# Konstruktor
def Time(j,m,s):
    return[j,m,s]

# Selektor
def Jam(T):
    return T[0]
def Menit(T):   
    return T[1]
def Detik(T):
    return T[2]

# Operator
def NextSecond(T):
    if Detik(T) == 59:
        if Menit(T) == 59:
            if Jam(T) == 23:
                return Time(0,0,0)
            else:
                return Time(Jam(T)+1,0,0)
        else:
            return Time(Jam(T),Menit(T)+1,0)
    else:
        return Time(Jam(T),Menit(T),Detik(T)+1)

def NextNSecond(T,n):
    if n == 1:
        return NextSecond(T)
    else:
        return NextNSecond(NextSecond(T),n-1)

# Aplikasi
print(NextNSecond(Time(23,59,59),2))
print(NextNSecond(Time(23,59,59),1))