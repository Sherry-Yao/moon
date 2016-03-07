#!/usr/bin/env python
# encoding: utf-8

import tornado.web
from conf.session import Session
from models.question import Question

MAX_UNGET_QUESTION_SUM = 51
PASS_NUM = 5

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = Session(self.application.session_manager, self)
        if not self.session.has_key('quests_unget'):
            self.session['quests_unget'] = range(Question().get_questions_sum())
        if not self.session.has_key('quests_pass'):
            self.session['quests_pass'] = 0
        if not self.session.has_key('quest_id'):
            self.session['quest_id'] = -1
        self.session.save()
        print "init"
        print self.session['quests_unget']

    def get_current_quests(self):
        return self.session['quests_unget']

    def get_current_pass(self):
        return self.session['quests_pass']

    def get_current_id(self):
        return self.session['quest_id']

    def reset_current_quests(self):
        self.session['quests_unget'] = range(Question().get_questions_sum())
        self.session['quests_pass'] = 0
        self.session['quest_id'] = -1
        self.session.save()

    def sub_current_quests(self):
        if self.current_id in self.session['quests_unget']:
            self.session['quests_unget'].remove(self.session['quest_id'])
            self.session.save()

    def add_current_pass(self):
        self.session['quests_pass'] = self.session['quests_pass'] + 1
        self.session.save()

    def set_current_id(self, new_id):
        self.session['quest_id'] = new_id
        self.session.save()

    def is_game_pass(self):
        #if self.session['quests_pass'] > PASS_NUM:
        #    self.render('prize.html')
        #if len(self.session['quests_unget']) < MAX_UNGET_QUESTION_SUM:
        #    print self.session['quests_unget']
        #    self.render('fail.html')
        print "is"

    def write_response(self, error):
        print error
        return self.redirect('/')
