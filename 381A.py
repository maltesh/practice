# http://codeforces.com/contest/381/problem/A
import math
def play_game():
    n = int(raw_input())
    cards = map (int, raw_input().split(' '))
    temp = []
    ln = len(cards)-1
    i = 0
    s = 0
    r = 0
    p  = True
    while i <= ln :
        if  cards[i] > cards[ln] : 
            if p:
                s = s + cards[i]
            else:
                r = r + cards[i]
            i = i + 1
        else:
            if p:
                s = s + cards[ln]
            else:
                r = r + cards[ln]
            ln = ln -1
        p = False if p else True
    return  str(s)  + ' ' + str( r)

if __name__ == "__main__":
    print play_game()