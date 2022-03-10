/*Nama File 	: CekHari.c*/
/*Deskripsi 	: Menampilkan nama-nama hari dari nomor hari, yaitu 1 s.d 7 yang dibaca dari masukan keyboard pada layar*/
/*Pembuat   	: Erlan Irhab Ghalib - 24060121140166*/
/*Tgl Pembuatan	: Selasa, 8 03 2022 14:52 WIB*/

#include <stdio.h>

int main()
{

    //Kamus
    int h;

    //Algoritma
    printf("Program untuk cek hari menggunakan inputan integer\n");
    printf("Masukan sebuah bilangan : ");
    scanf("%d", &h);

    switch(h)
    {
    case 1:
        printf("Hari Senin");
        break;
    case 2:
        printf("Hari Selasa");
        break;
    case 3:
        printf("Hari Rabu");
        break;
    case 4:
        printf("Hari Kamis");
        break;
    case 5:
        printf("Hari Jumat");
        break;
    case 6:
        printf("Hari Sabtu");
        break;
    case 7:
        printf("Hari Minggu");
        break;
    default:
        printf("Masukan nomor hari tidak tepat");
    }
    return 0;

}
