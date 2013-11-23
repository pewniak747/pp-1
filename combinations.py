#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
from matplotlib import patches

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

c = (sys.argv[1], sys.argv[2])

if c == ('a', 'e'):
  communication(1, 2, 0, 2)
  communication(3, 2, 2, 2)
  communication(3, 4, 0, 2)
  processing(1, 2, 6)
  processing(2, 4, 4)
  processing(3, 4, 4)
  processing(4, 2, 6)
elif c == ('a', 'f'):
  communication(1, 2, 0, 2)
  communication(2, 3, 2, 2)
  communication(3, 4, 0, 2)
  processing(1, 2, 6)
  processing(2, 4, 4)
  processing(3, 4, 4)
  processing(4, 2, 6)
elif c == ('b', 'e'):
  communication(1, 2, 4, 2)
  communication(3, 2, 2, 2)
  communication(3, 4, 0, 2)
  processing(1, 0, 4)
  processing(1, 6, 2)
  processing(2, 6, 2)
  processing(3, 4, 4)
  processing(4, 2, 6)
elif c == ('b', 'g'):
  communication(2, 1, 4, 2)
  communication(3, 2, 2, 2)
  communication(3, 4, 0, 2)
  processing(1, 0, 4)
  processing(1, 6, 2)
  processing(2, 6, 2)
  processing(3, 4, 4)
  processing(4, 2, 6)
elif c == ('c', 'e'):
  communication(1, 2, 0, 2)
  communication(3, 2, 2, 2)
  communication(3, 4, 4, 2)
  processing(1, 2, 6)
  processing(2, 4, 4)
  processing(3, 0, 2)
  processing(3, 6, 2)
  processing(4, 6, 2)
elif c == ('c', 'f'):
  communication(1, 2, 0, 2)
  communication(2, 3, 2, 2)
  communication(3, 4, 4, 2)
  processing(1, 2, 6)
  processing(2, 4, 4)
  processing(3, 0, 2)
  processing(3, 6, 2)
  processing(4, 6, 2)
elif c == ('d', 'e'):
  communication(1, 2, 2, 2)
  communication(3, 2, 0, 2)
  communication(3, 4, 2, 2)
  processing(1, 0, 2)
  processing(1, 4, 4)
  processing(2, 4, 4)
  processing(3, 4, 4)
  processing(4, 4, 4)
elif c == ('d', 'g'):
  communication(2, 1, 2, 2)
  communication(3, 2, 0, 2)
  communication(3, 4, 2, 2)
  processing(1, 0, 2)
  processing(1, 4, 4)
  processing(2, 4, 4)
  processing(3, 4, 4)
  processing(4, 4, 4)

plt.yticks([0.5, 1.5, 2.5, 3.5], ["P1", "P2", "P3", "P4"])
plt.xticks([], [])
plt.ylim(0, 4)
plt.xlim(0, 8)
#plt.savefig('combination-' + c[0] + c[1] + '.png')
plt.show()
