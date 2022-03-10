/*Nama File 	: CekBilSemb.c*/
/*Deskripsi 	: Menampilkan apakah bilangan i adalah bilangan bulat positive atau bulat negative atau bukan sebuah bilangan pada layar*/
/*Pembuat   	: Erlan Irhab Ghalib - 24060121140166*/
/*Tgl Pembuatan	: Selasa, 8 03 2022 21:12 WIB*/

#include <stdio.h>

int main()
{

    //Kamus
    int i;

    //Algoritma
    printf("Masukan sebuah bilangan : ");
    scanf("%d", &i);

    switch(i){

    case i > 0:
        printf("Bilangan tersebut merupakan bilangan positive");
        break;
    case i == 0:
        printf("Bilangan tersebut merupakan bilangan nol");
        break;
    case i < 0:
        printf("Bilangan tersebut merupakan bilangan negative");
        break;
    default:
        printf("Bukan termasuk sebuah bilangan");
    }
    return 0;

}
