/*Nama File 	: jarakGLBB.c*/
/*Deskripsi 	: Menghitung Jarak GLBB*/
/*Pembuat   	: [Erlan Irhab Ghalib - 24060121140166]*/
/*Tgl Pembuatan	: [Senin, 28 02 2022 19:31 WIB*/

#include <stdio.h>

int main(){

    //kamus
    float v0,t,a,s;

    //algortima
    printf("Program Jarak GLBB\n");
    printf("Masukkan nilai v0 = ");
    scanf("%f", &v0);
    printf("Masukkan nilai t = ");
    scanf("%f", &t);
    printf("Masukkan nilai a = ");
    scanf("%f", &a);

    s = v0 * t + (a * t * t/2);

    printf("Maka Jarak GLBB adalah %.2f",s);

    return 0;
}
