import sys

#TOtal Columns - s+2
# Total Rows   - 2s + 3
horizontal_padding_size = 2
vertical_padding_size = 3
def drawHorizoneTal(n):
    padding = horizontal_padding_size / 2
    return ' '*padding + '-'*n + ' '*padding


def drawLeftTopVertiCal(spacing):
    tmplt = ""
    for i in range(spacing):
        tmplt=tmplt+"|\n"
    return  tmplt.rstrip("\n")

def drawTwoVertiCal(spacing):
    fmt = "|%"+str(spacing+1)+"s"
    ss = [fmt%"|" for i in range(spacing)]
    return "\n".join(ss)

def drawRightVertiCal(spacing):
    fmt = "%"+str(spacing+2)+"s"
    ss = [fmt%"|" for i in range(spacing)]
    return "\n".join(ss)



filename = sys.argv[1]
lines   = open(filename,'r').readlines()
for line in lines:
    inpp = line.split(" ")
    if inpp[0] != '0' and inpp[1] != '0':
        spacing = int(inpp[0])
        digits = inpp[1].rstrip("\n")
        digits = map(int,list(digits))
        inp =spacing
        for i in digits:
            if i ==0:
                print drawHorizoneTal(inp)
                print drawTwoVertiCal(inp)
                print drawHorizoneTal(inp)
                print drawTwoVertiCal(inp)
                print drawHorizoneTal(inp)
            if i ==1 :
                print drawLeftTopVertiCal(inp)
                print drawLeftTopVertiCal(inp)
            if i ==2 :
                print drawHorizoneTal(inp)
                print drawRightVertiCal(inp)
                print drawHorizoneTal(inp)
                print drawLeftTopVertiCal(inp)
                print drawHorizoneTal(inp)
            if i == 3:
                print drawHorizoneTal(inp)
                print drawRightVertiCal(inp)
                print drawHorizoneTal(inp)
                print drawRightVertiCal(inp)
                print drawHorizoneTal(inp)
            if i ==4 :
                print drawTwoVertiCal(inp)
                print drawHorizoneTal(inp)
                print  drawRightVertiCal(inp)

# print drawHorizoneTal(2)
# print drawLeftTopVertiCal(2)
