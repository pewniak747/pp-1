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

fig = plt.figure(figsize=(8, 2))
ax = fig.add_subplot(111)

def bar(processor, start, length, color = 'y'):
  if length == 0:
    return
  margin = 0
  rectangle = patches.Rectangle((start, processor - 1 + margin), length, 1 - 2*margin, color=color, alpha=0.9)
  ax.add_patch(rectangle)

def communication(source, destination, start, length):
  bar(source, start, length, 'b')
  bar(destination, start, length, 'g')

def processing(processor, start, length):
  bar(processor, start, length)

if data['X'] == 1:
  communication(2, 1, data['ts12'], data['C12'] * data['d12'])
else:
  communication(1, 2, data['ts12'], data['C12'] * data['d12'])

if data['Y'] == 1:
  communication(2, 3, data['ts23'], data['C23'] * data['d23'])
else:
  communication(3, 2, data['ts23'], data['C23'] * data['d23'])

communication(3, 4, data['ts34'], data['C34'] * data['d34'])

processing(1, 0, data['A1'] * data['di1'])
processing(1, data['te12'], data['A1'] * data['dii1'])

processing(2, min(data['te12'], data['te23']), data['A2'] * data['di2'])
processing(2, max(data['te12'], data['te23']), data['A2'] * data['dii2'])

processing(3, 0, data['A3'] * data['di3'])
processing(3, max(data['te34'], data['te23']), data['A3'] * data['dii3'])

processing(4, data['te34'], data['A4'] * data['d4'])

plt.axvline(data['T'])
plt.yticks([0.5, 1.5, 2.5, 3.5], ["P1", "P2", "P3", "P4"])
plt.xlim(0, 1.2*data['T'])
plt.ylim(0, 4)
plt.xlabel("time")
plt.show()
