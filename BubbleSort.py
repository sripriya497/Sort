#Bubble sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
bubble_sort([5,4,3,2,1,0])

'''
Bubble sort: Compares adjacent elements and swaps if they are not in order
Run-time: O(n^2) - can be used for small dataset
'''
