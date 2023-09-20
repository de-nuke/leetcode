from functools import lru_cache

TESTS = {
    ("aa", "a"): False,
    ("ab", "ab"): True,
    ("ab", ".."): True,
    ("abc", ".."): False,
    ("abc", "a.."): True,
    ("abc", "aac"): False,
    ("aa", "a*"): True,
    ("aaaaaa", "a*"): True,
    ("baaaaaa", "ba*"): True,
    ("ab", ".*"): True,
    ("abcde..**", ".*"): True,
    ("", "abc.*def*"): False,
    ("abcgggde", "abc.*def*"): True,
    ("e", "ef*"): True,
    ("abcgggdeffff", "abc.*def*"): True,
    ("", ".*"): True,
    ("", "."): False,
    ("aab", "c*a*b"): True,
    ("aaaaaaabbbbbbbbbccc", ".*.*c"): True,
    ("aaacc", ".*c"): True,
    ("aaa", "a*a"): True,
    ("aaa", "a*"): True,
    ("aaa", ".*."): True,
    ("mississippi", "mis*is*ip*."): True,
    ("ab", "a*."): True,
    ("aaa", "ab*a*c*a"): True,
    ("ab", ".*.."): True,
}


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Regular expression matching
        https://leetcode.com/problems/regular-expression-matching/

        Solution stolen from here:
        https://www.youtube.com/watch?v=HAA8mgxlov8

        My solution wasn't working. It's in the commented section.
        """

        @lru_cache
        def dfs(s_pos, p_pos):
            if s_pos >= len(s) and p_pos >= len(p):
                return True

            if p_pos >= len(p):
                return False

            match = s_pos < len(s) and (s[s_pos] == p[p_pos] or p[p_pos] == ".")
            if (p_pos + 1) < len(p) and p[p_pos + 1] == "*":
                return dfs(s_pos, p_pos + 2) or (match and dfs(s_pos + 1, p_pos))

            if match:
                return dfs(s_pos + 1, p_pos + 1)

            return False

        return dfs(0, 0)

        # p_pos = 0
        # s_pos = 0
        # while p_pos < len(p):
        #     while p_pos < len(p) and p[p_pos] != "*":
        #         next_signal = p[p_pos + 1] if (p_pos + 1) < len(p) else None
        #         if next_signal == "*":
        #             break
        #         if s_pos >= len(s) or p[p_pos] not in {".", s[s_pos]}:
        #             return False
        #         p_pos += 1
        #         s_pos += 1
        #
        #     if p_pos < len(p) and p[p_pos] == "*":
        #         prev_signal = p[p_pos-1]
        #         next_signal = p[p_pos+1] if (p_pos + 1) < len(p) else None
        #
        #         while s_pos < len(s) and prev_signal in {s[s_pos], "."}:
        #             if next_signal and (
        #                     next_signal in {s[s_pos], "."}
        #                     and (
        #                         next_signal not in {s[s_pos+1], "."}
        #                         if s_pos+1 < len(s)
        #                         else True
        #                     )
        #             ):
        #                 break
        #             s_pos += 1
        #
        #     p_pos += 1
        #
        # if s_pos != len(s):
        #     return False
        # return True

        # p_pos = 0
        # pattern_parts = []
        # while p_pos < len(p):
        #     signal = p[p_pos]
        #     if p_pos < len(p) - 1 and p[p_pos + 1] == "*":
        #         pattern_parts.append(signal + "*")
        #         p_pos += 2
        #     else:
        #         pattern_parts.append(signal)
        #         p_pos += 1
        #
        # s_pos = 0
        # for pat_pos, pattern_part in enumerate(pattern_parts):
        #     if pattern_part == ".":
        #         s_pos += 1
        #         continue
        #
        #     if len(pattern_part) == 1:
        #         if s_pos < len(s) and s[s_pos] != pattern_part:
        #             return False
        #         s_pos += 1
        #     else:
        #         signal = pattern_part[0]
        #         next_pattern = (
        #             pattern_parts[pat_pos + 1]
        #             if pat_pos < len(pattern_parts) - 1
        #             else None
        #         )
        #
        #         if next_pattern is None:
        #             while s_pos < len(s) and signal in {s[s_pos], "."}:
        #                 s_pos += 1
        #         else:
        #             while (
        #                 s_pos < len(s)
        #                 and signal in {s[s_pos], "."}
        #                 and (
        #                     not self.isMatch(s[s_pos], next_pattern)
        #                     or (
        #                         (s_pos + 1) < len(s)
        #                         and self.isMatch(s[s_pos + 1], next_pattern)
        #                     )
        #                 )
        #             ):
        #                 s_pos += 1
        # if s_pos != len(s):
        #     return False
        # return True


if __name__ == "__main__":
    solution = Solution()
    method = getattr(
        solution, list(filter(lambda m: not m.startswith("_"), dir(solution)))[0]
    )
    for _input, expected_output in TESTS.items():
        actual_output = method(*_input)
        if not isinstance(expected_output, list):
            expected_output = [expected_output]

        if actual_output in expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[  ] {_input} -> {actual_output} (expected: {expected_output})")
