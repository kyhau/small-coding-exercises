"""
https://leetcode.com/problems/task-scheduler/
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        d = {}
        # ret = []
        curr_cnt = 0
        commons = c.most_common()
        while commons:
            prev_cnt = curr_cnt
            for item, _ in commons:
                if item not in d or (item in d and curr_cnt - d[item] >= n):
                    # ret.append(item)
                    curr_cnt += 1
                    d[item] = curr_cnt
                    c[item] -= 1
                    if c[item] == 0:
                        del c[item]
                    commons = c.most_common()
                    break
            if curr_cnt == prev_cnt:
                # append idle
                # ret.append("idle")
                curr_cnt += 1
            commons = c.most_common()
            # print(ret)
        return curr_cnt


"""
["A","A","A","A","A","A","B","C","D","E","F","G"]
2
Expected:
16
"""
