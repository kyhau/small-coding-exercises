"""
https://www.hackerrank.com/challenges/ginorts

Sort the string in the following manner:
1. All sorted lowercase letters are ahead of uppercase letters.
2. All sorted uppercase letters are ahead of digits.
3. All sorted odd digits are ahead of sorted even digits.

Some decent solutions from "Discussions"
"""
import logging
logging.getLogger().setLevel(logging.DEBUG)


def sol_1(s):
    order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
    return sorted(s, key=order.index)


def sol_2(s):
    import string
    # string.ascii_letters == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sorted(s, key=(string.ascii_letters + "1357902468").index)


def sol_3(s):
    #for c in s:
    #    logging.debug(f"({c.isdigit()-c.islower()}, {c in '02468'}, {c})")
    return sorted(s, key=lambda c: (c.isdigit() - c.islower(), c in "02468", c))


def sol_4(s):
    # Use ord.
    # The ord() method returns an integer representing Unicode code point for the given Unicode character.
    # After >>5, -2 means digit, -3 means upper case, -4 means lower case
    #for c in s:
    #    logging.debug(f"({ord(c)} {-ord(c)} {-ord(c)>>5}, {c in '02468'}, {c})")
    return sorted(s, key=lambda c: (-ord(c) >> 5, c in "02468", c))


test_data = ["Aa", "23", "BA", "87c2wFhWJh9eLf"]
expected = ["aA", "32", "AB", "cefhhwFJLW7928"]
for i in range(len(test_data)):
    for func in [sol_1, sol_2, sol_3, sol_4]:
        ret = func(test_data[i])
        #print(*ret, sep="")
        assert "".join(ret) == expected[i]
