# applications/histo/histo.py

URL = "/Users/samuel/Programming/GitHub/Lambda School/Assignments/cs-module-project-hash-tables/applications/histo/robin.txt"
with open(URL) as f:
    words = f.read()

def word_count(s):
    d = {}
    words = []
    for w in s.split():
        w = w.strip(",").strip(".").strip('"')
        words.append(w.lower())

    for w in words:
        if ":;,.-+=/\\|[]{}()*^&" in words:
            return {}

        else:
            d[w] = words.count(w)

    return d

def histo(s):
    d = word_count(s)
    table = sorted(list(d.items()), key=lambda i: (-i[1], i[0]))
    for word, freq in table:
        print(f"{word} " + "#" * freq)

histo(words)