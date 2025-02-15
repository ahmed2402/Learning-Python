# Write a recursive function to calculate the sum of first n natural numbers.

# def sum(n):
#     if( n == 0):
#         return 0
#     return sum(n-1) + n

# SUM = sum(5)
# print(SUM)

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def printList(list, idx = 0):
    if(idx == len(list)):
       return 0
    print(list[idx])
    printList(list,idx+1)


list = [1,2,3,4,5,6,7,4]
printList(list)