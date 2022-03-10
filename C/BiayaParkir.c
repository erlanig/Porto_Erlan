/*Nama File 	: BiayaParkir.c*/
/*Deskripsi 	: Menampilkan dan menentukan besarnya biaya parkir yang dihitung berdasarkan lamanya parkir (bilangan integer > 0 yang dimasukan melalui keyboard, pada layar*/
/*Pembuat   	: Erlan Irhab Ghalib - 24060121140166*/
/*Tgl Pembuatan	: Kamis, 10 03 2022 14:34 WIB*/


#include <stdio.h>

int main()
{

    //Kamus
    int lamaParkir, biaya;

    //Algoritma
    printf("Program Hitung Biaya Parkir\n");
    printf("Masukan jam lama parkir : ");
    scanf("%d", &lamaParkir);
    if (lamaParkir > 0 && lamaParkir <= 2){
        printf ("%d", 2000);
    }
    else{
        biaya = 2000 + (lamaParkir - 2) * 500;
        printf ("%d",biaya);
    }
    return 0;
}
