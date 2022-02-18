lst=[]
n=int(input("Enter size: "))
for i in range(0,n):
    elem=int(input())
    lst.append(elem)
print("Before sorting array elements are: ")  
print(lst)
for i in range(0,n):    
    for j in range(i+1,n):    
        if lst[j]<lst[i]:    
            temp = lst[j]    
            lst[j]=lst[i]    
            lst[i]=temp    
print("\nAfter sorting array elements are: ")    
print(lst)

#It is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order