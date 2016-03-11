#!/usr/bin/env python3
from Scraper import Scraper
import unittest
import Flask

class test(unittest.TestCase):
    def test(self):
        pyReddit = Scraper()
        pyReddit.getPosts()
        pyReddit.postContent()

def main():
    unittest.main()

"""
debug = True gives us really helpful debug information
and a stack trace in our browser, it also autoregenerates
so the webpage refreshes on it's own
"""
if __name__ == "__main__" :
    main()
    app.run(debug = True)
