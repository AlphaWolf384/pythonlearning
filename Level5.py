from urllib2 import urlopen
import pickle

url = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(url)

for line in data:
    print("".join([k * v for k, v in line]))
