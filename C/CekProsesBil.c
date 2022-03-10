/*Nama File 	: CekProsesBil.c*/
/*Deskripsi 	: Menghitung Luas dan Keliling Layang-layang*/
/*Pembuat   	: [Erlan Irhab Ghalib - 24060121140166]*/
/*Tgl Pembuatan	: [Senin, 7 03 2022 19:08 WIB*/

#include <stdio.h>

int main(){

    //kamus
    int N;

    //algoritma
    printf("Program mengecek dan memproses bilangan \n");
    printf("Masukkan nilai N = ");
    scanf("%d", &N);
    if (N % 2 == 0){
        N = N + 3;
        if (N % 5 == 0){
            N = N + 5;
            printf("Hasilnya adalah %d", N);
        }
        else{
            N = N + 2;
            printf("Hasilnya adalah %d", N);
        }
    }
    else{
        N = N + 3;
        if (N & 3 == 0){
            N = N + 4;
            printf("Hasilnya adalah %d", N);
        }
        else{
            N = N + 1;
            printf("Hasilnya adalah %d", N);
        }

    }
    return 0;
}
