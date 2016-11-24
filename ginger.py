#!/usr/bin/env python

"""Simple grammar checker

This grammar checker will fix grammar mistakes using Ginger.

Code placeholder for NLP functionality: https://github.com/zoncoen/python-ginger
Credit to zoncoen for unofficial API Ginger querying script.
"""

import sys
import urllib.parse
import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError
import json

def get_ginger_url(text):
    """Get URL for checking grammar using Ginger.
    @param text English text
    @return URL
    """
    API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"

    scheme = "http"
    netloc = "services.gingersoftware.com"
    path = "/Ginger/correct/json/GingerTheText"
    params = ""
    query = urllib.parse.urlencode([
        ("lang", "US"),
        ("clientVersion", "2.0"),
        ("apiKey", API_KEY),
        ("text", text)])
    fragment = ""

    return(urllib.parse.urlunparse((scheme, netloc, path, params, query, fragment)))


def get_ginger_result(text):
    """Get a result of checking grammar.
    @param text English text
    @return result of grammar check by Ginger
    """
    url = get_ginger_url(text)

    try:
        response = urllib.request.urlopen(url)
    except HTTPError as e:
            print("HTTP Error:", e.code)
            quit()
    except URLError as e:
            print("URL Error:", e.reason)
            quit()

    try:
        result = json.loads(response.read().decode('utf-8'))
    except ValueError:
        print("Value Error: Invalid server response.")
        quit()
    #print(result)
    return(result)


def main(string):
    """main function"""
    original_text = string
    if len(original_text) > 600:
        print("You can't check more than 600 characters at a time.")
        quit()
    fixed_text = original_text
    results = get_ginger_result(original_text)

    # Correct grammar case.
    if(not results["LightGingerTheTextResult"]):
        # print("No problems!")
        # No discernable issues.
        quit()

    # Incorrect grammar
    gap, fixed_gap = 0, 0
    for result in results["LightGingerTheTextResult"]:
        if(result["Suggestions"]):
            from_index = result["From"] + gap
            to_index = result["To"] + 1 + gap
            suggest = result["Suggestions"][0]["Text"]
            fixed_text = fixed_text[:from_index-fixed_gap] + suggest + fixed_text[to_index-fixed_gap:]


    #print("from: " + original_text)
    #print("to:   " + fixed_text)
    
    return fixed_text


if __name__ == '__main__':
    main()
