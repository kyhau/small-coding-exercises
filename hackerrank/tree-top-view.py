"""
https://www.hackerrank.com/challenges/tree-top-view/problem
"""


def topView(root):
    def set_degree_and_level(node, degree, level, ret):
        if node is not None:
            node.degree = degree
            node.level = level
            if level == len(ret):
                ret.append([node])
            else:
                ret[node.level].append(node)
            set_degree_and_level(node.left, degree - 1, level + 1, ret)
            set_degree_and_level(node.right, degree + 1, level + 1, ret)

    ret = []
    set_degree_and_level(root, 0, 0, ret)

    d = {}
    for row in range(len(ret) - 1, -1, -1):
        mi = ma = ret[row][0]
        for j in ret[row]:
            if j.degree < mi.degree:
                mi = j
            elif j.degree > ma.degree:
                ma = j
        d[mi.degree] = mi.info
        d[ma.degree] = ma.info
    print(" ".join(str(d[k]) for k in sorted(d.keys())))
