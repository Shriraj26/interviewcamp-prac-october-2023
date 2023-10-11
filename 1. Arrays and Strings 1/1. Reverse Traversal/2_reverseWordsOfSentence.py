
# ip - 'i live in a house'
# op -- "house live in a i"

def reverseWordsInSentence(sentence):

    start = len(sentence) - 1
    end = start + 1
    newSentence = ''
    while start >= 0:

        # if there is a space, then add sentence[start+1] till end to a new string
        if sentence[start] == ' ':
            newSentence += sentence[start+1:end] + ' '
            end = start

        start -= 1

    newSentence += sentence[start+1: end] 

    print(newSentence) 

sentence = 'this is beautiful'
# sentence = 'hello'
# sentence = 'i'
# sentence = ''
reverseWordsInSentence(sentence)




