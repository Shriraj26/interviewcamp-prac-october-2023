
# ip - 'i live in a house'
# op -- "house live in a i"

def reverseWordsInSentence(sentence):

    start, end = len(sentence) - 1, len(sentence)
    newWord = ''

    while start >= 0:

        if sentence[start] == ' ':
            newWord += sentence[start+1: end] + ' '
            end = start
        
        start -= 1

    newWord += sentence[start + 1: end]

    print(newWord)

sentence = 'i live in a house'
# sentence = 'robber i'

reverseWordsInSentence(sentence)
