#include<stdio.h>
#include<stdlib.h>
#define n 5
int main(){
    int queue[n],ch,front=0,rear=0,x=n,i;
      printf("\n1:inserstion\n2:deletion\n3:Display\n4:Exit\n");
      while(1)
     {
         printf("enter your choice");
         scanf("%d",&ch);
      switch(ch){
             case 1:
                     if(rear==x){
                       printf("queue Overflow");
                     }else{
                          printf("Enter the Element\n");
                          scanf("%d",&queue[rear++]);
                          
                     }
                     break;
                     
            case 2:
                    if(front==rear){
                      printf("empty");
                    }else{
                      printf("\n deleted element is %d",queue[front++]);
                      x++;
                    }
                    break;
                      
            case 3: //Display
                    printf("\n queue is ");
                    if(front==rear){
                      printf("empty");
                    }else{
                    for(i=front;i<rear;i++){
                        printf("%d\n",queue[i]);
                        printf("\n");
                    }
                    break;
                    }
           case 4: //Exit
                   exit(0);
           default: printf("Invalid Number");
                    break;
     }
   }
   return 0;
}
