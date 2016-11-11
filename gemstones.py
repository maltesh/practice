
count = int(raw_input().strip())
input = []
while count > 0:
    input.append(set(raw_input().strip()))
    count = count -1
total = reduce(set.intersection,input)
print total


