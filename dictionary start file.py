phonebook = {'Chris':'555-1111',
             'Katie':'555-2222',
             'Joanne':'555-3333'}
'''
print()
print('*****  start section 1 - print dictionary ********')
print()


print(phonebook)

print(len(phonebook))

mydictionary = dict(m=8,n=9)

print(mydictionary)

print()
print('*****  end section 1 ********')
print()







print()
print('*****  start section 2 - search dictionary ********')
print()


phone = phonebook['Chris']

print(phone)

---OR---

print(phonebook['Chris'])

print(phonebook)

---print(phonebook['Joe'])  <-- gives problems b/c Joe not in the Dictionary        can fix by always using the if method below---


name = 'Chris'          ---Don't forget that Python is case sensitive---

if name in phonebook:
    print(phonebook[name])
else:
    print('Not found')


print()
print('*****  end section 2 ********')
print()






print()
print('*****  start section 3 - edit/append dictionary ********')
print()


phonebook['Chris'] ='555-4444'

phonebook['Joe'] = '555-0123'

---if the key does not exist in the dictionary --> it will add it to the dictionary---

print(phonebook)

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


del phonebook['Chris']

print(phonebook)        'notice both value & key are deleted      notice Joe isn't in Dictionary, every time you run it again it wipes clean & starts over'---'


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

for k in phonebook:
    print(k)
    print(phonebook[k])         'the print k will only give names, must do the second line to print the values'


print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()

for v in phonebook.values():
    print(v)
                                    'no need for a key, it gives you the direct values'


print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

for pair in phonebook.items():
    print(pair)
                                    'Pair Object type = tuple   b/c you are getting Key & Values'

'for k,v in phonebook.items():'
    'print(k,v)'


print()
print('*****  end section 7 ********')
print()


'''





print()
print('*****  start section 8 - using random and converting to list ********')
print()




print()
print('*****  end section 8 ********')
print()








'''