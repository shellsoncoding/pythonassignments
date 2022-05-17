# 1.Reverse a list in Python
lst1 = [5, 8, 9, 10, 3, 1, 6]
print(f"Original List :{lst1}")
lst2 = []
length = len(lst1)
while length > 0:
    lst2.append(lst1[length - 1])
    length = length - 1
print(f"Reversed List :{lst2}")
print("-" * 40)
# 2.Concatenate two lists index - wise
lst1 = ['h', 'l', 'o']
print(f"list1 :{lst1}")
lst2 = ['e', 'l', '.']
print(f"list2 :{lst2}")
lst3 = [i + j for i, j in zip(lst1, lst2)]
for k in lst3:
    print(k, end='')
print()
print("-" * 40)
# 3.Turn every item of a list into its square
lst = [11, 52, 33, 4, 5, 6, 7]
print(f"List :{lst}")
res = []
for i in lst:
    res.append(i * i)
print(f"Result :{res}")
print("-" * 40)
# 4.Concatenate two lists in the following order
lst1 = ["Hello ", "Let's "]
lst2 = ["Learn", "Java"]

res = [x + y for x in lst1 for y in lst2]
print(res)
print("-" * 40)
# 5.Iterate both lists simultaneously
lst1 = [10, 20, 30, 40]
lst2 = [100, 200, 300, 400]

for x, y in zip(lst1, lst2):
    print(x, y)
print("-" * 40)

# 6.Remove empty strings from the list of strings
lst1 = ["Run", "", "over", "here", "", ""]
res = []
for ls in lst1:
    if ls == "":
        continue
    else:
        res.append(ls)
print(res)
print("-" * 40)

# 7. Add new item to list after a specified item
lst1 = [10, 20, [30, 40, [50, 60], 50], 30, 40]

lst1[2][2].append(70)
print(lst1)
print("-" * 40)

# 8.Extend nested list by adding the sublist
lst1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
res = ["h", "i", "j"]

lst1[2][1][2].extend(res)
print(lst1)
print("-" * 40)

# 9.Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)

list1[index] = 200
print(list1)
print("-" * 40)
# 10. Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]


def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]


res = remove_value(list1, 20)
print(res)
print("-" * 40)


# 11. Sort a list using the following technique
#
# 1. Bubble Sort
def bubble_sort(arr_list):
    # Outer loop for traverse the entire list
    for i in range(0, len(arr_list) - 1):
        for j in range(len(arr_list) - 1):
            if arr_list[j] > arr_list[j + 1]:
                temp = arr_list[j]
                arr_list[j] = arr_list[j + 1]
                arr_list[j + 1] = temp
    return arr_list


list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
print("The bubble-sorted list is: ", bubble_sort(list1))
print("-" * 40)


# 2. Merge Sort
def mergeSort(arr_list):
    if len(arr_list) > 1:
        a = len(arr_list) // 2
        l = arr_list[:a]
        r = arr_list[a:]

        mergeSort(l)
        mergeSort(r)
        b = c = d = 0

        while b < len(l) and c < len(r):
            if l[b] < r[c]:
                arr_list[d] = l[b]
                b += 1
            else:
                arr_list[d] = r[c]
                c += 1
            d += 1

        while b < len(l):
            arr_list[d] = l[b]
            b += 1
            d += 1

        while c < len(r):
            arr_list[d] = r[c]
            c += 1
            d += 1


def printList(arr_list):
    for i in range(len(arr_list)):
        print(arr_list[i], end=" ")
    print()


lst = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print("The unsorted list is :", lst)
mergeSort(lst)
print("The merge-sorted list is: ", lst)
print("-" * 40)
# 3. Insertion Sort
list1 = [10, 1, 5, 2, 6, 8, 7, 3, 11, 4]
print("The unsorted list is :", list1)
i = 1
while i < 10:
    element = list1[i]
    j = i
    i = i + 1

    while j > 0 and list1[j - 1] > element:
        list1[j] = list1[j - 1]
        j = j - 1

    list1[j] = element

print("The insertion-sorted list is: ", list1)
print("-" * 40)


# 4. Shell Sort
def shell_sort(my_list, list_len):
    interval = list_len // 2
    while interval > 0:
        for i in range(interval, list_len):
            temp = my_list[i]
            j = i
            while j >= interval and my_list[j - interval] > temp:
                my_list[j] = my_list[j - interval]
                j -= interval
            my_list[j] = temp
        interval //= 2


list1 = [45, 31, 62, 12, 89, 5, 9, 8]
l = len(list1)
print("The unsorted list is :", list1)
shell_sort(list1, l)
print("The shell-sorted list is :", list1)
print("-" * 40)


# 5. Selection Sort

def SelectionSort(myList):
    for i in range(len(myList) - 1):
        minimum = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[minimum]:
                minimum = j
        if minimum != i:
            myList[i], myList[minimum] = myList[minimum], myList[i]
    return myList


listItems = [4, 5, 3, 7, 4, 6, 2, 8]
print("The unsorted list is :", listItems)
print('The selection-sorted list is :', SelectionSort(listItems))

print("-" * 40)

# 12. Compare two list and find
# a.duplicates
# b.unique
#  from
# 1.list - 1
# 2.list - 2
my_list = ['a', 'b', 'c', 'b', 'c', 'c']
print("List :", my_list)
print("Duplicates :\t")
print(set([x for x in my_list if my_list.count(x) > 1]))


def unique(lst1):
    unique_list = []
    for x in lst1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x, end=" ")


list1 = [10, 20, 10, 30, 40, 40]
print("The list :", list1)
print("The Unique values from list is :")
unique(list1)
print()

print("-" * 40)
# 13. Write a Python program to sum all the items in a list.
num = [45, 70, 12, 34, 21, 56]
s = 0
for n in num:
    s += n
print("Sum of elements in given list is :", s)
print("-" * 40)
# 14. Write a Python program to multiply all the items in a list.
num = [45, 70, 12, 34, 21, 56]
m = 1
for n in num:
    m *= n
print("Product of elements in given list is :", m)
print("-" * 40)
# 15. Write a Python program to get the
# 			a. largest number
num = [100, 2, 300, 10, 11, 1000]
print("List is :", num)
largest_number = 0

for n in num:
    if n > largest_number:
        largest_number = n

print("The largest element is :", largest_number)
# 			b. second largest number
list1 = [100, 2, 300, 10, 11, 1000]
print("Second largest element is :", sorted(list1)[-2])
# 			c. smallest number
num = [100, 2, 300, 10, 11, 1000]
smallest_number = num[0]

for n in num:
    if n < smallest_number:
        smallest_number = n

print("The smallest element is :", smallest_number)
# 			d. second smallest number
list1 = [100, 2, 300, 10, 11, 1000]
print("Second smallest element is :", sorted(list1)[1])
print("-" * 40)


# 16.  Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# Python program to flatten a nested list
def flattenList(nestedList):
    if not (bool(nestedList)):
        return nestedList

    if isinstance(nestedList[0], list):
        return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])

    return nestedList[:1] + flattenList(nestedList[1:])


nestedList = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print('Nested List:\n', nestedList)

print("Flattened List:\n", flattenList(nestedList))
print("-" * 40)
# 17. Write a Python program to remove consecutive duplicates of a given list.
# Original list: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
from itertools import groupby

test_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

print("The original list is : " + str(test_list))
res = [i[0] for i in groupby(test_list)]
print("The list after removing consecutive duplicates : " + str(res))
print("-" * 40)

# Dictionaries
# ------------
# 1. Convert two lists into a dictionary
ListKeys = ["James", "Tom", "Holly"]
ListValues = [10, 25.2, 50]
myDict = {}
d = 0
for i in ListKeys:
    myDict[i] = ListValues[d]
    d += 1
print("Dictionary after conversion is: " + str(myDict))
print("-" * 40)


# 2. Merge two Python dictionaries into one
def merge_two_dicts(x, y):
    return y.update(x)


x = {'a': 11, 'b': 21}
y = {'b': 32, 'c': 4}
merge_two_dicts(x, y)
print("Merged dictionary")
print(y)
print("-" * 40)
# 3. Print the value of key ‘history’ from the below dict
sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
print("history :", sampleDict['class']['student']['marks']['history'])
print("-" * 40)
# 4. Initialize dictionary with default values
employees = ['John', 'Cain']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)
print(res["John"])
print("-" * 40)
# 5. Create a dictionary by extracting the keys from a given dictionary
sampleDict = {"name": "John", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)
print("-" * 40)
# 6. Delete a list of keys from a dictionary
sample_dict = {"name": "John", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
print("-" * 40)
# 7. Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')
print("-" * 40)
# 8. Rename key of a dictionary
sample_dict = {"name": "John", "age": 25, "salary": 8000, "city": "New york"}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
print("-" * 40)
# 9. Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))
print("-" * 40)
# 10. Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)
print("-" * 40)
# 11. Write a Python program to iterate over dictionaries using for loops.
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)
print("-" * 40)
# 12. Write a Python program to sort a given dictionary by key.
color_dict = {'4': 'yellow',
              '1': 'white',
              '3': 'green',
              '2': 'blue'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
print("-" * 40)
# 13. Write a Python program to remove duplicates from Dictionary.

test_dict = {'python': 10, 'is': 15, 'best': 20, 'language': 10, 'now': 20}

print("The original dictionary is : " + str(test_dict))
temp = []
res = dict()
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print("The dictionary after values removal : " + str(res))

print("-" * 40)
# 14. Write a Python program to combine two dictionary adding values for common keys.
# 	d1 = {'a': 100, 'b': 200, 'c':300}
# 	d2 = {'a': 300, 'b': 200, 'd':400}
# 	Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
for key in d2:
    if key in d1:
        d2[key] = d2[key] + d1[key]
    else:
        pass

print(d2)
print("-" * 40)


# 15. A Python Dictionary contains List as value. Write a Python program to clear the list values in the said
# dictionary. Original Dictionary: {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]} Clear the list values in
# the said dictionary:{'C1': [], 'C2': [], 'C3': []}
def test(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary


dictionary = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
print("Original Dictionary:")
print(dictionary)
print("Clear the list values in the said dictionary:")
print(test(dictionary))
print("-" * 40)


# 16. Write a Python program to extract a list of values from a given list of dictionaries.
#
# Original Dictionary:[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]

# Original Dictionary:[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math[90, 89, 92]
def test(lst, marks):
    result = [d[marks] for d in lst if marks in d]
    return result


marks = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

print("Original Dictionary:", marks)
subj = "Science"
print("Extract a list of values from said list of dictionaries where subject =", subj)
print(test(marks, subj))

print("Original Dictionary:")
print(marks)
subj = "Math"
print("Extract a list of values from said list of dictionaries where subject =", subj)
print(test(marks, subj))

print("-" * 40)


# 17. Write a Python program to find the length of a given dictionary values.
#
# Original Dictionary:{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values: {'red': 3, 'green': 5, 'black': 5, 'white': 5}
#
# Original Dictionary:{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:{'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}
def test(dictt):
    result = {}
    for val in dictt.values():
        result[val] = len(val)
    return result


color_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print("Original Dictionary:")
print(color_dict)
print("Length of dictionary values:")
print(test(color_dict))

color_dict = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
print("Original Dictionary:")
print(color_dict)
print("Length of dictionary values:")
print(test(color_dict))
print("-" * 40)
