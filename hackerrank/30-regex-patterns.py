"""
https://www.hackerrank.com/challenges/30-regex-patterns/problem
"""
import re

if __name__ == '__main__':
    N = int(input())
    first_names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        # The (?!.{51}) asserts that it's impossible to match 51 characters
        # starting from the beginning of the string, without actually
        # consuming any of the characters.
        re1 = "^(?!.{51})([a-z.]{1,20})(@gmail.com)$"
        if re.match(re1, emailID):
            first_names.append(firstName)

    for i in sorted(first_names):
        print(i)
