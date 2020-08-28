# applications/word_count/word_count.py

# Use dictionary to store words and their counts
    # What defines a word?
        # string of letters and punctuation,
        # unless that punctuation comes at beginning or end of a word.


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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

    print(word_count('":;,.-+=/\\|[]{}()*^&'))