"""Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers,
letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers
that add up to 10. If so, then your program should return the string true, otherwise it should return the string false.
 If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are
exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
"""
import re

def QuestionsMarks(strParam):

      # code goes here
      qmark_count = 0
      digits = []
      output = False
      stripped = re.sub("[A-Za-z]", "", strParam)
      for x in stripped:
          if x == "?" and len(digits) != 0:
              qmark_count += 1
          if x.isdigit():
              digits.append(int(x))
              if len(digits) == 1:
                  qmark_count = 0
              if len(digits) == 2:
                  if digits[0]+digits[1] == 10:
                      if qmark_count == 3:
                        output = True
                      else:
                        output = False
                        break
                  qmark_count = 0
                  helper = digits[1]
                  digits.clear()
                  digits.append(helper)
      return output

# keep this function call here
print(QuestionsMarks(input()))