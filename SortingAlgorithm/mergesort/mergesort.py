lst=[]
n= int(input("Enter the number of elements: "))
for i in range(n):
    elem= int(input())
    lst.append(elem)
print("Before sorting array elements are: ",lst)

def merge_sort(lst, left_index, right_index):  
    if left_index >= right_index:  
        return  
    
    middle = (left_index + right_index)//2  
    merge_sort(lst, left_index, middle)  
    merge_sort(lst, middle + 1, right_index)  
    merge(lst, left_index, right_index, middle)  
  
def merge(lst, left_index, right_index, middle):  
    left_sublist = lst[left_index:middle + 1]  
    right_sublist = lst[middle+1:right_index+1]  
  
    left_sublist_index = 0  
    right_sublist_index = 0  
    sorted_index = left_index  
 
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):  
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:  
            lst[sorted_index] = left_sublist[left_sublist_index]  
            left_sublist_index = left_sublist_index + 1 
        else:  
            lst[sorted_index] = right_sublist[right_sublist_index]  
            right_sublist_index = right_sublist_index + 1  
        sorted_index = sorted_index + 1
    while left_sublist_index < len(left_sublist):  
        lst[sorted_index] = left_sublist[left_sublist_index]  
        left_sublist_index = left_sublist_index + 1  
        sorted_index = sorted_index + 1  
    while right_sublist_index < len(right_sublist):  
        lst[sorted_index] = right_sublist[right_sublist_index]  
        right_sublist_index = right_sublist_index + 1  
        sorted_index = sorted_index + 1
        
merge_sort(lst, 0, len(lst) -1)        
print("After sorting array elements are: ", lst)