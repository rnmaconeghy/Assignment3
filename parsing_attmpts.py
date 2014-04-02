#Here are a couple of my aattempts at parsing the file for multiple alignments but my .txt file keeps coming out empty along with other errors.

#attempt1
infile=open('serprot_pairs.out')

init=infile.readline()

while init[:6] !=' I':
  
  init=infile.readline()

colnames=['I', 'J', 'ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STEDEV', 'SCORE', 'NUMBER']

filename='serprot_pairs.txt'

file=open(filename, 'w')

for c in colnames:
  file.write(c + '\t')

#attempt2

import re
filename='serprot_pairs.out'
opened=open('serprot_pairs.out', 'r')
outfile='serprot_test.txt'
outfile2=open('serprot_table.txt', 'w')
pattern = r'(\d+) +>([^/]+)/'
tablestart=' I'
newfile=[]
d = {}
with open(filename, 'r') as f:
  lines=f.readlines()

for line in lines:
  match = re.search(pattern,line)
if match:
  newline=match.group() + '\n'
  newfile.append(newline)

with open(outfile, 'w') as o:
  o.seek(0)
o.writelines(newfile)

with open(outfile,'r') as p:
  for line in p:
  (index, id) =line.split()
d[int(index)]=id

colnames=['I', 'J', 'ILEN','JLEN','%IDENT','NAS','MATCH','SCORE']
for cols in colnames:
  outfile2.write(cols + '\t')

insert=opened.readline()
while insert[:6] !=' I':
  opened.readlines