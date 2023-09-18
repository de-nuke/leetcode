TESTS = {
    "babad": ["bab", "aba"],
    "cbbd": ["bb"],
    "aaaaa": ["aaaaa"],
    "abcdefgh": ["a", "b", "c", "d", "e", "f", "g", "h"],
    "": [""],
    "abaffkajak": ["kajak"],
    "abbcccbbbcaaccbababcbcabca": ["bbcccbb"],
    "cbcdcbedcbc": ["bcdcb"],
}


class Solution:
    """
    Longest palindrome substring
    https://leetcode.com/problems/longest-palindromic-substring

    The solution is an implementation of Manacher's algorithm.
    """

    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"

        str_len = len(s)
        left, right = 0, 0  # boundaries of current longest palindrome
        radiuses = {}  # Mapping palindrome center to its radius

        for center in range(0, str_len):
            radius = 0

            # Manacher's algorithm – this is a part that speeds up computation
            if center < right:
                mirrored_center = left + (right - center)
                mirrored_radius = radiuses[mirrored_center]

                if center + mirrored_radius < right:
                    radiuses[center] = mirrored_center
                    continue

                # Can't take mirrored radius directly, because we may skip some
                # chars between right and center + mirrored radius
                radius = min(right - center, mirrored_radius)

            # Trivial Algorithm:
            while (
                center - radius >= 0
                and center + radius < str_len
                and s[center - radius] == s[center + radius]
            ):
                radius += 1

            # Loop stops after radius is incremented,
            # so it must be decremented to get the last "valid" value
            radius = radius - 1
            radiuses[center] = radius

            # Update longest palindrome
            if (2 * radius + 1) > (right + 1 - left):
                left = center - radius
                right = center + radius
        return s[left : right + 1].replace("#", "")


if __name__ == "__main__":
    solution = Solution()
    method = getattr(
        solution, list(filter(lambda m: not m.startswith("_"), dir(solution)))[0]
    )
    for _input, expected_output in TESTS.items():
        actual_output = method(_input)
        if actual_output in expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
