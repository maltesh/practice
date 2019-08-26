# https://www.codewars.com/kata/directions-reduction/train/python

def dirReduc(arr):
    
    t = {
        'north' : 'south',
        'south': 'north',
        'east' : 'west',
        'west' : 'east'
    }
    temp = []

    for k , dirw in enumerate(list(arr)):
        try:
            if  len(temp) >0 and t[dirw.lower()] == temp[-1].lower()  :
                temp.pop(-1)
            else:
                temp.append(dirw)
        except Exception as e :
            continue
    return temp

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
a = ["NORTH", "WEST", "SOUTH", "EAST"]
print dirReduc(a),