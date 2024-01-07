#Linear Search

def linear_search(arr,val):
    for idx,i in enumerate(arr):
        # print(idx,i)
        if i == val:
            return idx
    return

        
print('Element found at index:',linear_search([3,5,7,10,23,52,10,1],1))