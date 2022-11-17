"""Min Window Substring
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
Examples
Input: ["ahffaksfajeeubsne", "jefaa"]
Output: aksfaje
Input: ["aaffhkksemckelloe", "fhea"]
Output: affhkkse
Input: ["aabdccdbcacd", "aad"]
Output: aabd
Input: ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"]
Output: fafe
"""
def MinWindowSubstring(strArr):
    # code goes here
    str1 = [strArr[0]]
    str2 = [i for i in strArr[1]]
    contenders = set()
    winners = set()
    letters = []
    started = False
    for minuslength in range(len(str1[0])):
        str_work = str2.copy()
        letters.clear()
        if len(str1[0]) == minuslength:
            break
        for letter in str1[0][minuslength:]:
            if len(str_work) == 0:
                started = False
                break
            if letter in str_work and started:
                str_work.remove(letter)
                letters.append(letter)
                continue
            if started:
                letters.append(letter)
            if letter in str_work and not started:
                started = True
                str_work.remove(letter)
                letters.append(letter)

        contenders.add("".join(letters))

    for contender in contenders:
        contender_cpy = list(contender)
        is_winner = True
        for letter in str2:
            if letter not in contender_cpy:
                is_winner = False
            else:
                contender_cpy.remove(letter)
        if is_winner:
            winners.add(contender)

    return min(winners, key=len)

# keep this function call here
print(MinWindowSubstring(["aaffsfsfasfasfasfasfasfacasfafe", "fafe"]))