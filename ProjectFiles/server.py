from flask import Flask, request, abort, redirect, url_for, send_from_directory, jsonify
import flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def render_home():
    return app.send_static_file('index.html')

@app.route('/getNYTWordMap')
def getNYTWordMap():
    # logic for getting the word map

    # let's go for something where we return a dictionary that maps a word to a count or something

    sample_wordmap = {'food': 100, 'dog': 30, 'computers': 57, 'bananas': 599}
    return json.dumps(sample_wordmap)


if __name__ == '__main__':
    render_home()
