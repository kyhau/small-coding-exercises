"""
Implement a function that outputs the Look and Say sequence:
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""


def look_and_say(n):
    ret = []
    for i in range(n):
        tmp = []
        if not ret:
            tmp.append(1)
        else:
            target, cnt = None, 0
            for c in ret[-1]:
                if target is None:
                    target = c
                    cnt += 1
                else:
                    if target == c:
                        cnt += 1
                    else:
                        tmp.append(cnt)
                        tmp.append(target)
                        target = c
                        cnt = 1
            if target is not None:
                tmp.append(cnt)
                tmp.append(target)
        ret.append(tmp)
    return ret


ret = look_and_say(10)

for r in ret:
    print("".join([str(i) for i in r]))
