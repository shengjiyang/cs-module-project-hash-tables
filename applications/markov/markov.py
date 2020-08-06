import numpy as np
import random

# Read in all the words in one go
URL = "/Users/samuel/Programming/GitHub/Lambda School/Assignments/cs-module-project-hash-tables/applications/markov/input.txt"
with open(URL) as f:
    words = f.read()

pairs = []
for w in range(len(words.split()[1:])):
    pairs.append((words.split()[w], words.split()[1:][w]))

d = {}
for first, second in pairs:
    if first not in d:
        d[first] = []

    d[first].append(second)

print(d)