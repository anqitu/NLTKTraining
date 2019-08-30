# Module 3: Corpus
# Movie Review Corpus
# Author: Dr. Alfred

from nltk.corpus import movie_reviews

# print(movie_reviews.fileids())
# print(movie_reviews.categories())

fileid = 'pos/cv971_10874.txt'

text = movie_reviews.raw(fileid)
print(text)

print(" Num of chars :",len(movie_reviews.raw(fileid)))
print(" Num of words :",len(movie_reviews.words(fileid)))
print(" Num of sentences :",len(movie_reviews.sents(fileid)))

print(" Categories:",movie_reviews.categories(fileid))

