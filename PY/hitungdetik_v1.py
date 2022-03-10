# Nama file: hitungdetik_v1.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 10 September 2021
# Deskripsi : menghitung berapa jumlah detik dari format jam,menit,dan detik yang diberikan

# Definisi dan spesifikasi:
# hitung_detik = 3 integer>= 0 --> integer
#   {hitung_detik(j,m,s) menghitung jumlah detik dengan j sebagai jam dengan ketentuan jam <24, m sebagai menit<60
#   dan s sebagai sekon <60}

# Realisasi
def hitung_detik (j, m, s) :
    return (j*3600 + m*60 + s)

# Aplikasi
print(hitung_detik(1, 1, 1))
