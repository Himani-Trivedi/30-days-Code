# 1. Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words

files = ['obama_speech.txt', 'michelle_obama_speech.txt',
         'donald_speech.txt', 'melina_trump_speech.txt']

for i in files:
    i="D:/Himani/30-days-Code/Day-19/Data/" + i
    with open(i, 'r') as f:
        linesCount=0
        wordsCount=0
        for line in f:
            linesCount+=1
            for word in line:
                wordsCount+=1
        print(i + ":")
        print(linesCount)
        print(wordsCount)


# 2. Extract all incoming email addresses as a list from the email_exchange_big.txt file

f=open("D:/Himani/30-days-Code/Day-19/Data/" + 'email_exchange_big.txt','r') 

emails=[]
for e in f:
    emails.append(e)

print(emails)
f.close()