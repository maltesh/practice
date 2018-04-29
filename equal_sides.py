def find_even_index(arr):
    temp = 0
    for ky,val in enumerate(arr):
        if temp == sum(arr[ky+1:]):
            return ky
        temp =temp+val
    return -1





# print find_even_index([1,2,3,4,3,2,1])
# print find_even_index([1,100,50,-51,1,1])
# print find_even_index([20,10,-80,10,10,15,35])
# print find_even_index([10,-80,10,10,15,35,20])
# print find_even_index(range(1,100))
print find_even_index([0,0,0,0,0])