def ThreeNPlusOne(high, low=1):
    seq = [high]
    while high > low:
        if high % 2 == 0:
            high = high / 2
        else:
            high = high * 3 + 1
        seq.append(high)
        if high == 1:
            return seq
    return seq

scor = []
hig = 1000
low = 900
scor = map(len, map(ThreeNPlusOne, range(low, hig + 1)))
print low, " ", hig, " ", max(scor)
