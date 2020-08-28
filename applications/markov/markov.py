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


start = []
for w in list(d.keys()):
    if w[0] == w[0].upper() and w[0] != "(" and w[0:2] != '"-' and w[-1] != ")" and w[-1] != "." and w[-1] != "!":
        start.append(w)

stop = []
for w in list(d.keys()):
    if w[-1] == "." or w[-1] == "!" or w[-1] == "?":
        stop.append(w)

random.seed(84)
print(random.choice(start), end=" ")
print(random.choice(d["As"]), end=" ")
print(random.choice(d[random.choice(d["As"])]), end=" ")
print(random.choice(d[random.choice(d[random.choice(d["As"])])]), end=" ")
print(random.choice(d["if"]), end=" ")
print(random.choice(stop))

# Sentence 1: "As soon as if I declare!"

print(random.choice(start), end=" ")
print(random.choice(d["It"]), end=" ")
print(random.choice(d[random.choice(d["It"])]), end=" ")
print(random.choice(stop))

# Sentence 2: "It was the pencil."

print(random.choice(start), end=" ")
print(random.choice(d["How"]), end=" ")
print(random.choice(d[random.choice(d["How"])]), end=" ")
print(random.choice(d[random.choice(d[random.choice(d["How"])])]), end=" ")
print(random.choice(d[random.choice(d[random.choice(d[random.choice(d["How"])])])]), end=" ")
print(random.choice(stop))

# Sentence 3: "How would check, see get manners!"

print(random.choice(start), end=" ")
print(random.choice(stop))

# Sentence 4: "I've manners!"

print(random.choice(start), end=" ")
print(random.choice(d[random.choice(start)]), end=" ")
print(random.choice(d[random.choice(d[random.choice(start)])]), end=" ")
print(random.choice(d[random.choice(d[random.choice(d[random.choice(start)])])]), end=" ")
print(random.choice(d["all"]), end=" ")
print(random.choice(d[random.choice(d["all"])]), end=" ")
print(random.choice(stop))

# Sentence 5: "Here the some all the outside. Kitty?"