# https://www.codewars.com/kata/return-substring-instance-count-2/train/python


def search_substr(full_text, search_text, allow_overlap=True):
    temp  = []
    if search_text:        
        if allow_overlap:
            idx = full_text.find(search_text)
            if idx >=0:
                t = idx + 1
                return 1+search_substr(full_text[t:]  ,search_text,allow_overlap  )
        else:
            return full_text.count(search_text)
    return 0

