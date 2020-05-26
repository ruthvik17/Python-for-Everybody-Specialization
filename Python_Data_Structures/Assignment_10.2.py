fname = input("Enter the file name:")
if len(fname) < 1: fname = "mbox-short.txt"
fh = open(fname)
lines = []
word = []
hour = []
dict = {}
from collections import defaultdict

dict = defaultdict(int)

for line in fh:
    line = line.strip()
    lines.append(line.split(' '))

for i in lines:
    if i[0] == "From":
        word.append(i[6])
word = sorted(word)

for i in word:
    hour.append(i.split(":")[0])

for i in hour:
    if dict[i] == 0:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1

for key, value in dict.items():
    print(key, value)