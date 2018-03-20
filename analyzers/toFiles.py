import re

f = open('Glider PRO.r','rb')
lines = []

for linenum, line in enumerate(f):
  lines += [(linenum,line)]

f.close()

d_lit = bytes([ord(d) for d in 'data'])
e_lit = bytes([ord(d) for d in '};\n'])

typelines = [x for x in lines if d_lit in x[1]]
endlines = [y for y in lines if e_lit in y[1]]

types_of_things = []
num_of_things = []
resource_start = []
c = 0
for t in typelines:
  try:
    astr = t[1].decode().strip()
    m = re.search(r'data \'(.*)\' \(([0-9]*)(, .*)*\) {', astr)
    if m is not None:
      types_of_things += [m.group(1)]
      num_of_things += [m.group(2)]
      resource_start += [t[0]]
  except UnicodeDecodeError:
    c = c + 1
    print(t)

resource_end = [e[0] for e in endlines]

# print(set(types_of_things))

resources = zip(resource_start,resource_end,types_of_things,num_of_things)

# Typical data line:
# 	$"6368 6564 2074 6865 206E 756D 6265 7220"            /* ched the number  */
#
# data line between resource_start & resource_end lines, exclusive.

for resource in resources:
  f = open('resources/' + resource[3] + '.' + resource[2], 'wb')
  for line in lines[resource[0]+1:resource[1]]:
    m = re.search(r'\$"([0-9A-F ]*)"', str(line[1]))
    out = bytes([int(x,16) for x in re.findall(r'..',''.join(m.group(1).split()))])
    f.write(out)
  f.close()
