fname = input("Enter the file name")
fh = open(fname)
lines = []
word = []
count = 0
j = 0
for line in fh:
    line = line.strip()
    lines.append(line.split(' '))
for i in lines:
    if i[0] == "From":
        word.append(i[1])
        count = count + 1

for i in word:
    print(i)
print("There were", count, "lines in the file with From as the first word")
