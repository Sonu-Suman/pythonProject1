"""
# This is leet code problem


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order
"""

# THis is basic problem on this topic

import re

pattern = re.compile(r'[]()[{}]')

def setup(s):
    if re.match(pattern, s, flags=0):
        return True
    else:
        return False


print(setup("([)]"))

# This is  the solution

def isValid(s: str) -> bool:
        s = list(s)
        myhash ={"(":")", "{":"}", "[":"]"}
        stack = []
        openers = ["(", '{', '[']
        closers = [")", '}', ']']
        for x in s:
            if x in openers:
                stack.append(x)
            elif x in closers:
                if (len(stack) == 0):
                    return False
                opener = stack.pop()
                if myhash[opener] == x:
                    pass
                else:
                    return False
        return len(stack) == 0


print(isValid("([)]"))
