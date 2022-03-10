# Nama file: hitungdetik_am.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 10 September 2021
# Deskripsi : menghitung berapa jumlah detik dari jam,menit,detik dengan format am/pm yang diberikan

# Definisi dan Spesifikasi:
# hitungdetik_am : 3 integer>=0 , string --> integer
#   {hitungdetik_am(j,m,s,k) menghitung jumlah detik dengan j sebagai jam <12, m sebagai menit<60, s sebagai second<60
#   dan k sebagai keterangan am/pm, semisal pm maka j = j +12 jika am j = j}

# Realisasi
def hitungdetik_am (j, m, s, k) :
    if k == "am" :
        return(j*3600 + m*60 + s)

    else :
        return((j+12)*3600 + m*60 + s)

# Aplikasi
print(hitungdetik_am(2, 5, 45, "am"))
print(hitungdetik_am(1, 1, 1, "pm"))