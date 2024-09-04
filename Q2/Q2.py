def words_finder(text):
    words = text.split(' ')
    dict = {}
    wordsList = []
    for word in words:
        wordsList.append(word.strip(".,?!").lower())
    for word in wordsList:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


text = "Hello world! Hello everyone."
print(words_finder(text))
