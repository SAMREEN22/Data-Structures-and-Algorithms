lst=[]
n= int(input("Enter the number of elements: "))
for i in range(n):
    elem= int(input())
    lst.append(elem)
print("Before sorting array elements are: ",lst)

def heapify(lst, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and lst[largest] < lst[l]:
        largest = l
    if r < n and lst[largest] < lst[r]:
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

def heapSort(lst):
    n = len(lst)
    for i in range(n//2 - 1, -1, -1):
        heapify(lst, n, i)
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
        
heapSort(lst)        
print("After sorting array elements are: ", lst)