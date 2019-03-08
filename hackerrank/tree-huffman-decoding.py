"""
https://www.hackerrank.com/challenges/tree-huffman-decoding/problem
"""


def decodeHuff(root, s):
    def func(node, inputs, outputs):
        if node.data.isprintable():
            outputs.append(node.data)
        else:
            value = inputs.pop(0)
            func(node.left if value=='0' else node.right, inputs, outputs)

    inputs = list(s)
    outputs = []

    while inputs:
        func(root, inputs, outputs)
    print("".join(outputs))
