from ngram import ngrammer
import nltk
from nltk import word_tokenize
class corrector:
	def __init__(self):
		self.CORRECTNESS_THRESHOLD = 10.0
		self.PRONOUN_TOLERANCE = 4.5

	def isWrong(self, ngram_prob):
		if abs(ngram_prob) >= self.CORRECTNESS_THRESHOLD:
			return True
		else:
			return False

	# modify first coodinate of each tuple to store a list of tuples
	# db -> list of tuples
	# 1st coord -> list of tuples (words in order w/ tagging)
	# dict
	def pos_tag(self, list_of_ngrams):
		pos_list = []
		for ngram in list_of_ngrams:
			pos_list.append(nltk.pos_tag(word_tokenize(ngram[0])))
		return pos_list

	#def adjust_tolerance(self, )


	def check(self, input_string):
		ng = ngrammer()
		probabilities = ng.probabilities(input_string)
		wrong_ngrams = []
		for ngram_prob in probabilities:
			if self.isWrong(float(ngram_prob[1])):
				wrong_ngrams.append(ngram_prob)
		pos_tagged_list = self.pos_tag(wrong_ngrams)

		for i in range(len(pos_tagged_list)):
			wrong_ngrams[i] = (pos_tagged_list[i],wrong_ngrams[i])


		print(wrong_ngrams)
