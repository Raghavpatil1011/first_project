'''import re
tx = 'the rain in spain'
a = re.findall('ain',tx)
print(a)'''

'''import re
print(re.findall("hello world", "hello", 1))


import re
tx = 'the rain in spain'
#a = re.split('ain',tx)
a = re.split('ain',tx,1)
print(a)

import re
print(re.split('\W+', 'Hello, hello, hello.'))

import re
tx = 'the rain in spain'
a = re.match('the rain in spain',tx)
print(a)

import re
temp="amphievent@amp.com"
temp1=""
if(re.search(r'@amp\.',temp)):
    temp1=re.sub(r'a\w+(\.com)',r'edu\1',temp)
print(temp1)

import re
print(re.split(r'(n\d)=', 'n1=3.1, n2=5, n3=4.565'))''

import re
re.ASCII''

import re
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())''

import re
sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)''
print(matched.groupdict())'''


import re
str2=""
string = "Encountered Error : error code E101"
if(re.search(r"E...r",string)!=None):
    str2=re.sub(r"E(\d{3})",r"#\1",string)
print(str2)