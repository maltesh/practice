# https://codeforces.com/contest/236/problem/A

fml_msg = 'CHAT WITH HER!'
ml_msg = 'IGNORE HIM!'
inp = raw_input()
t_c  = len(list (set(inp)))
if t_c % 2 == 0:
    print fml_msg
else:
    print ml_msg