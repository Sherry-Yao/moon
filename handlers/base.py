#!/usr/bin/env python
# encoding: utf-8

import tornado.web
from conf.session import Session

PASS_NUM = 6
MAX_QUEST_NUM = 10

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = Session(self.application.session_manager, self)

    def reset_current_quests(self):
        self.session['quests_get'] = []
        self.session['quests_pass'] = 0
        self.session['reset'] = 0
        self.session.save()

    def get_old_quests(self):
        return self.session['quests_get']

    def add_current_quests(self, quest_id):
        if quest_id not in self.session['quests_get']:
            self.session['quests_get'].append(quest_id)
            self.session.save()

    # add the num of pass questions
    def add_current_pass(self):
        self.session['quests_pass'] = self.session['quests_pass'] + 1
        self.session.save()

    # judge if player can continue to play
    def is_game_continue(self):
        if self.session.has_key('reset') and self.session.has_key('quests_get') \
            and self.session.has_key('quests_pass'):
            if self.session['reset'] == 1:
                self.reset_current_quests()
                return True
            if self.session['quests_pass'] >= PASS_NUM:
                self.render('prize.html')
                return False
            if len(self.session['quests_get']) >= MAX_QUEST_NUM:
                self.session['reset'] = 1
                self.session.save()
                self.render('fail.html')
                return False
        else:
            self.reset_current_quests()

        return True

    def write_response(self, error):
        print error
        return self.redirect('/')
