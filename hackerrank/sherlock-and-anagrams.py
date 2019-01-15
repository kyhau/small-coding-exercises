"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    is_anagram = lambda w1, w2: sorted(list(w1)) == sorted(list(w2))

    anagrams = 0

    # note: put strlen-loop out of pos-loop to avoid comparing "strlen==1" again for each pos
    for strlen in range(1, len(s)):
        for pos in range(len(s)):
            if strlen < len(s) - pos:
                s1 = s[pos:pos + strlen]
                pos2 = pos + 1
                while pos2 + strlen <= len(s):
                    s2 = s[pos2:pos2 + strlen]
                    if is_anagram(s1, s2):
                        anagrams += 1
                    pos2 += 1

    return anagrams
