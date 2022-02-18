#include <stdio.h>
int main()
{
int i, low, high, mid, n, key, array[100];
printf("Enter the size of array ");
scanf("%d",&n);
printf("Enter %d integers ", n);
for(i=0;i<n;i++)
scanf("%d",&array[i]);
printf("Enter element to be found ");
scanf("%d", &key);
low = 0;
high = n-1;
mid = (low+high)/2;
while (low <= high) {
if(array[mid] < key)
low = mid+1;
else if (array[mid] == key) {
printf("%d found at location %d", key, mid+1);
break;
}
else
high = mid-1;
mid = (low+high)/2;
}
if(low > high)
printf("Not found! %d isn't present in the list", key);
return 0;
}

//used in a sorted array by repeatedly dividing the search interval in half
//the idea of binary search is to use the information that the array is sorted and reduce the time complexity