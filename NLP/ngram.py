import http.client, urllib.request, urllib.parse
import urllib.error, base64, json, nltk
from nltk import word_tokenize
from nltk.util import ngrams
import string

def queryAPI(body_dict):
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

def extractProbabilities(unserialized_data):
    data = json.loads(unserialized_data.decode('utf-8'))
    for trigram_result in data['results']:
        print('Trigram: ' + trigram_result['words'] + ' | ' + 'Probability: ' + str(trigram_result['probability']))


def extractTrigrams(input_string):
    print('Raw: ' + input_string)
    tokens = word_tokenize(input_string)
    print('Tokens: ', end = '')
    print(tokens)
    numOfTokens = len(tokens)
    if numOfTokens == 1:
        print('1')
    elif numOfTokens == 2:
        trigramGenerator = ngrams(tokens,2)
    else:
        trigramGenerator = ngrams(tokens, 3)
    trigrams = set()
    [trigrams.add(gram) for gram in trigramGenerator]
    print(trigrams)
    return trigrams
    

# Constructs and returns a dictionary obj that makes up the body of the API Query.
def constructBody(trigrams):
    body = dict()
    body['queries'] = []
    for gram in trigrams:
        body['queries'].append(' '.join(list(gram)))

    print(body['queries'])
    return body

def main(raw):
    #raw = raw.translate(None, string.punctuation)
    trigram_list = extractTrigrams(raw.lower())
    body = constructBody(trigram_list)
    raw_output = queryAPI(body)
    extractProbabilities(raw_output)

if __name__ == '__main__':
    main()