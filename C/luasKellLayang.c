/*Nama File 	: luasKellLayang.c*/
/*Deskripsi 	: Menghitung Luas dan Keliling Layang-layang*/
/*Pembuat   	: [Erlan Irhab Ghalib - 24060121140166]*/
/*Tgl Pembuatan	: [Senin, 28 02 2022 19:25 WIB*/

#include <stdio.h>

int main(){

    //kamus
    float s1,s2,d1,d2;
    float luasLayang,kellLayang;

    //algoritma
    printf("Menghitung Luas Layang-layang\n");
    printf("Masukan nilai d1 = ");
    scanf("%f", &d1);
    printf("Masukan nilai d2 = ");
    scanf("%f", &d2);
    printf("Masukan nilai s1 = ");
    scanf("%f", &s1);
    printf("Masukan nilai s2 = ");
    scanf("%f", &s2);
    luasLayang = (d1 * d2)/2;
    kellLayang = 2 * (s1+s2);

    printf("Maka Luas Layang-layang adalah %.2f\n",luasLayang);
    printf("Maka Keliling Layang-layang adalah %.2f",kellLayang);

    return 0;
}
