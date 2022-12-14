#search
'''import re
tx = 'the rain in spain'
a = re.search('spain',tx)
if a:
    print('available')
else:
    print('not available')'''

#findall
'''import re
tx = 'the rain in spain'
a = re.findall('ain',tx)
print(a)'''

#split
'''import re
tx = 'the rain in spain'
#a = re.split('ain',tx)
a = re.split('ain',tx,1)
print(a)'''
#sub

'''import re
tx = 'the rain in spain'
#a = re.sub('ain','ainy',tx)
a = re.sub('ain','ainy',tx,1)
print(a)'''


'''import re
tx = 'the rain in spain'
a = re.match('the rain in spain',tx)
print(a)'''


'''import re
txt= 'we are 50 in count'
x=re.findall('\d',txt)
print(x)
y = re.findall('we................',txt)
print(y)'''

'''import re
txt = 'we are very happy here'
z=re.findall('^we',txt)
if z:
    print('Yes')
else:
    print('No')'''




'''import re
txt = 'we are very happy here'
z=re.findall('here$',txt)
if z:
    print('Yes')
else:
    print('No')'''


'''import re
txt = 'hello world'
z=re.findall('he.*o',txt)#it can be '*' '+' '?'
if z:
    print('Yes')
else:
    print('No')

* - zero or more occurence
+ - one or more occurence
? - zero or one occurnece
'''

'''import re
txt = 'hello world'
z=re.findall('he.{2}o',txt)#it can be {3} without 'o' ex:-he.{3}
if z:
    print('Yes')
else:
    print('No')'''


import re
txt = 'hello world'
z=re.findall('o|bye',txt)#it can be {3} without 'o' ex:-he.{3}
print(z)
if z:
    print('Yes')
else:
    print('No')
