from flask import Flask, request, abort, redirect, url_for, send_from_directory, jsonify
import flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def render_home():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    render_home()
