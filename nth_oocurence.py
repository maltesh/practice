# https://www.codewars.com/kata/find-the-nth-occurrence-of-a-word-in-a-string/train/python
def find_nth_occurrence(substring, string, occurrence=1):

    k = -1
    count = 0
    ct = 0
    length = len(string)
    while  count < occurrence:
        temp = string.find(substring,  k+1 ,length)
        if temp >= 0:
            k = temp
            count = count +1
        else:
            return -1
    return k

string = "Test1 Test2 Test3 Test4 "
print find_nth_occurrence("Test", string, 2)