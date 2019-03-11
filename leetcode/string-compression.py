"""
https://leetcode.com/problems/string-compression/
"""


class Solution:
    def compress(self, chars: List[str]) -> int:

        def convert_cnt_string(chars, i, cnt):
            # If previous count >= 10
            if cnt >= 10:
                chars.pop(i + 1)
                cnt_str = list(str(cnt))
                for pos in range(len(cnt_str) - 1, -1, -1):
                    chars.insert(i + 1, cnt_str[pos])

        cnt = 1
        for i in range(len(chars) - 1, 0, -1):
            if chars[i] == chars[i - 1]:
                cnt += 1
                chars[i] = str(cnt)
                if cnt > 2:
                    chars.pop(i + 1)
            else:
                convert_cnt_string(chars, i, cnt)
                # Reset cnt to 1
                cnt = 1

        convert_cnt_string(chars, 0, cnt)
        return len(chars)

