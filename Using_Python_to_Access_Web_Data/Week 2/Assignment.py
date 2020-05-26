import re
fname = r"C:\Users\ruthv\PycharmProjects\Using Python to Access Web Data\Week 1\regex_sum.txt"
fh = open(fname)
num = []
for line in fh:
    num.append(re.findall('[0-9]+', line))

count = 0

for i in num:
    if len(i) == 0: continue
    else:
        for j in i:
            count = count + int(j)

print(count)
