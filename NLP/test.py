from grammar_corrections import corrector
from ngram import ngrammer
import unittest



class NgramTest(unittest.TestCase):

	def setUp(self):
		self.ng = ngrammer()

	def testSanitize(self):
		self.assertEqual(self.ng.sanitize("Is that you're cup?"), "Is that you're cup")

	def testTrigramExtraction(self):
		self.assertEqual(self.ng.extractTrigrams("Is that you're cup"), {('Is', 'that', 'you', "'re"), ('that', 'you', "'re", 'cup')})

	def testConstructBody(self):
		self.assertEqual(self.ng.constructBody({('I', 'think', 'its', 'a'), ('think', 'its', 'a', 'cup')}), \
											{'queries': ['I think its a', 'think its a cup']})

if __name__ == "__main__": 
    unittest.main()