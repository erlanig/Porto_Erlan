/*Nama File 	: jarakPBola.c*/
/*Deskripsi 	: Menghitung jarak yang di tempuh benda yang mengalami gerak parabola*/
/*Pembuat   	: [Erlan Irhab Ghalib - 24060121140166]*/
/*Tgl Pembuatan	: [Senin, 28 02 2022 19:25 WIB*/

#include <stdio.h>

int main(){

    //kamus
    float v0,t,y;
    const float g = 9.8;
    //algoritma
    printf("Menghitung jarak yang di tempuh benda yang mengalami gerak parabola\n");
    printf("Masukan nilai v0 = ");
    scanf("%f", &v0);
    printf("Masukan nilai t = ");
    scanf("%f", &t);

    y = v0 * t - 1/2 * (g * t * t);

    printf("Maka jarak yang di tempuh benda yang mengalami gerak parabola %.2f", y);

}
