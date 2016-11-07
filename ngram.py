########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9292de8c83df4531861ef48c725f9256',
}

params = urllib.parse.urlencode({
    # Request parameters
    'model': 'body',
    'order': '4',
})

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/text/weblm/v1.0/calculateJointProbability?%s" % params, "How\'re you doing today", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))