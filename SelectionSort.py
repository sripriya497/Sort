#Selection Sort

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
            
        arr[i],arr[min] = arr[min], arr[i]
        print(arr)

selection_sort([9,7,5,3,1,0,6,8,4,2])

'''
Selection sort: For each iteration find the minimum value and swap it with the first element of that iteration
run-time: O(n^2) - bad for large dataset
'''