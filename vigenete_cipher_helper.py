# -*- encoding: utf-8 -*-
# https://www.codewars.com/kata/vigenere-cipher-helper/train/python


class VigenereCipher(object):
    num_char_map = {}
    char_num_map = {}
    max_rng =0
    ref_key_map ={};
    text =''
    default_encoding = 'utf8'
    def __init__(self, key, alphabet):
        key = key.decode(self.default_encoding)
        alphabet = alphabet.decode(self.default_encoding)
        self.num_char_map = dict(zip(range(0,len(alphabet)),alphabet))
        self.char_num_map = dict(zip(alphabet,range(0,len(alphabet))))
        self.ref_key_map = [ self.char_num_map[c] for c in key]
        self.max_rng = len(alphabet)
    
    def encode(self, text):
        es = ''
        text = text.decode(self.default_encoding)
        self.text = text
        for index,val in enumerate(text):
            try:
                idx = self.char_num_map[val]+self.get_index(index)                
                cr_idx = idx if idx < self.max_rng else idx - self.max_rng 
                es = es + self.num_char_map[cr_idx]
            except:
                es = es + val
        return es.encode(self.default_encoding)
    
    def get_index(self,index):
        try:
            return self.ref_key_map[index]
        except:
            return  self.ref_key_map[index%len(self.ref_key_map)]
    
    def decode(self, text):
        es = ''
        text= text.decode(self.default_encoding)
        self.text = text
        for index,val in enumerate(text):
            try:
                idx = self.char_num_map[val] - self.get_index(index)
                cr_idx = idx if idx <= self.max_rng else idx -self.max_rng 
                if cr_idx < 0:
                    cr_idx = self.max_rng + cr_idx
                es = es + self.num_char_map[cr_idx]
            except:
                es = es +val
        return es.encode(self.default_encoding)



if __name__ == '__main__':
    abc = "アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー"
    key = "カタカナ"
    # print key.encode('ascii')
    c = VigenereCipher(key, abc)
    enc =  c.encode("カタカナ")
    print enc
    dec = c.decode(enc)
    print dec