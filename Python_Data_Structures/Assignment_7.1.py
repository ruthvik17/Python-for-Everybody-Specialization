# Use words.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1: fname = "words.txt"
fh = open(fname)

for lines in fh:
    lines = lines.upper()
    lines = lines.strip()
    print(lines)