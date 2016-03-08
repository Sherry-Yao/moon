#!/usr/bin/env python
# encoding: utf-8

import pymongo

class Database():
    def __init__(self, root='localhost', port=27017, db_name='moon'):
        self.connect(root, port, db_name)
        self.collection = None

    def connect(self, root, port, db_name):
        try:
            if int(pymongo.get_version_string()[0]) >= 3:
                connection = pymongo.MongoClient(root, port)
            else:
                connection = pymongo.Connection(root, port)
            self.db = connection[db_name]
        except pymongo.errors, e:
            print e

    def usecollection(self, collection):
        self.collection = self.db[collection]

    def getitemssum(self):
        try:
            if self.collection:
                return self.collection.count()
        except pymongo.errors, e:
            print e

        return

    def insertitem(self, conditions):
        try:
            if not self.QueryItems(conditions):
                return self.collection.insert(conditions)
        except pymongo.errors, e:
            print e

        return False

    def queryoneitem(self, conditions):
        try:
            if self.collection and type(conditions) is dict:
                item = self.collection.find_one(conditions)
                return item
        except pymongo.errors, e:
            print e

        return

    def queryitems(self, conditions):
        try:
            if self.collection and type(conditions) is dict:
                raw_items = self.collection.find(conditions)
                items = []
                for item in raw_items:
                    items.append(item)
                return items
        except pymongo.errors, e:
            print e

    def queryallitems(self):
        try:
            if self.collection:
                raw_items = self.collection.find()
                items = []
                for item in raw_items:
                    items.append(item)
                return items
        except pymongo.errors, e:
            print e

        return

    def updateitems(self, old_conditions, new_conditions):
        items = self.queryitems(old_conditions)
        try:
            if items:
                for item in items:
                    self.collection.remove(old_conditions)
                    self.collection.insert(new_conditions)

                return True
        except pymongo.errors, e:
            print e

        return False

    def deleteitems(self, conditions):
        try:
            items = self.queryitems(conditions)
            if items:
                self.collection.remove(conditions)
                return True
        except pymongo.errors, e:
            print e

        return False
