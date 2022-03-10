/*Nama File 	: volBolaKerct.c*/
/*Deskripsi 	: Menghitung Volume Bola dan Volume Kerucut*/
/*Pembuat   	: [Erlan Irhab Ghalib - 24060121140166]*/
/*Tgl Pembuatan	: [Senin, 5 03 2022 20.01 WIB*/

#include <stdio.h>

int main(){

    //kamus
    float r,Vb,Vk;
    const float Phi = 3.1415;

    //algortima
    printf("Program Volume Bola dan Volume Kerucut\n");
    printf("Masukkan nilai r = ");
    scanf("%f", &r);

    Vb = 4/3 * Phi * r * r * r;

    printf("Maka volume bola adalah %.2f\n",Vb);

    Vk = Vb/2;
    printf("Maka volume kerucut adalah %.2f",Vk);

    return 0;
}
