
assert (1==1)
def bin_search(arr,pivot):
    arr = sorted(arr)
    low=0
    high=len(arr)-1
    if arr[len(arr)/2] == pivot:
        return high/2
    elif arr[(high+low)/2]<pivot:
        bin_search(arr[low:high/2],pivot)

    elif arr[(high+low)/2]>pivot:
        bin_search(arr[high/2:high],pivot)


print bin_search([2,3,5],2)


