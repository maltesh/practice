# http://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python



def permutations(string):
    import itertools
    return set([''.join(item) for item in  itertools.permutations(string,len(string))])
