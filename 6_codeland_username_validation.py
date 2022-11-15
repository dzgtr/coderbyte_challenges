"""
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string
 is a valid username according to the following rules:
1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.
If the username is valid then your program should return the string true, otherwise return the string false. """

import re

def CodelandUsernameValidation(strParam):

    # code goes here
    isvalid = True
    if len(strParam) not in range(4,26):
        isvalid = False
    if not bool(re.match("[A-Za-z]", strParam[:1])):
        isvalid = False
    if not bool(re.search("^[A-Za-z0-9_]*$", strParam)):
        isvalid = False
    if strParam[-1] == "_":
        isvalid = False
    return isvalid

# keep this function call here
print(CodelandUsernameValidation(input()))