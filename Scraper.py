from pymongo import Connection
import praw
import pymongo
import unittest
import time

"""
Main class for pyReddit
"""
class Scraper(unittest.TestCase):

    # constructor of Scrapper object, creates a connection
    # to the mongodb server, and then pulls the first 100
    # posts on Reddit
    def __init__(self):
        self.userAgent = praw.Reddit(user_agent = 'pyReddit')
        self.mongoConnection = pymongo.MongoClient()
        self.dataBase = self.mongoConnection.reddit
        self.threads = self.dataBase.threads
        self.frontPagePosts = self.userAgent.get_front_page(limit = 100)
        self.assertTrue(self.dataBase == self.mongoConnection.reddit)

    # Inserts the posts gathered in the init into the mongo
    # database
    def getPosts(self):
        while True:
            self.threads.remove({})
            for posts in self.frontPagePosts:
                postContent = {}
                postContent['Title'] = posts.title
                postContent['Content'] = posts.selftext
                # Ensuring we are actually putting in content
                self.assertNotEqual(None, postContent)
                self.threads.insert(postContent)
                print("HERE")
                time.sleep(30)
