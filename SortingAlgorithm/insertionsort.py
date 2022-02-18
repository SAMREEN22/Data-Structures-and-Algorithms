lst=[]
n= int(input("Enter the number of elements: "))
for i in range(n):
    elem= int(input())
    lst.append(elem)
print("Before sorting array elements are: ",lst)

for i in range(n-1):
    for j in range(n-i-1):
        if(lst[j] > lst[j+1]):
             temp = lst[j]
             lst[j] = lst[j+1]
             lst[j+1] = temp
print("After sorting array elements are: ", lst)

#Insertion sort has advantages like: Simple implementation, Efficient for small data sets, Adaptive(it is appropriate for data sets that are already substantially sorted).