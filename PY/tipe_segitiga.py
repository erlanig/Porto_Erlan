# Nama file: tipe_egitiga.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 19 September 2021
# Deskripsi : memberi informasi tipe segitiga dari inputan 3 buah integer

# Definisi dan Spesifikasi:
# tipe_segitiga : 3 integer >0 --> string
#   {tipe_segitiga(a,b,c) menentukan tipe segitiga dari 3 inputan integer sebagai sisi segitiga}

# Realisasi
def tipe_segitiga(a,b,c):
    if a == b == c:
        return "Segitiga sama sisi"
    elif a == b or b == c or a == c :
        return "Segitiga sama kaki"
    else :
        return "Segitiga sembarang"
    
# Aplikasi    
print(tipe_segitiga(4,5,6))