a = "coding is nice"
c_s = a.capitalize()
print(c_s)
c_s = a.center(45, '+')
print(c_s)
b = "LOLLiPoP"
l_s = b.casefold()
print(l_s)
c = "I love to read books"
print(c.count('o'))
print(c.endswith('lol'))
print(c.encode())
print(c.find('love'))
print(c.find('no'))
d = "Insomnia is bad"
print(d.index('bad'))
e = "7777lalala"
print(e.isalnum())
f = "santaclaus"
print(f.isalpha())
g = "jsdhkjwe1235 ksdjiejd78"
print(f.isdecimal())
h = "007007007"
print(h.isdigit())
i = "root4477"
print(i.isidentifier())
j = "4477root"
print(j.isidentifier())
print(a.islower())
k = "8888979797"
print(k.isnumeric())
l = 'Space is a printable'
print(l)
print(l.isprintable())
m = '\nNew Line is printable'
print(m)
print(m.isprintable())
n = ''
print('\nEmpty string printable?', n.isprintable())
o = "     \z"
print(o.isspace())
p = 'I Hate Drugs.'
if p.istitle() == True:
  print('Titlecased String')
else:
  print('Not a Titlecased String') 
q = 'GUtter'
if q.istitle() == True:
  print('Titlecased String')
else:
  print('Not a Titlecased String')
r = "BEAUTIFUL"
print(r.isupper())
s = "not BEAUTIFUL"
print(s.isupper())
separator = ', '
numList = ['1', '2', '3', '4']
print(separator.join(numList))
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))
