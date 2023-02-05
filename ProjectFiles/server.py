from flask import Flask, request, abort, redirect, url_for, send_from_directory, jsonify
import flask
import requests
import json
from wordcloud import WordCloud, STOPWORDS

app = Flask(__name__)

@app.route('/')
def render_home():
    return app.send_static_file('index.html')

@app.route('/getNYTWordMap')
def getNYTWordMap():
    # assume we have a country string
    args = request.args.to_dict()
    country = args['country']
    

    # logic for getting the word map

    # let's go for something where we return a dictionary that maps a word to a count or something

    sample_wordmap = {'food': 100, 'dog': 30, 'computers': 57, 'bananas': 599}
    return json.dumps(sample_wordmap)


@app.route('/apiTester')
def testAPI():
    targ_country = 'Iran'

    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    queryParams = {
        'api-key' : "vi1B8sCbzyAYuJ7cJIBF5YfDDhdu2sfN",
        'begin_date' : "20210201",
        'end_date' : "20230201",
        'fq' : "Iran",
        'sort' : 'newest'
    }

    response = requests.get(url, params=queryParams)

    json_data = response.json()
    leading_paragraphs = ""
    documents = json_data['response']['docs']
    for article in documents:
        lead = article['lead_paragraph']
        
        if targ_country in lead:
            leading_paragraphs += " " + lead
            print(lead)

    print("\n", len(documents))
    ignored_bucket = set(STOPWORDS)
    words = leading_paragraphs.split(" ")
    cloud = {}
    for w in words:
        if w in ignored_bucket:
            continue
        if w in cloud:
            cloud[w] += 1
        else:
            cloud[w] = 1

    return json.dumps(cloud)
        
   # return response.json()


if __name__ == '__main__':
    render_home()
