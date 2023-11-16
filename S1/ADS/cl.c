#include<stdio.h>
#include<stdlib.h>
struct node
{
int data;
struct node*next;
};
struct node*strat;
void push()
{
int x;
struct node*ptr;
ptr=malloc(sizeof(struct node();
if(ptr==NULL)
{
printf("\n can't push the element: ");
}
else
{
printf("\n enter the value: ");
sacnf("%d",&x);
if(start==NULL)
{
ptr->data=x;
ptr->next=NULL;
start=ptr;
}
else
{
ptr->data=x;
ptr->next=start;
start=ptr;
}
}
}
void pop()
{
int x;
struct node*ptr;
if
