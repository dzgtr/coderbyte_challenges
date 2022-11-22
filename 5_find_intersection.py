"""
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order,
the second element will represent a second list of comma-separated numbers (also sorted).
Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order.
If there is no intersection, return the string false. """

def FindIntersection(strArr):

    # code goes here
    intersection = []
    list1 = strArr[0].split(", ")
    list2 = strArr[1].split(", ")
    for x in range(len(list1)):
      for y in range(len(list2)):
        if list1[x] == list2[y]:
          intersection.append(list1[x])
    result = ",".join(intersection)
    if result == "":
        return "false"
    else:
        return result

# keep this function call here
print(FindIntersection(["1, 2, 3, 4, 5", "6, 7, 8, 9, 10"]))
#print(FindIntersection(input()))