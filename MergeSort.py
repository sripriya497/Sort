#Merge Sort

def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return
    mid = length//2
    # print('mid',mid)
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    merge_sort(leftarr)
    merge_sort(rightarr)
    # print(leftarr, rightarr, arr)
    merge(leftarr,rightarr,arr)
    # print(arr)

def merge(left, right, arr):
    llen = len(arr)//2
    rlen = len(arr)-llen
    l = r = i = 0
    while l < llen and r < rlen:
        if left[l] < right[r]:
            arr[i] = left[l]
            l+=1
            i+=1
        else:
            arr[i] = right[r]
            r+=1
            i+=1
    while l < llen:
        arr[i] = left[l]
        i+=1
        l+=1
    while r < rlen:
        arr[i] = right[r]
        r+=1
        i+=1

arr = [9,7,5,3,1,8,6,4,2,0]
merge_sort(arr)
print(arr)

