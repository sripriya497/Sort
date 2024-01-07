#Binary Search

def binary_search(arr,val):
     low = 0
     high = len(arr)-1
     while low <= high:
        mid = low + (high-low)//2
        if arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
        else:
            return mid
     return
print('Element found at:',binary_search([2,4,6,8,10,20,24,30],24))
     

