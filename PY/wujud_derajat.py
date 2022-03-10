# Nama file: wujud_derajat.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 18 September 2021
# Deskripsi : memberi tahu wujud dari suatu besaran celcius

# Definisi dan Spesifikasi:
# wujud_derajat : integer --> string
#   {wujud_derajat(a) memberi tahu wujud dari benda yang memiliki suhu dalam besaran celcius}

# Realisasi
def wujud_derajat(a) :
    if a > 0 :
        if a < 100 :
            return "Cair"
        else :
            return "Gas"
    else :
        return "Padat"
        
# Aplikasi
print(wujud_derajat(-10))
print(wujud_derajat(10)) 
print(wujud_derajat(0))