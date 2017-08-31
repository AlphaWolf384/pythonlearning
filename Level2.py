import re

data = open('C:\Users\DRicchi\Desktop\Level2.txt').read()

count = {}
for c in data:
    count[c] = count.get(c, 0) + 1

print count


find = re.findall("<!--(.*?)-->", data, re.DOTALL)[-1]
    


print("".join(re.findall("[A-Za-z]", find)))
