#!/usr/bin/env python3
from Scraper import Scraper
import unittest
from flask import Flask, render_template
import time

app = Flask(__name__)
app.debug = True
pyReddit = Scraper()

class test(unittest.TestCase):
    def test(self):
        pyReddit.getPosts()
        app.run()

@app.route("/")
def index():
    _items = pyReddit.dataBase.threads.find()
    items = [item for item in _items]
    return render_template('template.html', items=items)

def main():
    unittest.main()

"""
debug = True gives us really helpful debug information
and a stack trace in our browser, it also autoregenerates
so the webpage refreshes on it's own
"""
if __name__ == "__main__" :
    main()
