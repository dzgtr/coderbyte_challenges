"""
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are
correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))",
then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets
do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
"""
import re

def BracketMatcher(strParam):
    # code goes here
    left = 0
    right = 0
    strParam = re.sub("[A-Za-z]", "", strParam)
    for bracket in strParam:
        if bracket == "(":
            left += 1
        elif bracket == ")":
            right += 1
        if right>left:
            return 0
    if left == right:
        return 1
    else:
        return 0

# keep this function call here
print(BracketMatcher(input()))