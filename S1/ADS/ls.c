#include<stdio.h>
void main()
{
int n,i,a[10],lar=0,small=0;
printf("enter the number of elements : ");
scanf("%d",&n);
printf("enter the elements one by one :\n ");
for(i=1;i<=n;i++)
{
scanf("%d",&a[i]);
}
small=a[1];
for(i=1;i<=n;i++)
 {
  if(lar<a[i])
   {
    lar=a[i];
   }
  if(small>a[i])
   {
   small=a[i];
   }
 }
printf("\nlargest element is = %d",lar);
printf("\nsamllest element is = %d \n",small);
}


