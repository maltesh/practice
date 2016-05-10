import sys
import math


def isfloat(value):
    try:
        int(value)
        return True
    except:
        return False

filename = sys.argv[1]
fp = file(filename)
lines = fp.readlines()

index = 0
for li in enumerate(lines):
    idx = li[0]
    line = li[1]
    if line.rstrip('\n') != 0:
        num = line.rstrip('\n')
        if isfloat(num) == True:
            items = lines[idx + 1:idx + int(num) + 1]
            summ = sum(map(float, items))
            if summ:
                high = 0
                low = 0
                avg = summ / float(len(items))
                for expense in items:
                    temp = float(expense) - avg
                    if temp > 0:
                        high = high + math.floor(temp * 100) / 100
                    else:
                        low = low - math.ceil(temp * 100) / 100

                print max([low, high])
