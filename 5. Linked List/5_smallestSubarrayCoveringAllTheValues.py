"""
For input words - ['and', 'of', 'one']
And this document text - 'a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses'
We need smallest substring that will have all the words 'and','of' and 'one'
Therefrore ans should be - 'of a main clause and sometimes one'

LRU is used to store the words occurred at what indices,
if u get say and, of or one from the doc, store in LRU the key as word and value as index
everytime u add a word and length of cache is full, calculate the substring length so that it should
be optimum


"""


