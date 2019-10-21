"""
https://www.hackerrank.com/challenges/keyword-transposition-cipher/
"""
from collections import OrderedDict


def func(s1, s2):
    raw_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def substitution_cipher(s1):
        d = OrderedDict({k:[] for k in s1})
        keys = list(d.keys())

        ss2 = [s for s in list(raw_str) if s not in keys]
        while ss2:
            for i in range(len(keys)):
                if not ss2:
                    break
                d[keys[i]].append(ss2.pop(0))
        
        final = []
        for k in sorted(keys):
            final.append(k)
            final.extend(d[k])
        return final
 
    raw = list(raw_str)
    final = substitution_cipher(s1)

    ret = [raw[final.index(x)] if x != " " else x for x in s2]
    return "".join(ret)


s1 = "SECRET"
s2 = "JHQSU XFXBQ"
expected = "CRYPT OLOGY"
assert func(s1, s2) == expected


s1 = "SPORT"
s2 = "LDXTW KXDTL NBSFX BFOII LNBHG ODDWN BWK"
expected = "ILOVE SOLVI NGPRO GRAMM INGCH ALLEN GES"
assert func(s1, s2) == expected
