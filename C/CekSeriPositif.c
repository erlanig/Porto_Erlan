/*Nama File 	: CekSeriPositif.c*/
/*Deskripsi 	: Menampilkan nilai kebenaran tahanan apakah masukkan tersebut bernilai negative atau tidak, jika bernilai positif maka akan mengeluarkan hasil total penjumlahan ketiga tahanan pada layar*/
/*Pembuat   	: Erlan Irhab Ghalib - 24060121140166*/
/*Tgl Pembuatan	: Selasa, 8 03 2022 16:32 WIB*/

#include <stdio.h>

int main()
{

    //Kamus
    float t1,t2,t3,total;

    //Algoritma
     printf("Program untuk cek seri positif\n");
    printf("Masukan sebuah bilangan : ");
    scanf("%f", &t1);
    printf("Masukan sebuah bilangan : ");
    scanf("%f", &t2);
    printf("Masukan sebuah bilangan : ");
    scanf("%f", &t3);
    if (t1 >= 0 && t2 >= 0 && t3 >= 0){
            total = t1 + t2 + t3;
            printf("Maka total tahanan jika dirangkai seri adalah %.2f\n",total);
    }
    else{
        printf("Masukan tahanan tidak boleh negatif");
    }


}
