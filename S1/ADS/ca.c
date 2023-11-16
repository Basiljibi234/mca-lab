#include<stdio.h>
int main()
{
int a[10],b[10],n,i;
printf("enter number of elements in array");
scanf("%d",&n);
printf("enter elements in first array");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("enter elements in second array");
for(i=0;i<n;i++)
{
scanf("%d",&b[i]);
}
printf("the combined array is :");
for(i=0;i<n;i++)
{ 
printf("%d,%d,",a[i],b[i]);
}
}

