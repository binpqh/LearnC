#include<stdio.h>
void main()
{
    int n;
    int i = 0;
    printf("Vui Long Nhap So Nguyen\n");
    scanf("%d",&n);
    while (n >= 1) 
    {
        n /= 10;
        i++;
    }
    printf("Ket Qua So Nguyen %d",i);
}
