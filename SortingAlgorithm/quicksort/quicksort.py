def quicksort(lst, start, end):
    if end - start > 1:
        p = partition(lst, start, end)
        quicksort(lst, start, p)
        quicksort(lst, p + 1, end)
 
 
def partition(lst, start, end):
    pivot = lst[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and lst[i] <= pivot):
            i = i + 1
        while (i <= j and lst[j] >= pivot):
            j = j - 1
 
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
        else:
            lst[start], lst[j] = lst[j], lst[start]
            return j
 
 
lst = input('Enter the list of numbers: ').split()
lst = [int(x) for x in lst]
quicksort(lst, 0, len(lst))
print('Sorted list: ', end='')
print(lst)