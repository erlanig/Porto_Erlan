/*Nama File 	: BiayaParkir.c*/
/*Deskripsi 	: Menampilkan dan menghitung besarnya harga setelah diberikan diskon pada layar*/
/*Pembuat   	: Erlan Irhab Ghalib - 24060121140166*/
/*Tgl Pembuatan	: Kamis, 10 03 2022 21:09 WIB*/

#include <stdio.h>

int main()
{

    //Kamus
    char j;
    int h,t;

    //Algoritma
    printf("Program Menghtiung Harga Diskon\n");
    printf("Masukan inputan 'A' atau 'B' atau 'C': ");
    scanf("%c", &j);
    printf("Masukan harga: ");
    scanf("%d", &h);

    switch(j){

    case 'A':
        t = h - (h * 0.10);
        printf("%d", t);
        break;
    case 'B':
        t = h - (h * 0.15);
        printf("%d", t);
        break;
    case 'C':
        t = h - (h * 0.2);
        printf("%d", t);
        break;
    }
    return 0;

}
