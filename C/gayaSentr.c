/*Nama File 	: gayaSentr.c*/
/*Deskripsi 	: Menghitung Gaya Sentripetal*/
/*Pembuat   	: [Erlan Irhab Ghalib - 24060121140166]*/
/*Tgl Pembuatan	: [Senin, 5 03 2022 19:41 WIB*/

#include <stdio.h>

int main(){

    //kamus
    float m,v,r,F;

    //algortima
    printf("Program Gaya Sentripetal\n");
    printf("Masukkan nilai m = ");
    scanf("%f", &m);
    printf("Masukkan nilai v = ");
    scanf("%f", &v);
    printf("Masukkan nilai r = ");
    scanf("%f", &r);

    F = m * ((v*v)/r);

    printf("Maka Gaya Sentripetal adalah %.2f",F);

    return 0;
}
