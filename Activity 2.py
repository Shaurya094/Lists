def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
         ctr += 1
         lst.append(word)
    print ("Words that have the same start and end letter: \n", lst)
    return ctr

count = match_words(['abc', 'aca', 'rdr', 'cr7'])
print ("Number of words having the same first and least character: ", count) 