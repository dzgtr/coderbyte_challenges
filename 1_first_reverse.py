"""Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
For example: if the input string is "Hello World and Coders" then your program should return
the string sredoC dna dlroW olleH. """

def FirstReverse(strParam):

  # code goes here
  strParam = strParam[::-1]
  return strParam

# keep this function call here
print(FirstReverse(input()))
