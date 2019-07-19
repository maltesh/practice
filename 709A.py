n ,b, d  = map(int,raw_input().split(' '))
oranges = map(int,raw_input().split(' '))
total = 0
size = 0
bl = False
for orange in oranges:
    if orange > b:
        continue
    size = size + orange
    if size > d:
        total = total + 1
        size =0


print total