#  Create a student dictionary and 
self=dict()

#  add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
self['name']="Himani"
self['gender']="Female"
self["skills"]=['C/C++','Python','Java','git','SQL']

#  Get the length of the student dictionary
print(self)
print("Lenght",len(self))

#  Get the value of skills and check the data type, it should be a list
print(self['skills'])
print(type(self))

#  Modify the skills values by adding one or two skills
self['skills'].append("Android")
self['skills'].append("PHP")

#  Get the dictionary values as a list
myself=list(self.values())
print(myself)

#  Change the dictionary to a list of tuples using the items() method
print(tuple(self.items()))
