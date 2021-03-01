import pandas as pd
with open("file1.txt") as data1:
    list1 = [n for n in data1.readlines()]
    print(list1)

with open("file2.txt") as data2:
    list2 = [n for n in data2.readlines()]
    print(list2)

result = [int(n) for n in list1 if n in list2]
print(result)
