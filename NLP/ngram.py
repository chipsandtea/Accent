import http.client, urllib.request, urllib.parse
import urllib.error, base64, json, nltk
from nltk import word_tokenize
from nltk.util import ngrams

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
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def extractTrigrams(raw):
    tokens = word_tokenize(raw)
    trigramGenerator = ngrams(tokens, 3)
    trigrams = []
    [trigrams.append(gram) for gram in trigramGenerator]
    body = dict()
    body['queries'] = []
    for gram in trigrams:
        body['queries'].append(' '.join(gram))

    print(body['queries'])
    return body


def main(raw):
    queryAPI(extractTrigrams(raw))

if __name__ == '__main__':
    main()