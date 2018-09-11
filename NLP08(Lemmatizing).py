'''Lemmatizer converts plural into sigular'''
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better",pos= "a")) #a for acjective
print(lemmatizer.lemmatize("best",pos= "n"))   #n for noun
print(lemmatizer.lemmatize("running",pos= "v")) #v for verb
