"""
Python tutorial.
Author and copyright: Thomas Watson, 2019
License: For use only in COMP 4030: Design and Analysis of Algorithms,
         University of Memphis
"""

def max_of_short_list(w):
	"""
	Given a list w of one or two integers, returns the maximum.
	(Garbage in, garbage out if the length of w is not one or two.)
	"""

	return w[1] if (len(w) > 1 and w[1] > w[0]) else w[0]


print("Hello world")

# Here's a comment.

x = 5
y = x // 2
z = x / 2
z = y ** 0.5

if 1 > 2:
    print("Pigs can fly")
elif 1 < 2:
    print("Fish can swim")
else:
    print("The cows came home")

while x != 10:
    print(x)
    x += 1

for i in range(10):
    print(i, end=" ")
print()

x, y = 17, 19
x, y = y, x
print(x, y)

###############################################################################

a = [1, 3, 5, 7, 9]
x = len(a)
b = a

a[0] = 8
b[1] = 6
print(a)

a.sort()
print(b)

b = a[1:4]
a[2] = 10
for k in b:
    print(k, end=" ")
print()

###############################################################################

c = [-1, -1, -1, -1, -1]
d = [-1] * 5
e = c

print(c == d)
print(c == e)
print(c is d)
print(c is e)

e = []
if e: print("e is not empty")
if c: print("c is not empty")

###############################################################################

# The following illustrate "list comprehensions": a convenient way to create
# a list by embedding a loop into an expression.

squares = [i * i for i in range(1, 11)]
print(squares)

even_squares = [i * i for i in range(1, 11) if i % 2 == 0]
print(even_squares)

# Python convention is to use snake_case for variables and methods/functions,
# and UpperCamelCase for class names.

###############################################################################

print(max_of_short_list([7]))
print(max_of_short_list([7, 8]))
print(max_of_short_list([8, 7]))
