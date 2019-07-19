s = raw_input()
instruction = raw_input()
i = 0
pos = 0
for char in instruction:
    if char == s[pos]:
        pos = pos + 1
print pos + 1