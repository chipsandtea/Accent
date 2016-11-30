from ngram import ngrammer

class corrector:
	def __init__(self):
		self.CORRECTNESS_THRESHOLD = 10.0
		self.PRONOUN_TOLERANCE = 4.5

	def isWrong(self, ngram_prob):
		if abs(ngram_prob) >= self.CORRECTNESS_THRESHOLD:
			return True
		else:
			return False

	def check(self, input_string):
		ng = ngrammer()
		probabilities = ng.probabilities(input_string)
		wrong_ngrams = []
		for ngram_prob in probabilities:
			if self.isWrong(float(ngram_prob[1])):
				wrong_ngrams.append(ngram_prob)
		print(wrong_ngrams)