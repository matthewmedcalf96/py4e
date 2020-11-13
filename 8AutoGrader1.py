fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
	a = line.rstrip()
	b = a.split()
	lst = list(b)
print(lst)
