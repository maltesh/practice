from collections import Counter
calories = map(int,raw_input().split ( ' '))
seq  = dict(Counter(list(raw_input())))


calories =  dict(zip( range(1, len(calories)+ 1), calories))
temp = 0
# print calories, seq
for key,val in seq.items():
    temp = temp + val * calories.get(int(key),0)

print temp