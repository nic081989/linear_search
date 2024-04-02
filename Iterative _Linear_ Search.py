# NAME:         Nicholas Ngobi
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a function `linear_search` that takes an
# unordered array of numbers as a parameter and
# a number to search for and returns the index of
# the number in the array, or -1 otherwise. Your
# search should be performed using a loop, rather
# than recursion. 
#The function iterates through each element in the array one by one
#if it finds  an element equal to the specified number n, it returns the index of that element.
# If the loop completes without finding the number, it retunrs -1 to indicate that the number is not present in the 
#array
# def linear_search(array, n) defines a function named linear_search that takes unordered array and a number to search for n as parameters
#For i in range (len(array)) starts a loop that iterates through the indices of the array using range function.
#If array[i] == n: this line checks if the current element at index i in the array is equal to the number n.
#retrun i: If the condition in the previous line is true, it means the number was found and the functon returns the index i
# If the ,loop completes  and the number is not found, return -1. If the loop completes and the function reaches this line, which returns -1 to indicate that the number was not found in the array.
def linear_search(array, num):
    for i in range (len(array)):
        if array[i] == num:
            return i
    return -1

def main():
    a = [45, 67, -2, 33, -44, 134, -67]
    print(a)
    for n in [1, 0, -1, 2, -2, 134, 67, -67]:
        print("%5d index? %d" % (n, linear_search(a, n)) )

main()
