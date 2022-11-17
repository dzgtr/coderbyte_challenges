"""Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain
pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and
the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"],
then this forms the following tree:
4
|
2
|\
1 7

which you can see forms a proper binary tree. Your program should, in this case, return the string true because
a valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs,
then return the string false. All of the integers within the tree will be unique, which means there can only be
one node in the tree with the given integer value.
"""
import re

def TreeConstructor(strArr):
    # code goes here

    new_array = []
    parents = {}
    children = set()
    for item in strArr:
        newitem = re.sub("[()]", "", item)
        new_array.append(newitem.split(","))
    for item in new_array:
        if item[0] not in children:
            children.add(item[0])
        else:
            return False

        if item[1] not in parents:
            parents[item[1]] = 1
        else:
            parents[item[1]] += 1
        if parents[item[1]] > 2:
            return False
    if len(parents) > len(children):
        return False
    return True

# keep this function call here
print("Should be true:")
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))
print("Should be false:")
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))
print(TreeConstructor(["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)", "(1,9)"]))
print(TreeConstructor(["(2,5)", "(2,6)"]))