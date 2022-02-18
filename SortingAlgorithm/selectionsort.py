lst=[]
n= int(input("Enter the number of elements: "))
for i in range(n):
    elem= int(input())
    lst.append(elem)
print("Before sorting array elements are: ",lst)

for i in range(n):
    small=i
    for j in range(i+1, n):
        if lst[small] > lst[j]:
            small=j
    lst[i], lst[small] = lst[small], lst[i] #swapping found minimum element with first element            
print("After sorting array elements are: ", lst)

#It sorts an array by repeatedly finding the minimum element(ascending order) from unsorted part and putting it at the beginning.
#The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.