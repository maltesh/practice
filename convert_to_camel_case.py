# https://www.codewars.com/kata/convert-string-to-camel-case/train/python


from string import capwords

def to_camel_case(text):
    idx = []
    tmep = []
    if text:
        tmep.extend(text.split('-'))
        for ite in tmep:
            idx.extend(ite.split('_'))
        idx[0] = capwords(idx[0]) if  idx[0][0].isupper() else idx[0]
        return idx[0]+''.join(map(capwords,idx[1:]))
    return ''


if __name__ == '__main__':
    print to_camel_case("the_Pippi-was_evil")