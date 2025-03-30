f = open('input.txt', 'r', encoding='utf-8')
a = f.readlines()
b = {}
for i in a:
  i = i.split()
  b[(i[0] + ' ' + i[1])] = int(i[2])
mnv = 999
mnk = None
mxv = -1
mxk = None
for i in b.keys():
  if b[i] > mxv:
    mxv = b[i]
    mxk = i
  if b[i] < mnv:
    mnv = b[i]
    mnk = i
f = open('output1.txt', 'w', encoding='utf-8')
f.write(mxk + ' ' + str(mxv))
f = open('output2.txt', 'w', encoding='utf-8')
f.write(mnk + ' ' + str(mnv))