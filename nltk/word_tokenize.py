from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

para = "Hello, world! It's good to see you. Thanks for buying this book."
sents = sent_tokenize(para)
sents = [word_tokenize(sentence) for sentence in sents]
print sents

print "****"

words = word_tokenize(para)
print words