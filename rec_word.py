# Reverse the sentence

def recuersiveWord(sentence):
    stock = []

    words = sentence.split()
    for word in words:
        stock.insert(0, word)

    return ' '.join(word for word in stock)


sentence = 'Do or do not, There is no try.'
print(recuersiveWord(sentence))