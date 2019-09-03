# https://www.codewars.com/kata/printer-errors/train/python
import string
def printer_error(s):
    good_set = list(string.ascii_letters[:13])
    unq_ones = set(sorted(s))
    error = 0
    for leter in unq_ones:
        if leter not in good_set:
            # print leter
            error += s.count(leter)

    return str(error)+'/'+str(len(s))

s="ehfdmiliebciccjmgajgjmmfgbmhjjfedchgkdeljihijdkjhfjeigdmcigkiiefhckhlalmgdgemdglmlbedakbifaflmkkmjhcefbefchkhafdhgikfmlihddhjmijfmjmbdajfifhgdeabhgbglmhbfjlacamjielgbmghbhhgiigacajcafkalcfmfffekecckifkkmhmhkmiajjjifcljhdmgjkejgkbjgchccchgvgkjlfkblhfdchakeuhefelakjbibjfmbizedcjgjhifjakfkiavichjjljhkdliffjjnjiaeimagdmahadlarbablidgiaegkfeeewagkfigfmgikiieaevijeajlajjclclhimsdbgheahbgfebbebfoeaamdkmhiablijgiohdcgkihghhhgljlcxfbbhihgkbmkegjmazejkikaglfclmcdfln"
print printer_error(s)