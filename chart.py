#!/usr/bin/env python

import sys, re
import matplotlib.pyplot as plt
from matplotlib import patches

lines = sys.stdin.readlines()
data = dict()

stream = open(sys.argv[1], 'r')
for line in stream.readlines():
  search = re.search('(\w+):\s+([\d\.]+)', line)
  if search:
    data[search.group(1)] = float(search.group(2))

for line in lines:
  search = re.search('Value of objective function: ([\d\.]+)', line)
  if search:
    data['T'] = float(search.group(1))
  else:
    search = re.search('(\w+)\s+([\d\.]+)', line)
    if search:
      data[search.group(1)] = float(search.group(2))

fig = plt.figure()
ax = fig.add_subplot(111)

def bar(processor, start, end, typebar):
  margin = 0
  if typebar == 'communication':
    color = 'b'
  elif typebar == 'processing':
    color = 'y'
  rectangle = patches.Rectangle((start, processor - 1 + margin), end-start, 1 - 2*margin, color=color, alpha=0.7)
  ax.add_patch(rectangle)

bar(1, data['ts12'], data['te12'], 'communication')
bar(2, data['ts12'], data['te12'], 'communication')

bar(2, data['ts23'], data['te23'], 'communication')
bar(3, data['ts23'], data['te23'], 'communication')

bar(3, data['ts34'], data['te34'], 'communication')
bar(4, data['ts34'], data['te34'], 'communication')

bar(1, 0, data['A1'] * data['di1'], 'processing')
bar(1, data['te12'], data['te12'] + data['A1'] * data['dii1'], 'processing')

start = min(data['te12'], data['te23'])
bar(2, start, start + data['A2'] * data['di2'], 'processing')
start = max(data['te12'], data['te23'])
bar(2, start, start + data['A2'] * data['dii2'], 'processing')

bar(3, 0, data['A3'] * data['di3'], 'processing')
start = max(data['te34'], data['te23'])
bar(3, start, start + data['A3'] * data['dii3'], 'processing')

bar(4, data['te34'], data['te34'] + data['A4'] * data['d4'], 'processing')

plt.axvline(data['T'])
plt.yticks([0.5, 1.5, 2.5, 3.5], ["P1", "P2", "P3", "P4"])
plt.xlim(0, 1.2*data['T'])
plt.ylim(0, 4)
plt.show()

