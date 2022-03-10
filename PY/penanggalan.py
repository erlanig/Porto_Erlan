# Nama file: penanggalan.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 19 September 2021
# Deskripsi : menghitung jumlah hari dari tanggal yang diberikan

# Definisi dan Spesifikasi:
## penanggalan : 0<integer<32 , 0<integer<13 --> 0<integer<367
#   {jumlah_hari(d,m} dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari 1900 +y. 1 Januari tahun 1900+y adalah hari ke 1}
# dpm : 0< integer <13 --> integer
#   {dpm(b) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. terhitung mulai satu
# januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan b, tanpa memperhhitungkan tahun kabisat}


# Realisasi
def dpm (b) :
    if b == 1 :
        return 1
    elif b == 2 :
        return 32
    elif b == 3 :
        return 60
    elif b == 4 :
        return 91
    elif b == 5 :
        return 121
    elif b == 6 :
        return 152
    elif b == 7 :
        return 182
    elif b == 8 :
        return 213
    elif b == 9 :
        return 244
    elif b == 10 :
        return 274
    elif b == 11 :
        return 305
    elif b == 12 :
        return 335
    else :
        return "Tanggal Tidak Valid"

def penanggalan(d,m) :
    return dpm(m) + d - 1

# Aplikasi
print(penanggalan(1,1))
print(penanggalan(30,2))
print(penanggalan(22,10))