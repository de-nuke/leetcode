TESTS = {
    ("PAYPALISHIRING", 3): "PAHNAPLSIIGYIR",
    ("PAYPALISHIRING", 4): "PINALSIGYAHRPI",
    ("DOMEKNAMAZURACH", 4): "DAAONMRCMKAUHEZ",
    ("DOMEKNAMAZURACH", 5): "DAOMZMAUHENRCKA",
    ("A", 1): "A",
    ("ABCD", 3): "ABDC",
    ("ABCDE", 4): "ABCED",
    ("", 3): "",
    ("A", 3): "A",
}


class Solution:
    """
    ZigZag Conversion – https://leetcode.com/problems/zigzag-conversion/

    Let's represent a string as a ZigZag with "amplitude" defined as "numRows".
    For example, if numRows == 4 and string length == 16, then the ZigZag would be:

    A     G     M
     B   F H   L N
      C E   I K   O
       D     J     P

    Now, let's turn each character into its index in the string:
    0     6       12
     1   5 7    11  13
      2 4   8 10      14
       3     9          15

    If we read indices line by line and map each index into a string, then we get the
    expected result. In this example, it would be:
    – indices read line by line: 0,6,12,1,5,7,11,13,2,4,8,10,14,3,9,15
    – As chars: A,G,M,B,F,H,L,N,C,E,I,K,O,D,J,P

    The main difficulty is to produce a list of indices for each row, like this:
    - row 0 -> 0,6,12
    - row 1 -> 1,5,7,11,13
    - etc...

    We can observe that indices in each row are incremented by concrete two numbers
    alternately:
    - row 0 -> indexes are incremented by 6, by 0, by 6, by 0, etc.
    - row 1 –> indexes are incremented by 4, by 2, by 4, by 2, etc.
    - row 2 -> indexes are incremented by 2, by 4, by 2, by 4, etc.
    - row 3 -> indexes are incremented by 0, by 6, by 0, by 6, etc.

    Additionally, indexes in each row are shifted by the row number itself:
    – row 0 -> indexes shifted by 0
    – row 1 -> indexes shifted by 1
    – row 2 -> indexes shifted by 2
    – row 3 -> indexes shifted by 3

    It turns out, that "steps" for each row can be calculated based on row number
    and total number of rows using this formula:
    - step[0] = 2 * (numRows - row - 1)
    - step[1] = 2 * row

    Taking all of the above together, we can write an algorithm to build a result:

    - set results as empty string
    - For each row:
        - calculate steps
        - based on steps, generate indices as long as they are lower than string length
        - for each generated index, take character at this position in the string and
          append it to the result.
    - return the result.

    There are some edge cases, when the result will always be equal to the input string:
    - if number of rows is 1, OR
    - if number of rows is greater than or equal to string's length
    """

    def convert(self, s: str, numRows: int) -> str:
        str_len = len(s)
        if numRows == 1 or numRows >= str_len:
            return s

        result = ""
        for row in range(numRows):
            result += s[row]  # Assuming row < string's length

            steps = (2 * (numRows - row - 1), 2 * row)  # Assuming numRows != 1

            i = row
            step_idx = 0
            while i < str_len:
                step = steps[step_idx]
                if step:
                    i = i + step
                    if i < str_len:
                        result += s[i]
                    else:
                        break

                step_idx = not step_idx  # Switch 0 to 1, and 1 to 0

        return result


if __name__ == "__main__":
    solution = Solution()
    method = getattr(
        solution, list(filter(lambda m: not m.startswith("_"), dir(solution)))[0]
    )
    for _input, expected_output in TESTS.items():
        actual_output = method(*_input)
        if actual_output == expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
