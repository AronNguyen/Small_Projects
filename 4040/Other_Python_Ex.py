from functools import reduce
import re

##NOT LAMBDA EXPRESSION
def square(num):
    return num * num

my_list = [1, 2, 3, 4, 5, 6]

result = list(map(square, my_list))
print(result)

##LAMBDA EXPRESSION

resutlt = list(map(lambda x: x*x, my_list))
print('resutlt using lambda expression', result)


result = list(map(lambda x: x*x if x%2 == 0 else x ** 3, my_list))
print('resutlt using lambda expression', result)

result = list(filter(lambda x: x%2 == 0, my_list))
print('filter result using lambda expression', result)

result = reduce(lambda x, y: x*y, my_list)
print('reduce result using lamda expression', result)

dogs = ['Tod', 'Tom', 'Bob']
big_dogs = []
for dog in dogs:
    big_dogs.append("Big {}".format(dog))
print(big_dogs)

big_dogs = ['Big {}'.format(dog) for dog in dogs]
print(big_dogs)

sentences = ['Mary read a story to Sam and Isla', 'Isla cuddled Sam', 'Sam chortled']
result = len(list(filter(lambda x: re.search('Sam', x), sentences)))
print(result)
result = len(list(map(lambda x: x.index('Sam'), sentences)))
print(result)
reuslt = reduce(lambda a, x: a + x.count('Sam'), sentences, 0)
print(result)

def i_am_an_object(myarg):
    return myarg

print(i_am_an_object(1))

an_object_by_any_other_name = i_am_an_object
print(an_object_by_any_other_name(5))
print(i_am_an_object)
print(an_object_by_any_other_name)

def outer():
    def inner(a):
        return a
    return inner

f = outer()
print(f)
print(f(10))

f2 = outer()
print(f2(11))

def outer2(a):
    def inner2(b):
        return a + b
    return inner2

add1 = outer2(1)
print(add1)
print(add1(4))
