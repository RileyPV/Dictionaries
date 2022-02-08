person = {}
person['fname'] = 'Joe'
person['lname'] = 'Fonebone' 
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey'] #list
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'} #dictionary

print(person)

print(type(person['children']))


print(person['children'][2])


print(person['pets']['cat'])


for i in person['children']:
     print(i)

for i,j in person['pets'].items():
     print(i)
     




                      
