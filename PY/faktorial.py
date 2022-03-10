# Nama file: faktorial.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal:  19 Oktober 2021
# Deskripsi: Menghitung faktorial dari n 

# Definisi dan Spesifikasi
# faktorial(n) : integer >= 0 --> integer > 0
# {faktorial(n) = n sesuai dengan rekrusif faktorial}

# Realisasi
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n*faktorial(n-1)

def permutasi(n, k):
    return faktorial(n)/faktorial(n-k)

def kombinasi(n, k):
    return faktorial(n)/(faktorial(n-k)*faktorial(k))

# Aplikasi
print(faktorial(4))
print(permutasi(4,2))
print(kombinasi(4,2))
