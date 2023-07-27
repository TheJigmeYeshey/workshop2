import sys

lst = []
total = 0

for line in sys.stdin:
    val = line.split()
    lst.append((val[0],int(val[1])))
    total += int(val[1])

print(total)

for i in lst:
    print(i[0], "[", "*" * i[1] * 2, "]", round((i[1]/total)*100, 0), '%')