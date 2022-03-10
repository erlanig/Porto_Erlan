/*Nama File 	: kalSS.c*/
/*Deskripsi 	: Menampilkan dan menghitung beberapa hasil operasi aritmatika kedua bilangan tersebut berdasarkan pilihan operasi menggunakan character yang diinput menggonakan keyboard, pada layar*/
/*Pembuat   	: Erlan Irhab Ghalib - 24060121140166*/
/*Tgl Pembuatan	: Selasa, 8 03 2022 21:12 WIB*/

#include <stdio.h>

int main()
{

    //Kamus
    int s1,s2,s3;

    //Algoritma
    printf("Masukan sisi 1 : ");
    scanf("%d", &s1);
    printf("Masukan sisi 2 : ");
    scanf("%d", &s2);
    printf("Masukan sisi 3 : ");
    scanf("%d", &s3);

    switch(s1,s2,s3)
    {
    case s1 == s2 == s3:
        printf("Segitiga Sama Sisi");
        break;
    case 'b':
        i = iA - iB;
        printf("%f",i);
        break;
    case 'c':
        i = iA * iB;
        printf("%f",i);
        break;
    case 'd':
        i = iA / iB;
        printf("%f",i);
        break;
    case 'e':
        i = iA / iB;
        printf("%d",i);
        break;
    case 'f':
        i = iA % iB;
        printf("%f",i);
        break;
    default:
        printf("Bukan pilihan menu yang benar");
    }
    return 0;

}
