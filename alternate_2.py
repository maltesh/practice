

#co = int(raw_input().strip())
#inpts = []
#while co > 0:
#    inpts.append(raw_input().strip())
#    co = co-1

inpts =[  'AAAA' ]
for s in inpts:
	tc = 0
	chr = s[0]
	for i in s[1:]:
		if chr == i:
		    tc = tc+1
		else:
		    chr = i
			
	print tc
