from itertools import product

extraction = {"Programming Fundamentals": [["5:30-6:20", "TuThu"], ["1:30-:2:20", "MoWe"], ["10:30-11:20", "TuThu"]],
              "Engineering Mathematics": [["5:15PM - 6:30PM", "TuThu"], ["11:30AM - 12:45PM", "TuThu"], ["10:00AM - 11:15AM", "MoWe"]],
              "Data Structures 2": [["8:30AM - 9:45AM", "MoWe"], ["11:30AM - 12:45PM", "TuTh"]],
              "Calculus 2": [["3:30PM - 4:45PM", "TuTh"], ["8:30AM - 9:45AM", "TuTh"], ["10:00AM - 11:15AM", "TuTh"], ["10:00AM - 11:15AM", "MoWe"], ["5:15PM - 6:30PM", "TuTh"]],
              "Intro to Design and Media": [["3:30PM - 6:00PM", "MoWe"]]}

keys = list(extraction.keys())

# Quick sort in Python

# function to find the partition position


def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


size = len(keys)

quickSort(keys, 0, size - 1)

# print(keys)


# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


insertionSort(keys)
# print(keys)


courses = dict()
for i in keys:
    courses[i] = extraction[i]

# Binary Search in python


def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return array[mid]
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print("Enter the number of courses you want to choose: ")
numb = eval(input())

selected_courses = dict()
for i in range(numb):
    print("Enter the course you want to choose: ")
    course = input("")
    result = binarySearch(keys, course, 0, len(keys)-1)
    selected_courses[result] = courses[result]


# selected_courses = {"Data Structures 2": [["08:30AM", "09:45AM", "MoWe"], ["05:15PM", "06:30PM", "WeFr"], ["11:30AM", "12:45PM", "TuTh"]],
#               "Calculus 2": [["03:30PM", "04:45PM", "TuTh"], ["02:30PM", "03:45PM", "WeFr"], ["08:30AM", "09:45AM", "TuTh"], ["10:00AM", "11:15AM", "TuTh"], ["10:00AM", "11:15AM", "MoWe"], ["05:15PM", "06:30PM", "TuTh"]],
#               "Intro to Design and Media": [["03:30PM", "06:00PM", "MoWe"], ["02:30PM", "05:00PM", "WeFr"]]}

values = list(selected_courses.values())
permutations = list(product(*values))





def convert24(str1):
     
    # 08:30AM
         
    # remove the AM    
    if str1[-2:] == "AM":
        return str1[0:2] + str1[3:-2]
     
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[0:2] + str1[3:-2]
         
    else:
        # add 12 to hours and remove PM
        return str(int(str1[0:2]) + 12) + str1[3:5]
 
for i in permutations:
    print(i)

# for i in ((permutations)):
    # print(i)
    # s=[]
    # for k, l, m in i:
    #     s.append([k,l,m])
    #     print(s)
    # k=0
    # while True:
    #     n=1
    #     n2=0
    #     to=convert24(s[0][0])
    #     while True:
    #         a=convert24(s[n][n2])
    #         if a>
        # for k in i:
        #     for j in range(len(k)):
        #         print(permutations[i][j][k][0])
        #         a = permutations[i][j][k]
        #         a = convert24(a)
        #         print(a)
        #         permutations[i][0] = convert24(k)
        #         print(permutations[i][0])
        #         permutations[i][1] = convert24(l)
        #         print(k,l,m)

# print(permutations)


# for i in permutations:
#     print(i)