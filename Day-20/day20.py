# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

from requests.auth import HTTPBasicAuth
import requests

responseOfRequest=requests.get('http://www.gutenberg.org/files/1112/1112.txt')

try:
    print(responseOfRequest.json())
except :
    print(responseOfRequest.status_code)


# responseWothAuth=requests.get('https://api.github.com / user,')
# print(responseWothAuth.status_code)

# print(responseOfRequest.content)
# print(responseOfRequest.text)


# 2. Read the countries API and find
#    a. the 10 largest countries
#    b. the 10 most spoken languages
#    c. the total number of languages in the country's API


