#!/usr/bin/env python3
from Scraper import Scraper
import unittest
import os
import sys

app.debug = True
pyReddit = Scraper()
fpid = os.fork()

class test(unittest.TestCase):
    def test(self):
        pyReddit.getPosts()
        
def main():
    if fpid!=0:
        sys.exit(0)
    unittest.main()

if __name__ == "__main__" :
    main()
