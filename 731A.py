# http://codeforces.com/contest/731/problem/A

import string
all_chars = list(raw_input())
char_to_num = dict(zip(string.ascii_lowercase,range(1,27)))
cp = 1
l = 26
total = 0
# print char_to_num
for ltr in all_chars:
    diff = 0
    val = min ( abs(cp - char_to_num[ltr] ) , l - abs(cp - char_to_num[ltr] ))
    total = total + val
    cp = char_to_num[ltr]

print total