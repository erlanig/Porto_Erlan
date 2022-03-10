# Nama file: HargaBesih.py
# Pembuat: Erlan Irhab Ghalib 
# Tanggal: 8 Oktober 2021
# Deskripsi: menentukan diskon sebuah produk berdasarkan harga produk dan kategori pelanggan(Premium, Gold, dan Silver) dan outputnya yaitu harga bersih produk setelah dipotong diskon

# Realisasi
def Harga(h):
    if h>1000000:
        return h-(h*0.3)
    elif 750000<h<1000000:
        return h-(h*0.2)
    elif 500000<h<7500000:
        return h-(h*0.1)
    else:
        return h-(h*0.05)

def Kategori(k):
    if k == "Premium":
        return 0.05
    elif k == "Gold":
        return 0.025
    elif k == "Silver":
        return 0

def HargaBersih(h,k):
    return Harga(h) - (Harga(h)*Kategori(k))

# Aplikasi
print(HargaBersih(2000000,"Premium"))
print(HargaBersih(2000000, "Gold"))
print(HargaBersih(2000000, "Silver"))
print(HargaBersih(800000,"Premium"))
print(HargaBersih(800000, "Gold"))
print(HargaBersih(800000, "Silver"))
print(HargaBersih(600000,"Premium"))
print(HargaBersih(600000, "Gold"))
print(HargaBersih(600000, "Silver"))
print(HargaBersih(400000,"Premium"))
print(HargaBersih(400000, "Gold"))
print(HargaBersih(400000, "Silver"))