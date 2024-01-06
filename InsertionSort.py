#Insertion Sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]

            j-=1
        arr[j+1] = tmp
    print(arr)

insertion_sort([5,4,3,2,1])


'''
Insertion sort: compare element in the left and shift to right if less than the tmp
run-time: O(n^2)
less steps than bubble sort. Best case is O(n) compared to selection sort O(n^2)
'''