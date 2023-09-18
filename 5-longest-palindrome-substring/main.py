TESTS = {
    "babad": ["bab", "aba"],
    "cbbd": ["bb"],
    "aaaaa": ["aaaaa"],
    "abcdefgh": ["a"],
    "": [""],
    "abaffkajak": ["kajak"],
    "abbcccbbbcaaccbababcbcabca": ["bbcccbb"],
    "cbcdcbedcbc": ["bcdcb"]
}

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"

        str_len = len(s)
        l, r = 0, 0  # boundaries (left, right) of current longest palindrome. Initially, it is empty string
        radiuses = {}  # Mapping index to a radius of longest palindrome, which has center at this index.

        for center in range(0, str_len):
            radius = 0

            # Manacher's algorithm – this is a part that speeds up computation
            if center < r:
                mirrored_center = l + (r - center)
                mirrored_radius = radiuses[mirrored_center]

                if center + mirrored_radius < r:
                    radiuses[center] = mirrored_center
                    continue

                # Can't take mirrored radius directly, because we may skip some chars
                # between r and center + mirrored radius
                radius = min(r-center, mirrored_radius)

            # Trivial Algorithm:
            while (
                    center - radius >= 0 and
                    center + radius < str_len and
                    s[center - radius] == s[center + radius]
            ):
                radius += 1
            radius = radius - 1  # Because when loop stopped, the radius was already too big by one

            radiuses[center] = radius

            # Update longest palindrome
            if (2 * radius + 1) > (r + 1 - l):
                l = center - radius
                r = center + radius
        return s[l:r+1].replace("#", "")


if __name__ == "__main__":
    solution = Solution()
    method = getattr(solution, list(filter(lambda m: not m.startswith("_"), dir(solution)))[0])
    for _input, expected_output in TESTS.items():
        actual_output = method(_input)
        if actual_output in expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
