"""
https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
"""

import math
import os
import random
import re
import sys


# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    def func(curr_ptr):
        if curr_ptr.next is None:
            return curr_ptr, curr_ptr

        new_root_head, parent_ptr = func(curr_ptr.next)
        parent_ptr.next = curr_ptr
        curr_ptr.next = None
        return new_root_head, curr_ptr

    new_root_head, _ = func(head)
    return new_root_head

