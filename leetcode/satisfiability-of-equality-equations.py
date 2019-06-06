"""
https://leetcode.com/contest/weekly-contest-123/problems/satisfiability-of-equality-equations/
"""


class Solution:
	def equationsPossible(self, equations: 'List[str]') -> 'bool':
		right = []
		wrong = []

		def func(add_to, check_not_in, x, y):
			for i in check_not_in:
				if x in i and y in i:
					return False
			added = False
			for i in range(len(add_to)):
				if x in add_to[i] or y in add_to[i]:
					add_to[i] = f"{add_to[i]}{x}{y}"
					added = True
					break
			if added is False:
				add_to.append(f"{x}{y}")

		for i in equations:
			if "==" in i:
				parts = i.split("==")
				x, y = parts[0], parts[1]

				if func(right, wrong, x, y) is False:
					return False
		for i in equations:
			if "!=" in i:
				parts = i.split("!=")
				x, y = parts[0], parts[1]
				if x == y:
					return False
				if func(wrong, right, x, y) is False:
					return False
		return True



