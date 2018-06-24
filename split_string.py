# https://www.codewars.com/kata/split-strings/train/python


def solution(s):
    temp = s[:]
    if len(s)%2 ==1 :        
        temp = temp +'_'
    l = []
    for rng in range(0,len(temp),2):
        l.append(temp[rng:rng+2])
    return l


if __name__ == '__main__':
    print solution('asdfadsf')