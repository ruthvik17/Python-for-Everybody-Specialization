fname = input("Enter the file name:")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
lines = []
word = []
dict = {}
from collections import defaultdict

dict = defaultdict(int)
for line in fh:
    line = line.strip()
    lines.append(line.split(' '))

for i in lines:
    if i[0] == "From":
        word.append(i[1])

for i in word:
    if dict[i] == 0:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
p = 0
largest = None
k = None

for key, value in dict.items():
    if p == 0:
        largest = dict[key]
        k = key
    if largest < dict[key]:
        largest = dict[key]
        k = key
    p = p + 1

print(k, largest)