#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
import os, sys
import pymongo
from Scraper import Scraper

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    pyReddit = Scraper()
    postCollectionContainer = pyReddit.dataBase.threads.find()
    postCollection = [post for post in postCollectionContainer]
    return render_template('template.html', postCollection = postCollection)

if __name__ == '__main__':
    app.run()
