#Character Frequency Histogram
from os import strerror
freq = {chr(i) : 0 for i in range(97, 123)}
count = 0
print(freq)
try:
    file = open('D:\\Desktop\\Neo\\Test.txt', 'rt')
    for ch in file.read():
        if ch in freq.keys():
            freq[ch.lower()] += 1
    new_file = open('D:\\Desktop\\Neo\\Test' + '.hist.txt', 'w')
    for i in sorted(freq.keys(), key = lambda x : freq[x], reverse = True):
        new_file.write(i + '->' + str(freq.get(i)))
    new_file.close()
    file.close()
except IOError as e:
    print('Cannot open the source file: ', strerror(e.errno))
    exit(e.errno)
