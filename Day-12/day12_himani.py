# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
#  (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
#  0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

import random
from turtle import color

def list_of_hexa_colors():
    hexcolor='#'
    symbols=['a','b','c','d','e','f']

    while len(hexcolor) < 7:
        hexcolor+=random.choice(str("1234567890abcdef"))

    # col=random.randrange(0,2**24)
    # hexcolor=hex(col)
    
    return hexcolor


print(list_of_hexa_colors())


# 2. Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


def  generate_colors(type,noOfColors):
    colors=[]
    if type == 'hexa':
        while noOfColors > 0:
            colors.append(list_of_hexa_colors())
            noOfColors-=1
    else:
        while noOfColors > 0:
            noOfColors-=1
            colors.append('rgb(' + str(random.randint(0,255)) + ',' +  str(random.randint(0,255)) + ',' +  
            str(random.randint(0,255))+ ',')
    
    return colors


print(generate_colors('hexa',3))
print(generate_colors('rgb',5))


