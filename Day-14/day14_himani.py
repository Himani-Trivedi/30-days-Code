
from re import A


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use a map to create a new list by changing each country and name to uppercase in the countries list
countries=list(map(lambda s: s.upper(), countries))
names=list(map(lambda x : x.upper(),names))
print(countries)
print(names)

# 2. Use a filter to filter out countries having precisely six characters.
newCountries=list(filter(lambda x:len(x) == 6,countries))
print(newCountries)

# 3. Using the generator print the Fibonacci series.


def fibo(n):
    a=0
    b=1

    while True:
        yield a
        t=a+b
        a=b
        b=t

x=fibo(6)
for i in range(7):
    print(next(x))