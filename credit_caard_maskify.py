#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

# return masked string
def maskify(cc):
    if cc and len(cc)>=4:
        return  (len(cc)-4)*'#' + cc[-4::]
    return cc

print maskify("Nananananananananananananananana Batman!") == "####################################man!"