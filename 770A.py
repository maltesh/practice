# http://codeforces.com/contest/770/problem/A
import string
n, k = map(int,raw_input().split(' '))
ltrs = string.ascii_lowercase[0:k]
diff = n - k
end = ltrs * diff
t =  '%'+ "."+ str( diff )+"s"
k = t%(end)

print ltrs + k