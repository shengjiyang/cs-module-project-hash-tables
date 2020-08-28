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

def no_dups(s):
    count = word_count(s)
    
    string = ""
    for key in count:
        string = string + " " + key

    return string[1:]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))