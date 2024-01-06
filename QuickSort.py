#Quick Sort
def quick_sort(arr, start, end):
    if end <= start:
        return
    pividx = partition(arr,start,end)
    quick_sort(arr,start,pividx-1)
    quick_sort(arr,pividx+1,end)
    
            
def partition(arr, start, end):
    piv_val = arr[end]
    i = start - 1
    for j in range(start,end):
        if arr[j] < piv_val:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    i+=1
    arr[i],arr[end] = arr[end],arr[i]
    return i

l = [10,9,21,4,30,90,17,44,50] 
quick_sort(l, 0, len(l)-1)
print(l)

'''
quick sort: move smaller elements to left of pivot. recursively divide array in two partitions and run quick sort
run-time complexity: O(nlogn) => best case and average case
                     O(n^2) => worst case if already sorted
space complexity: O(logn) due to recursion
'''
