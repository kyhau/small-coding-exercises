"""
https://www.hackerrank.com/challenges/electronics-shop/problem
"""
import os
import sys


def getMoneySpent(keyboards, drives, b):

    # Sort the prices in descending order
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)

    # Case 1: Cannot afford even the cheapest keyboard and drive
    if keyboards[-1] + drives[-1] > b:
        return -1

    # Case 2: The total of the most expensive keyboard and drive is less than b
    max_spend = b
    if keyboards[0] + drives[0] < b:
        max_spend = keyboards[0] + drives[0]

    # Remove all keyboards and drives that the single price is already greater than b
    def remove_item_not_affortable(item_list, max_spend):
        k = 0
        while k < len(item_list):
            if item_list[k] < max_spend:
                break
            del item_list[k]
        return item_list

    keyboards = remove_item_not_affortable(keyboards, max_spend)
    drives = remove_item_not_affortable(drives, max_spend)

    for max_value in range(max_spend, 0, -1):
        for posk in range(len(drives)):
            diff = max_value - drives[posk]
            for keyboard in keyboards:
                if keyboard == diff:
                    return max_value
                if keyboard < diff:
                    break
    return max_value
