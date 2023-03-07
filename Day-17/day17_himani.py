
# 1. This is an Exception Handling Question.
from asyncio.windows_events import NULL
from unicodedata import name


names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
#  Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

nordic_countries=[]
es=NULL
ru=NULL

class fiveError(Exception):
    pass

class sixError(Exception):
    pass

try:
    for i in range(0,len(names)):
        if(i == 5):
            raise fiveError
        nordic_countries.append(names[i])
except fiveError:
        es=names[i]
        ru=names[i+1]
       
print(nordic_countries,es,ru,sep='\n')


# 2. Input a name, Year you were born, and declare the age variable. In age variable 2023 - year_born. Handle a type_error that occurred
