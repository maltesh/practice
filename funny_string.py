#https://www.hackerrank.com/challenges/funny-string
count = int(raw_input().strip())
while count > 0:
    ip_str = raw_input().strip()
    rev_str = ip_str [::-1]
    d_ips = [ abs( ord(sl) - ord(fl)) for fl , sl in zip(ip_str,ip_str[1:]) ]
    r_ips = [ abs(ord(fl) - ord(sl)) for fl , sl in zip(rev_str,rev_str[1:]) ]
    if d_ips == r_ips :
        print 'Funny'
    else :
        print 'Not Funny'
    count = count -1


