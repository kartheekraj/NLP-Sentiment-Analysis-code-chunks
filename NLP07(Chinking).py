tokenized = custom_sent_tokenizer.tokenize(sample)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			
			chunkGram = r"""Chunk: {<.*>}"""

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			print(chunked)