# applications/crack_caesar/crack_caesar.py

URL = "/Users/samuel/Programming/GitHub/Lambda School/Assignments/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt"
with open(URL) as f:
    cipher = f.read()

def letter_count(s):
    
    d = {}
    
    for c in s:
        if c.isspace():
            continue
        
        if c not in d:
            d[c] = 0
            
        d[c] += 1
        
    return d

def print_sorted_letter_count(s):
	d = letter_count(s)

	items = list(d.items())

	items.sort(key=lambda e: e[1], reverse=True)

	for i in items:
		print(f"{i[0]}: {round(100 * (i[1] / len(cipher)), 2)}")

# print_sorted_letter_count(cipher)

cipher_dict = {
    "W" : "E",
    "J" : "T",
    "M" : "A",
    "X" : "O",
    "C" : "H",
    "D" : "N",
    "K" : "R",
    # "I" : "I",
    "N" : "S",
    "U" : "D",
    "S" : "L",
    "O" : "W",
    "G" : "U",
    "Q" : "G",
    "B" : "F",
    "Y" : "B",
    "E" : "M",
    "F" : "Y",
    "A" : "C",
    "Z" : "P",
    "P" : "K",
    "H" : "V",
    "V" : "Q",
    "T" : "J",
    "L" : "X",
    "R" : "Z"
}

def decode(words, cipher):
    result = ''
    for letter in words:
        if letter in cipher:
            result = result + cipher[letter]
        else:
            result = result + letter
    return result

print(decode(cipher, cipher_dict))