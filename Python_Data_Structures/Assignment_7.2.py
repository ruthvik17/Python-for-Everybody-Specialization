# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
num = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    index = line.find(":")
    num.append(float(line[index + 1:].strip()))

total = 0
for i in num:
    total = total + i

average = total / len(num)

print("Average spam confidence:", average)


