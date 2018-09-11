#Word net
from nltk.corpus import wordnet

syns = wordnet.synsets("Program")

#synset
print(syns[0].name())

# just the word
print(syns[0].lemmas()[0].name())

#defination
print(syns[0].definition())

#examples
print(syns[0].examples())