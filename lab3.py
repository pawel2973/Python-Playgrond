#Familiar Functions
#Write at least two more instances of function calls,
# not listed above, and predict their output. Are they valid or invalid? Check your hypothesis.

def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))

# Valid or invalid?
#print_two()
print_two(4, 1)
#print_two(41)
#print_two(a=4, 1)
#print_two(4, a=1)
#print_two(4, 1, 1)
#print_two(b=4, 1)
print_two(a=4, b=1)
print_two(b=1, a=4)
#print_two(1, a=1)
#print_two(4, 1, b=1)

print_two("4","1")
print_two([],{})
#print_two(,)
print_two(4,b=1)

#Default Arguments
def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

keyword_args(5)
keyword_args(a=5)
keyword_args(5, 8)
keyword_args(5, 2, c=4)
keyword_args(5, 0, 1)
keyword_args(5, 2, d=8, c=4)
#keyword_args(5, 2, 0, 1, "")
#keyword_args(c=7, 1)
keyword_args(c=7, a=1)
keyword_args(5, 2, [], 5)
#keyword_args(1, 7, e=6)
keyword_args(1, c=7)
#keyword_args(5, 2, b=4)

#keyword_args()
keyword_args("4")

#Exploring Variadic Argument lists
def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

variadic(2, 3, 5, 7)
variadic(1, 1, n=1)
#variadic(n=1, 2, 3)
variadic()
variadic(cs="Computer Science", pd="Product Design")
#variadic(cs="Computer Science", cs="CompSci", cs="CS")
variadic(5, 8, k=1, swap=2)
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})

variadic(1, 2, *[3, 4, 5],a=6, **{'n':0, 'm':1})
variadic(None)

#Optional: Putting it all together

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

#all_together(2)
all_together(2, 5, 7, 8, indent=False)
all_together(2, 5, 7, 6, indent=None)
#all_together()
#all_together(indent=True, 3, 4, 5)
#all_together(**{'indent': False}, scope='maximum')
all_together(dict(x=0, y=1), *range(10))
#all_together(**dict(x=0, y=1), *range(10))
#all_together(*range(10), **dict(x=0, y=1))
all_together([1, 2], {3:4})
#all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})
all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})

all_together(0,0,**{"test":"yes", "a":"b"})
all_together(*[1,2])

#
print()
#Writing Functions
#speak_excitedly

def speak_excitedly(msg, i=1, cap=False):
    if cap:
        print(msg.upper()+i*'!')
    else:
        print(msg+i*'!')

speak_excitedly("I love python")
speak_excitedly("Keyword arguments are great",4)
speak_excitedly("I guess Java is okay...",i=0)
speak_excitedly("Let's go Stanford",2,True)

#
print()
#average
#Write a function average that accepts a variable number of integer positional arguments
# and computes the average. If no arguments are supplied, the function should return None.

def average(*args):
    if len(args) == 0:
        return None
    else:
        return sum(args)/len(args)

print(average())
print(average(5))
print(average(6, 8, 9, 11))

list = [0,1,2,3,4,5,6,7,8,9,10]
print(average(*list))

#
print()
#Challenge: make_table
def make_table(key_justify='left',value_justify='right',**kwargs):
    #l=max(len(value)+len(key) for key,value in kwargs.items()) # najdluzszy ciag znakow w naszych kwargs
    l1=max(len(key) for key in kwargs) # najdluzszy element key
    l2=max(len(value) for key,value in kwargs.items()) # najdluzszy value element
    print("="*(l1+l2+7))

    #<, > , ^ setting allinging format
    def just(x):
        return {
        'left':'<',
        'right':'>',
        'center':'^'
        }.get(x,'<') # domyslnie <
    ky = just(key_justify)
    vj = just(value_justify)

    for key, value in kwargs.items():
        print("| {:{}{}} | {:{}{}} |".format(key,ky,l1,value,vj,l2))
    print("=" * (l1 + l2 + 7))


make_table(
    first_name="Sam",
    last_name="Redmond",
    shirt_color="pink"
)
make_table(
    key_justify="right",
    value_justify="center",
    song="Style",
    artist_fullname="Taylor $wift",
    album="1989"
)
make_table(
    key_justify="left",
    value_justify="center",
    movie="Interstellar",
    director="Christopher Nolan",
    year="2014"
)

#
print()
#Function Nuances
#Predict the output of the following code snippet. Then, run the code to check your hypothesis.

def say_hello():
    print("Hello!")

print(say_hello())

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())
print(echo(5))
print(echo("Hello"))

def drive(has_car):
    if not has_car:
        return
    return 100  # miles

print(drive(False))
print(drive(True))

#
print()
#Parameters and Object Reference
def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1)
    print("Inside append_one: arr = {}".format(arr))

l = [4]
print("Before reassign: arr={}".format(l))
reassign(l)
print("After reassign: arr={}".format(l))

l = [4]
print("Before append_one: arr={}".format(l))
append_one(l)
print("After append_one: arr={}".format(l))

#
print()
#Scope
# Case 1
x = 10

def foo():
    print("(inside foo) x:", x) #10
    y = 5
    print('value:', x * y) #50

print("(outside foo) x:", x) # 10
foo()
print("(after foo) x:", x) #10

# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x) # 8
    y = 5
    print('value:', x * y) # 40

print("(outside foo) x:", x) # 10
foo()
print("(after foo) x:", x) # 10

#UnboundLocalError
"""
x = 10

def foo():
    print("(inside foo) x:", x)  # We swapped this line
    x = 8                        # with this one
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)

lst = [1,2,3]
def foo():
    lst.append(4)
foo()

lst = [1,2,3]
def foo():
    lst = lst + [4]
foo()
"""

#Default Mutable Arguments - A Dangerous Game
x = 5

def square(num=x):
    return num * num

x = 6
print(square())   # => 25, not 36
print(square(x))  # => 36


def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst


# Works well when the keyword is provided
append_twice(1, lst=[4])  # => [4, 1, 1]
append_twice(11, lst=[2, 3, 5, 7])  # => [2, 3, 5, 7, 11, 11]

# But what happens here?
print(append_twice(1))
print(append_twice(2))
print(append_twice(3))

def append_twice2(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    lst.append(a)
    return lst
print(append_twice2(1))
print(append_twice2(2))
print(append_twice2(3))

def fib(n, cache={0: 1, 1: 1}):
   if n in cache:  # Note: default value captures our base cases
       return cache[n]
   out = fib(n-1) + fib(n-2)
   cache[n] = out
   return out

print(fib(1))
print(fib(7))
print(fib(7))

#Investigating Function Objects
#Default Values (__defaults__ and __kwdefaults__)
def all_together(x, y,z=1,  *nums, indent=True, spaces=4, **options): pass

print(all_together.__defaults__)  # => (1, )
print(all_together.__kwdefaults__ ) # => {'indent':True, 'spaces':4}

#Documentation (__doc__)
def my_function():
    """Summary line: do nothing, but document it.

    Description: No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)
# Summary line: Do nothing, but document it.
#
#     Description: No, really, it doesn't do anything.
def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """A useless comment"""
    print(x + y * z)
    print(sum(nums))
    for k, v in options.items():
        if indent:
            print("{}\t{}".format(k, v))
        else:
            print("{}{}{}".format(k, " " * spaces, v))


code = all_together.__code__
print(code.co_consts,code.co_names,code.co_varnames,code.co_argcount,sep="\n")

#Security
def nice(): print("You're awesome!")
def mean(): print("You're... not awesome. OOOOH")

# Overwrite the code object for nice
nice.__code__ = mean.__code__
nice()  # prints "You're... not awesome. OOOOH"

#dis module
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


import dis

dis.dis(gcd)

#Parameter Annotations (__annotations__)
def annotated(a: int, b: str) -> list:
    return [a, b]

print(annotated.__annotations__)
# {'b': <class 'str'>, 'a': <class 'int'>, 'return': <class 'list'>}

#Call (__call__)
def greet(): print("Hello world!")

greet() # "Hello world!"
# is just syntactic sugar for
greet.__call__()  # "Hello world!"

