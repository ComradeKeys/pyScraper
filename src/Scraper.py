from pymongo import Connection
import praw
import pymongo
import unittest
from flask import Flask
app = Flask(__name__)

"""
Main class for pyReddit
"""
class Scraper(unittest.TestCase):

    # constructor of Scrapper object, creates a connection
    # to the mongodb server, and then pulls the first 100
    # posts on Reddit
    # MongoDB server broke, I need to move this to HEWA
    # server so unit test stops failing
    def __init__(self):
        self.userAgent = praw.Reddit(user_agent = 'pyReddit')
        self.mongoConnection = pymongo.MongoClient()
        self.dataBase = self.mongoConnection.reddit
        self.threads = self.dataBase.threads
        self.frontPagePosts = self.userAgent.get_front_page(limit = 100)
        self.assertTrue(self.database == self.mongoConnectoin.reddit)

if __name__ == "__main__":
    # Inserts the posts gathered in the init into the mongo
    # database
    def getPosts(self):
        for posts in self.frontPagePosts:
            postContent = {}
            postContent['Title'] = posts.title
            postContent['Content'] = posts.selftext
            # Ensuring we are actually putting in content
            self.assertNotEqual(None, postContent)
            self.threads.insert(postContent)

    # Pulls from the database and puts it into Flask,
    # looks horribly ugly I should probably not use the
    # newline like this. There should be a template for this
    app.route("/")
    def postContent(self):
        content = {}
        for d in self.threads.find()[:200]:
            content = content + "\n" + d + "\n"
        return content
