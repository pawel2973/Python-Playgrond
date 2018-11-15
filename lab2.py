# Lists
# Type the following lines at your Python interactive interpreter and see if they match what you expect:
########################################################################################################
print("LISTS")
print("-------------------------------------------------------------")
s = [0] * 3
s[0] += 1
print(s)

s = [''] * 3
s[0] += 'a'
print(s)

s = [[]] * 3
s[0] += [1]
print(s)

print("===================================")
listA = [1, 2, 3]
listB = listA
print("ID po przypisaniu\nSą takie same dla typów mutable i immutable logiczne\n===================================")
print("listaA: " + str(id(listA)))
print("listaA: " + str(id(listB)))
A = 8
B = A
print("int A:  " + str(id(A)))
print("int B:  " + str(id(B)))

print("===================================")
print(
    "ID po działaniu +=\nDla typów mutable są takie same\nDla typów immutable są różne\n===================================")
listA += [1]
A += 7
print("listaA: " + str(id(listA)))
print("listaA: " + str(id(listB)))
print("int A:  " + str(id(A)))
print("int B:  " + str(id(B)))

"""
    1# Python variables don't store values directly they store references to objects.
    
    Mutable obj:    Meaning you can change their content without changing their identity(change the object in-place).
        >> list, set, dict
    Immutable obj:  Can not be change. Changing content equals changing identity.
        >> bool, int, float, complex, tuple, str, frozenset

    -----------------
        About +=
    -----------------
    If the object is mutable then it is encouraged (but not required) to perform the modification in-place. 
    So a points to the same object it did before but that object now has different content.
    
    If the object is immutable then it obviously can't perform the modification in-place. 
    Some mutable objects may also not have an implementation of an in-place "add" operation. 
    In this case the variable "a" will be updated to point to a new object containing the result of an addition operation.

    Technically this is implemented by looking for __IADD__ first, if that is not implemented then __ADD__ is tried and finally __RADD__.
    
    a += b is essentially the same as a = a + b, except that:
      +  always returns a newly allocated object, 
      += should (but doesn't have to) modify the object in-place if it's mutable.
      In a = a + b, a is evaluated twice. 

    Whenever you assign a variable to another variable of mutable data type, any changes to the data are reflected by both variables. 
    The new variable is just an alias for the old variable. This is only true for mutable data types.
"""

# Tuples
# Write a function to compute the GCD of two numbers.
########################################################################################################

print("\n\nTUPLES")
print("-------------------------------------------------------------")


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


print("gcd(10, 25): " + str(gcd(10, 25)))  # => 5
print("gcd(14, 15): " + str(gcd(14, 15)))  # => 1
print("gcd(9, 3): " + str(gcd(3, 9)))  # => 3
print("gcd(1, 1): " + str(gcd(1, 1)))  # => 1

print("\n\nDICTIONARIES")
print("-------------------------------------------------------------")

our_dict = {
    "CA": "US",
    "NY": "US",
    "ON": "CA"
}


def flip_dict(input_dict):
    inv_map = dict()
    for key, val in input_dict.items():
        inv_map.setdefault(val, set())
        inv_map[val].add(key)
    return inv_map


print(flip_dict(our_dict))

"""
    >> In for loop we have an access to old key and its value.
    >> The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
    >> Our default value is the collection constructor, so when we have situation when key = key method setdefault() do nothing, only can show value of key
    >> We use add() method to add element to set    
"""

print("\n\nCOMPREHENSIONS")
print("-------------------------------------------------------------")

# [0, 1, 2, 3] -> [1, 3, 5, 7]
list1a = [0, 1, 2, 3]
list1b = [list1a[i] + i + 1 for i in range(len(list1a))]
print("{0} -> {1}".format(list1a, list1b))

# [3, 5, 9, 8] -> [True, False, True, False]
list2a = [3, 5, 9, 8]
list2b = [i % 3 == 0 for i in list2a]
print("{0} -> {1}".format(list2a, list2b))

# ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"] -> ["sam", "guido"]
list3a = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
list3b = [i.lstrip("TA_") for i in list3a if i.startswith("TA_")]
print("{0} -> {1}".format(list3a, list3b))

# ['apple', 'orange', 'pear'] -> ['A', 'O', 'P']
list4a = ['apple', 'orange', 'pear']
list4b = [i[0].upper() for i in list4a]
print("{0} -> {1}".format(list4a, list4b))

# ['apple', 'orange', 'pear'] -> ['apple', 'pear']
list5a = ['apple', 'orange', 'pear']
list5b = [list5a[i] for i in range(len(list5a)) if i == 0 or i == len(list5a) - 1]
print("{0} -> {1}".format(list5a, list5b))

# ['apple', 'orange', 'pear'] -> [ ('apple', 5), ('orange', 6), ('pear', 4) ]
list6a = ['apple', 'orange', 'pear']
list6b = [tuple([i, len(i)]) for i in list6a]
print("{0} -> {1}".format(list6a, list6b))

# ['apple', 'orange', 'pear'] -> {'apple': 5, 'orange': 6, 'pear': 4}
list7a = ['apple', 'orange', 'pear']
dict7b = {i: len(i) for i in list7a}  # dict_variable = {key:value for (key,value) in dictonary.items()}
# list7b = [dict([(i, len(i))]) for i in list7a]
print("{0} -> {1}".format(list7a, dict7b))


# Cyclone Phrases (challenge)
# Cyclone words are words that have a sequence of characters in alphabetical order when following a cyclic pattern.
########################################################################################################

print("\n\nCyclone Phrases (challenge)")
print("-------------------------------------------------------------")


def is_cyclone_phrase(word):
    word = word.split(" ")
    print("========================\n" + str(word) + "\n========================")

    # situation when word = ""
    if len(word) == 1:
        if len(word[0]) == 0:
            return True

    is_cyclone_word = True
    for z in range(len(word)):
        id_x = 0
        id_y = len(word[z]) - 1
        i = 0

        while id_x != id_y:
            print(word[z][id_x] + " -> " + word[z][id_y])
            if word[z][id_x] > word[z][id_y]:
                is_cyclone_word = False

            temp_y = id_y

            if i % 2 == 0:
                id_y = id_x + 1
                id_x = temp_y
            else:
                id_y = id_x - 1
                id_x = temp_y
            i = i + 1
        if not is_cyclone_word:
            return False
        print("")
    return True


print(is_cyclone_phrase("adjourned"))  # => True
print(is_cyclone_phrase("settled"))  # => False
print(is_cyclone_phrase("all alone at noon"))  # => True
print(is_cyclone_phrase("by myself at twelve pm"))  # => False
print(is_cyclone_phrase("acb"))  # => True
print(is_cyclone_phrase(""))  # => True

"""
    How algorithm works:
    --------------------
    word = "abcdef"
    id:     012345
    --------------------
         id_x | id_y
(0)         0 |  5  # id_x = id_y(0), id_y = id_x(0) + 1, at end of loop: id_x = 5, id_y = 1 
(1)         5 |  1  # id_x = id_y(1), id_y = id_x(1) - 1, at end of loop: id_x = 1, id_y = 4   
(2)         1 |  4  # id_x = id_y(2), id_y = id_x(2) + 1, at end of loop: id_x = 2, id_y = 3
(3)         2 |  3  # id_x = id_y(3), id_y = id_x(3) - 1, at end of loop: id_x = 4, id_y = 2
(4)         4 |  2  # id_x = id_y(4), id_y = id_x(4) + 1, at end of loop: id_x = 3, id_y = 3
(5)         3 |  3  # STOP: while (id_x != id_y) 
        
    if (i % 2 == 0)  # Decide what equation we use:    
        id_y = id_x + 1
            or
        id_y = id_x - 1
"""


# Pascal's Triangle
# Write a function that generates the next level of Pascal's triangle given a list that represents a valid row of Pascal’s triangle.
########################################################################################################

print("\n\nPascal's Triangle")
print("-------------------------------------------------------------")

def generate_pascal_row(row):
    l_zero = [0] + row
    r_zero = row + [0]
    return [x + y for x, y in zip(l_zero, r_zero)]
print(list(generate_pascal_row([1,2,1])))
