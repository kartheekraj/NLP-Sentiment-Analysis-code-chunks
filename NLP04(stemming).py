#Stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example = ['python','pythoner','pythoning','pythoned','pythonly']

# for w in example:
# 	print(ps.stem(w))

new = "Grand Theft Auto (GTA) is an action-adventure video game series created by David Jones and Mike Dailly;[2] the later titles of which were created by brothers Dan and Sam Houser, Leslie Benzies and Aaron Garbut. It is primarily developed by Rockstar North (formerly DMA Design), and published by Rockstar Games. The name of the series references the term used in the US for motor vehicle theft. "

words = word_tokenize(new)

for w in words:
	print(ps.stem(w))