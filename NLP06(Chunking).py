#Chunking
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train = state_union.raw('2005-GWBush.txt')
sample = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train)

tokenized = custom_sent_tokenizer.tokenize(sample)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			
			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			print(chunked)



	except Exception as e:
		print(str(e))

process_content()