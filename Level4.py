from urllib2 import urlopen
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num = "12345"
num = str(16044/2)
pattern = re.compile("and the next nothing is (\d+)")

while True:
    content = urlopen(url % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)
