#!/usr/bin/env python
# encoding: utf-8

from conf.database import Database
import random

class Question():
    def __init__(self):
        self.db = Database()
        self.db.use_collection('questions')

    def get_questions_sum(self):
        return self.db.getitemssum()

    def get_new_question(self, questions):
        new_question_id = random.randint(0, len(questions))
        new_question = self.db.queryoneitem({'id': new_question_id})
        return new_question

    def validate_question(self, quest_id, answer):
        validate_question = self.db.queryoneitem({'id': quest_id})
        if answer == validate_question['answer']:
            return True
        else:
            return False
