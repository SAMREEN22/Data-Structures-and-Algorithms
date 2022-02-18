#include<stdio.h>
int main()
{
    int n,i,num;
    printf("Enter Size of Array:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter elements of Array:");
    for(i=0;i<n;i++)
    {
         scanf("%d",&arr[i]);
    }
    printf("Enter element for searching:");
    scanf("%d",&num);
    for (i=0;i<n;i++)
    {
         if(arr[i]==num)
        {
             printf("Element found at Index: %d",i);
             printf("\nElement found at Position: %d",i+1);
            break;
        }
    }
    if(i==n)
     printf("Element not found");
return 0;
}

//starting at the beginning of the data set, each item of data is examined until a match is made. Once the item is found, the search ends.