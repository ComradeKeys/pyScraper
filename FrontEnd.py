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
    _items = pyReddit.dataBase.threads.find()
    items = [item for item in _items]
    return render_template('template.html', items=items)

if __name__ == '__main__':
    app.run()
