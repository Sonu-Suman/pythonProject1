# Reverse the sentence

def recuersiveWord(sentence):
    stock = []

    words = sentence.split()
    for word in words:
        stock.insert(0, word)

    stock[0] = list(stock[0])[0].upper() + stock[0][1:]
    return ' '.join(word for word in stock)


sentence = 'Do or do not, There is no try.'
print(recuersiveWord(sentence))