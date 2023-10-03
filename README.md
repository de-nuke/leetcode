## Init development environment:
1. `python3 -m venv venv`
2. `source ./venv/bin/activate/`
3. `python3 -m pip install -r requirements.txt`
4. `chmod u+x leetcode.py`

## Generate boilerplate for a problem:
`./leetcode.py PROBLEM_URL [recreate]`

* `PROBLEM_URL` is an url to the problem on [leetcode.com](https://leetcode.com/)
* `recreate` is optional flag indicating that existing directory and all 
files for the given problems should be overwritten if they exist.

Examples:
* `./leetcode2.py https://leetcode.com/problems/4sum/`
* `./leetcode2.py https://leetcode.com/problems/4sum/ recreate`
