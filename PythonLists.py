#Python Lists

#List is used to store multiple items of single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#Create list:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

#Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#List Items - Data Types
#List can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3]
list3 = [True, False, True]
list4 = ["cherry", 45, True, 25, "male"]

print(list1)
print(list2)
print(list3)
print(list4)


#type()
#From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) #note the duble round-brackets
print(thislist)


#Python Collections
""""
There are four collection data types in the Python programming language
 - List is a collection which is a ordered and changeable. Allows duplicate members.
 _ Tuple is a collection which is ordered and unchangeable, Allows duplicate members.
 - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 - Dictionary is a collection which is ordered** and changeable. No duplicate members.
 
 *Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""


#Python - Access List Items
#List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
"""
Negative indexing means start form the end
-1 reefers to the last item, -2 refers to the second item etc.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Range of Indexes
"""
You can specify of indexes by specifying where to start to end the range.
When specifying a range, the return value will be a new list with the specified items.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#First item has index 0

thislist = ["apple", "banana", "orange", "cherry", "kiwi", "melon", "mango"]
print(thislist[:4])

#By leaving out the end value, the range will go to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of negative indexes
"""
Specify negative indexes if you want to start the search from the end of the list:
This example returns the items from "orange" (-4) to, but NOT include "mango" (-1):
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exist
"""
To determine if a specified item is present in a list use the in keyword:
Check if "apple" is present in the list.
"""

thislist = ["apple", "mango", "orange"]
if "apple" in thislist:
    print("Yes 'apple is in the fruits list.")


#Python - Change List Items

#Change Item Value
"""
To change the value of a specific item, refer to the index number:
Change the second item:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Items Values
"""
To change the values of items within a specific range, define a list with a new values,
and refer to the range of index numbers where you want to insert the new values:
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermalon":
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

"""
If you insert more items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:
Change the second value by replacing it with two new values:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#Note: The length of the list will change when the number of items inserted does not match the number of items replaced.


"""
If you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:
Change the second and third value by replacing it with one value:
"""

thislist = ["appple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#Insert Items
"""
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
Insert "watermelon" as the third item:
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Python - Add List Items
"""
Append Itmes
To add item to the end of the list, use append() method:
Use the append() method to append an item:
"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Insert Items
"""
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

Insert the item as the second position:
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
"""
To append elements from another list to the current list, use the extend() method.

Add the elements of tropical to thislist:
"""

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#The elements will be added to the end of the list.

#Add Any Iterable
"""
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Add elements of a tuple to a list:
"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#Python - Remove List Items

"""
Remove Specified Item

The remove() method removes the specified item.

Remove banana:
"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""
If there are more than one item with the specified value, the remove() method removes the first occurrence:

Remove the first occurrence of "banana":
"""

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
"""
The pop() method removes the specified index

Remove the second item:
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

"""
If you do not specify the index, the pop() method removes the last item.

Remove the last item:
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

"""
The del keyword also removes the specified index:

Remove the first item:
"""

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print (thislist)

"""
del also can delete completely:

Delete the entire list:
"""

thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
"""
The clear() method emptys the list.

The list still remains, but it has no content.

Clear the list content:
"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Python Loops Lists
"""
Loop through a List

You can through the list items by using a for loop:

Print all items in the list, one by one:
"""

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Loop through the Index Nembers
"""
You can also loop through the list items by referring th their index number.
 
Use the range() and len() functions to create a suitable iterable.

Print all items by referring to their index number:
"""

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Usinf a While Loop
"""
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through
the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

Print all items, using a while loop to go through all the index numbers
"""
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping Using Lists Comprehension
"""
List Comprehension offers the shortest syntax for looping through lists:

A short hand for loop that will print items in a list:
"""

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#Python - List Comprehension
#List Comprehension
"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The Syntax
"""
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.
"""

#Condition
"""
The condition is like a filter that only accepts the items that evaluate to True.

Only accept items that are not "apple":
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

"""
The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted:

With no if statements:
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

"""
Iterable
The iterable can be any iterable object, like a list, tuple, set etc.

You can use the range() function to create an iterable:
"""
newlist = [x for x in range(10)]
print(newlist)

#Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]
print(newlist)

"""
The expression is the current item in the iteration, but it is also the outcome,
which you can manipulate before it ends up like a list item in the new list:

Set a values in a new list to upper case:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#You can set the outcome to whatever you like:
#Set all values in the new list to 'hello':

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

"""
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

Return "orange" instead of "banana":
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
"""
The expression in the example above says:

"Return the item if it is not banana, if it is banana return orange".
"""


#Python - Sorts Lists
"""
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Sort the list alphabetically:
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 23, 65, 82, 50]
thislist.sort()
print(thislist)

#Sort Descending
"""
To sort descending, use the keyword argument reverse = True:

Sort the list descending:
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 18]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
"""
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Sort the list based on how close the number is to 50:
"""

def myFunc(n):
    return abs(n - 50)

thislist = [100, 50, 82, 65, 23]
thislist.sort(key = myFunc)
print(thislist)

#Case Insensitive Sort
"""
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

Case sensitive sorting can give an unexpected result:
"""
thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)

"""
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

Perform a case-insensitive sort of the list:
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

#Reverse Order
"""
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

Reverse the order of the list items:
"""
thislist = ["banana", "Kiwi", "Orange", "cherry"]
thislist.reverse()
print(thislist)


#Python - Copy Lists
#Copy a List
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
and changes made in list1 will automatically also be made in list2.
"""

#Use a copy() method
"""
You can use the build-in List method copy() to copy a list.

Make a copy of a list with the copy() method:
"""
thislist = ["apple", "banana", "cherry"]
myList = thislist.copy()
print(myList)

#Use a list() method
"""
Another way to make a copy is to use the built-in method list().

Make a copy of a list with the list() method:
"""
thislist = ["apple", "banana", "cherry"]
myList = list(thislist)
print(myList)

#Use the slice Operator
"""
You can also make a copy of a list by using the : (slice) operator.

Make a copy of a list with the : operator:
"""
thislist = ["apple", "banana", "cherry"]
myList = thislist[:]
print(myList)


#Python - Join List
#Join Two Lists
"""
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Join two list:
"""
list1 = ["a,", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

"""
Another way to join two lists is by appending all the items from list2 into list1, one by one:

Append list2 into list1:
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

"""
Or you can use the extend() method, where the purpose is to add elements from one list to another list:

Use the extend() method to add list2 at the end of list1:
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


#Python - List Methods

"""
append()
- Adds elements at the end of the list.
"""
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

"""
clear()
- Removes all elements of the list.
"""
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

"""
copy()
- Returns a copy of the list.
"""
fruits = ["apple", "banana", "cherry", "orange"]
x = fruits.copy()
print(x)

"""
count()
- Returns the number of elements with the specified value.
"""
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

points = [1, 2, 3, 4, 5, 9, 8, 7, 9, 3]
x = points.count(9)
print(x)

"""
extend()
Add the elements of a list (or any iterable), to the end of the current list.
"""
fruits = ["apple", "banana", "cherry"]
cars = ["Volvo", "BMW", "Ford"]

fruits.extend(cars)
print(fruits)

#Exercise with Tuple and List
fruits = ["apple", "banana", "cherry"]
points = (1, 2, 3, 4, 9, 5)

fruits.extend(points)
print(fruits)

"""
index()
Returns the index of the first element with the specified value.
"""
fruits = ["apple", "banana", "cherry"]
x = fruits.index("apple")

print(x)

numbers = [10, 55, 67, 32, 5, 82, 47]
x = numbers.index(47)
print(x)

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)

"""
insert()
Adds an element at the special position
"""
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)

"""
pop()
Removes the elements at the specified position.
"""
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)

#Return the removed element
fruits = ["apple", "banana", "cherry"]
x = fruits.pop(1)
print(x)

"""
remove()
Removes item with the specified value.
"""
fruits = ["apple", "banana", "cherry"]
fruits.remove("cherry")
print(fruits)

"""
reverse()
Reverses the order of the list.
"""
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

"""
sort()
Sorts the list
"""
cars = ["Ford", "BMW", "Volvo"]
cars.sort()
print(cars)

cars = ["Volvo", "BMW", "Ford"]
cars.sort(reverse = True)
print(cars)

#A function that returns the length of the value:
def myFunc(e):
    return len(e)

cars = ["Ford", "Mitsubishi", "BMW", "VW"]

cars.sort(key=myFunc)
print(cars)

#A function that will returns the 'year' value:
def myFunc(e):
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'BMW', 'year': 2008},
    {'car': 'VW', 'year': 2010},
    {'car': 'Mitsubishi', 'year': 1999}
]

cars.sort(key=myFunc)
print(cars)

#A function that returns the length of the value:
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)

#Code Challenge
"""
Inside the editor, complete the following steps:
Create a list called colors with the values "red", "green", "blue"
Print the first item in the list
Change the second item to "yellow"
Add "purple" to the end of the list using append()
Remove "red" from the list using remove()
Print the list
"""

colors = ["red", "green", "blue"]

print(colors[0])

colors[1] = "yellow"
colors.append("purple")
colors.remove("red")

print(colors)


#Exercise 1
foods = ["pizza", "burger", "pasta"]

print(foods)


#Exercise 2
colors = ["red", "blue", "green"]

print(colors[0])
print(colors[2])


#Exercise 3
cars = ["BMW", "Audi", "Mercedes"]

cars[1] = "Toyota"
print(cars)


#Exercise 4
numbers = [1, 2, 3]

numbers.append(4)
print(numbers)


#Exercise 5
animals = ["cat", "dog", "bird"]

animals.remove("dog")
print(animals)


#Exercise 6
students = ["Ivan", "Maria", "Peter", "Anna"]

print(len(students))


#Exercise 7
fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Banana is on the list.")
else:
    print("Banana is not on the list.")


#Exercise 8
games = ["CS2", "Minecraft", "FIFA"]

for game in games:
    print(game)


#Exercise 9 (BONUS)
animals = ["dog", "cat", "bear"]
numbers = [1, 2, 3]
float_numbers = [3.14, 2.71, 4.15]
booleans = [True, False, True]

general_sheet = animals + numbers + float_numbers + booleans

print(general_sheet)


#Exercise 10 (BONUS)
menu = ["Pizza", "Pasta", "Burger"]


print("--- MENU ---")
print(" ")

print("1.", menu[0])
print("2.", menu[1])
print("3.", menu[2])


#Overall - 6.00