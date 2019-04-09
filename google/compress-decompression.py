"""
https://techdevguide.withgoogle.com/paths/advanced/compress-decompression
"""


def func(x):
    while "[" in x
        # Find ], then find last [ before ].
        pos2 = x.find("]")
        pos1 = x.rfind("[", 0, pos2-1)
        substring = x[pos1+1:pos2]

        pos0 = 0
        for pos in range(pos1-1, -1, -1):
            if not x[pos].isdigit():
                pos0 = pos+1
                break
        num = int(x[pos0:pos1])

        x = x[0:pos0] + substring*num + x[pos2+1:]

    print(x)
    return x


ret = func("3[abc]4[ab]c")
assert ret == "abcabcabcababababc"

ret = func("10[a]")
assert ret == "aaaaaaaaaa"

ret = func("2[3[a]b]")
assert ret == "aaabaaab"