# http://codeforces.com/contest/443/problem/A

ip = raw_input()[1:-1]
ip = map(None,map(str.strip,map(str,ip.split(",")))) if ip else []
print len(set(ip))