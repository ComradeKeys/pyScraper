from pymongo import Connection
import praw
import pymongo
import unittest
import sys
import os

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
        self.assertTrue(self.dataBase == self.mongoConnection.reddit)



    # Inserts the posts gathered in the init into the mongo
    # database
    def getPosts(self):
        self.threads.remove({})
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
    def printContent(self):
        for d in self.threads.find()[:200]:
            print(d)
