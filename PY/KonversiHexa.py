# Nama file: KonversiHexa.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 9 Oktober 2021
# Deskripsi: mengkonversi bilang desimal menjadi hexadesimal

# Realisasi
def IntToChar(x):
    return str(x)
def KonkatStr(s,c):
    return s + c

def KonversiHexa(n, b):
    IntToChar = "0123456789ABCDEF"
    if n<16:
        return IntToChar[n]
    else:
        return KonversiHexa((n//b), b) + IntToChar[n % b]

# Aplikasi
print(KonversiHexa(11600, 16))
