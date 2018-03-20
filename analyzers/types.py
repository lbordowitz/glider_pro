import re

f = open('Glider PRO.r','rb')
lines = []

for line in f:
     lines += [line]

f.close()

typelines = [x for x in lines if ord('{') in x]

types_of_things = []
c = 0
for t in typelines:
     try:
             m = re.search(r'data \'(.*)\' \(([0-9]*)(, ".*")?\) {', t.decode())
             if m is not None:
                     types_of_things += [m.group(1)]
     except UnicodeDecodeError:
             c = c + 1
 

print(set(types_of_things))
print(c)

