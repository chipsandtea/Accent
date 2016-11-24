import http.client, urllib.request, urllib.parse, 
import urllib.error, base64, json, nltk
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams

def queryAPI(body):
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
        dic = {"queries":["this","is","this is"]}
        body = json.dumps(dic)
        conn.request("POST", "/text/weblm/v1.0/calculateJointProbability?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def extractTrigrams(raw):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(raw)
    trigrams = ngrams(tokens, 3)
    print(type(trigrams))
    print(trigrams)
    return trigrams

def main(raw):

if __name__ == '__main__':
    main()