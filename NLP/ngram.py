import http.client, urllib.request, urllib.parse
import urllib.error, base64, json, nltk
from nltk import word_tokenize
from nltk.util import ngrams
import string, re

# Queries the Microsoft LM API for joint probabilities of trigrams.
class ngrammer:
    def __init__(self):
        self.tkns = dict()

    # Returns the index the token was received for reordering.
    def getIndex(self, token):
        return self.tkns[token]

    # Tags the part of speech 
    def pos_tag(self, list_of_ngrams):
        pos_list = []
        for ngram in list_of_ngrams:
            pos_list.append(nltk.pos_tag(word_tokenize(ngram[0])))
        return pos_list

    # Queries Microsoft LM api
    def queryAPI(self, body_dict):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': '9292de8c83df4531861ef48c725f9256',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'model': 'query',
        })

        try:
            conn = http.client.HTTPSConnection('api.projectoxford.ai')
            
            body = json.dumps(body_dict)
            conn.request("POST", "/text/weblm/v1.0/calculateJointProbability?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()
            #print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return data

    def extractProbabilities(self, unserialized_data):
        data = json.loads(unserialized_data.decode('utf-8'))
        trigram_probabilities = []
        for trigram_result in data['results']:
            remake = []
            #print(trigram_result['words'])
            for word in word_tokenize(trigram_result['words']):
                remake.append(self.capitalize(word))
            #print(remake)
            rebuilt = ' '.join(remake)
            trigram_result['words'] = rebuilt
            print('Trigram: ' + trigram_result['words'] + ' | ' + 'Probability: ' + str(trigram_result['probability']))
            trigram_probabilities.append((trigram_result['words'], trigram_result['probability']))
        return trigram_probabilities

    # Extract and returns the trigrams given a sanitized input string.
    def extractTrigrams(self, input_string):
        print('Raw: ' + input_string)
        tokens = word_tokenize(input_string)
        for i in range(len(tokens)):
            self.tkns[tokens[i]] = i
            #print(self.tkns[tokens[i]])
        #print('Tokens: ', end = '')
        #print(tokens)
        numOfTokens = len(tokens)
        if numOfTokens == 1:
            print('1')
        elif numOfTokens == 2:
            trigramGenerator = ngrams(tokens,2)
        elif numOfTokens == 3:
            trigramGenerator = ngrams(tokens, 3)
        else:
            trigramGenerator = ngrams(tokens, 4)
        trigrams = set()
        [trigrams.add(gram) for gram in trigramGenerator]
        print(trigrams)
        return trigrams
        

    # Constructs and returns a dictionary obj that makes up the body of the API Query.
    def constructBody(self, trigrams):
        body = dict()
        body['queries'] = []
        for gram in trigrams:
            body['queries'].append(' '.join(list(gram)))

        #print(body['queries'])
        return body

    # Sanitizes the input by removing punctuation other than apostrophes and hyphens.
    def sanitize(self, raw):
        remove_regex = string.punctuation
        remove_regex = remove_regex.replace("'","")
        remove_regex = remove_regex.replace("-","")
        pattern = r"[{}]".format(remove_regex)
        sanitized = re.sub(pattern,'',raw)
        return sanitized

    def capitalize(self, word):
        for tkn in self.tkns:
            if word == tkn.lower():
                word = tkn
        return word


    def probabilities(self, raw):
        sanitized_input = self.sanitize(raw)
        trigram_list = self.extractTrigrams(sanitized_input)
        body = self.constructBody(trigram_list)
        raw_output = self.queryAPI(body)
        trigram_probabilities = self.extractProbabilities(raw_output)
        return(trigram_probabilities)
