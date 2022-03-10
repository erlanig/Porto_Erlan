# Nama file: konversi_derajat.py
# Pembuat: Erlan Irhab Ghalib
# Tanggal: 19 September 2021
# Deskripsi : mengkonversi nilai suhu dalam celcius menjadi reamur, farenheit, '
# dan kelvin sesuai dengan kode konversi

# Definisi dan Spesifikasi:
# konversi_derajat : integer, string --> real
#   {konversi_derajat(a,b) mengubah nilai celcius menjadi nilai derajat sesuai kode konversi b}

# Realisasi
def konversi_derajat (a,b) :
    if b == "reamur" :
        return 4*a/5
    elif b == "farenheit" :
        return (9*a/5)+32
    elif b == "kelvin" :
        return a + 273
    else : 
        return "Tidak Valid"

# Aplikasi
print(konversi_derajat(22,"reamur"))
print(konversi_derajat(22,"farenheit"))
print(konversi_derajat(22,"kelvin"))