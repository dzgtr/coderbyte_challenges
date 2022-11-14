"""Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty.
Words may also contain numbers, for example "Hello world123 567"
"""

import re

def LongestWord(sen):

  # code goes here
  longest = ""
  stripped = re.sub('[^A-Za-z0-9\ ]+', '', sen)
  words = stripped.split()
  for word in words:
    if len(word)>len(longest):
      longest = word
  return longest

# keep this function call here
print(LongestWord(input()))