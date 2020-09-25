"""
Tech challenge for google when they came to the University

Problem was to decode a sentence where each character of a word had been shifted
a certain amount

Brute forced since there are only 26 character in the alphabet
returned a list of words and then pick from the list the actual words

"""

def game_genie():

    c = 'S'
    h = 'Q'
    a = 'Z'
    r = 'U'
    e = 'Q'
    ##y = 'S'
    ##p = 'J'
    ##q = 'I'

    for i in range(20):
        print(i)

        c = chr(ord(c) + 1)
        if c > 'Z':
            c = 'A'

        h = chr(ord(h) + 1)
        if h > 'Z':
            h = 'A'

        a = chr(ord(a) + 1)
        if a > 'Z':
            a = 'A'

        r = chr(ord(r) + 1)
        if r > 'Z':
            r = 'A'

        e = chr(ord(e) + 1)
        if e > 'Z':
            e = 'A'



        print(c,h,a,r,e)

    return -1

print(game_genie())


"""
Another challenge that a friend completed
"""
def number_munchers():
    a = -1
    b = -1
    c = -1
    i = 1
    j = 1
    for i in range(1000):
        for j in range(1000):
            temp = i * j
            if temp < 1000:
                a = temp % 1000
            elif temp < 100
            temp % 100:
                a = temp % 100
            else temp < 10:
                a = temp % 10
            print(a)

# print(number_munchers())
