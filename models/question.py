#!/usr/bin/env python
# encoding: utf-8

from conf.database import Database
import random

class Question():
    #connect to db
    def __init__(self):
        self.db = Database()
        self.db.usecollection('questions')

    #get the sum of the collection questions in db
    def get_questions_sum(self):
        return self.db.getitemssum()

    #get the new question to play
    def get_new_question(self, gotten_questions):
        question_id = -1
        max_question_id = self.db.getitemssum() - 1
        while True:
            question_id = random.randint(0, max_question_id)
            if question_id not in gotten_questions:
                break
        new_question = self.db.queryoneitem({'id': question_id})

        return new_question

    #validate user's answer
    def validate_question(self, quest_id, answer):
        validate_question = self.db.queryoneitem({'id': quest_id})
        if int(answer) == validate_question['answer']:
            return True
        else:
            return False
