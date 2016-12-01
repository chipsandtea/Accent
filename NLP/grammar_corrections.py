from ngram import ngrammer
import nltk
from nltk import word_tokenize
class corrector:
	def __init__(self):
		self.CORRECTNESS_THRESHOLD = 10.0
		self.PRONOUN_TOLERANCE = 4.5
		self.ngrams_with_pos = dict()

	def initial_flagging(self, ngram_prob):
		if abs(ngram_prob) >= self.CORRECTNESS_THRESHOLD:
			return True
		else:
			return False

	# modify first coodinate of each tuple to store a list of tuples
	# db -> list of tuples
	# 1st coord -> list of tuples (words in order w/ tagging)
	# dict
	


	def check_tolerance(self):
		for i in range(len(self.ngrams_with_pos)):
			for word in self.ngrams_with_pos[i]['tuple']:
				if word[1] == 'NNP':
					print('Pronoun - Singular')
					self.ngrams_with_pos[i]['probability'] = self.ngrams_with_pos[i]['probability'] + self.PRONOUN_TOLERANCE
			if abs(self.ngrams_with_pos[i]['probability']) < self.CORRECTNESS_THRESHOLD:
				self.ngrams_with_pos.pop(i,None)


	def check(self, input_string):
		ng = ngrammer()
		sanitized_input = ng.sanitize(input_string)
		trigram_list = ng.extractTrigrams(sanitized_input)
		probabilities = ng.probabilities(input_string)
		wrong_ngrams = []
		for ngram_prob in probabilities:
			if self.initial_flagging(float(ngram_prob[1])):
				wrong_ngrams.append(ngram_prob)
		pos_tagged_list = ng.pos_tag(wrong_ngrams)

		for ngram_index in range(len(pos_tagged_list)):
			ngram_tuple = []
			for word_pos_pair in pos_tagged_list[ngram_index]:
				ngram_tuple.append((word_pos_pair[0], word_pos_pair[1], ng.getIndex(word_pos_pair[0])))
			self.ngrams_with_pos[ngram_index] = dict()
			self.ngrams_with_pos[ngram_index]['tuple'] = ngram_tuple
			self.ngrams_with_pos[ngram_index]['probability'] = wrong_ngrams[ngram_index][1]


		print(wrong_ngrams)
		for i in self.ngrams_with_pos:
			print(self.ngrams_with_pos[i]['tuple'])
			print(self.ngrams_with_pos[i]['probability'])
		self.check_tolerance()
		for i in self.ngrams_with_pos:
			print(self.ngrams_with_pos[i])

