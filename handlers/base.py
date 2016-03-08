#!/usr/bin/env python
# encoding: utf-8

import tornado.web
from conf.session import Session
from models.lottery import Lottery

PASS_NUM = 6
MAX_QUEST_NUM = 10

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = Session(self.application.session_manager, self)

    def reset_current_quests(self):
        self.session['quests_get'] = []
        self.session['quests_pass'], self.session['reset'] = 0
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
        # if win, directly turn to Lottery
        if self.session.has_key('win_code'):
            self.render('prize.html',
                    code = Lottery().get_code(self.session.session_id))
            return False

        # neither win or first time to play
        if self.session.has_key('reset') and self.session.has_key('quests_get') \
            and self.session.has_key('quests_pass'):

            # replay
            if self.session['reset'] == 1:
                self.reset_current_quests()
                return True
            # finally pass
            if self.session['quests_pass'] >= PASS_NUM:
                del self.session['reset'], self.session['quests_get'], \
                        self.session['quests_pass']
                self.session['win_code'] = \
                        Lottery().gen_code(self.session.session_id)
                self.session.save()
                self.render('prize.html', code=self.session['win_code'])
                return False
            # Up to max num of allow questions once
            if len(self.session['quests_get']) >= MAX_QUEST_NUM:
                self.session['reset'] = 1
                self.session.save()
                self.render('fail.html')
                return False

        # first time to play
        else:
            self.reset_current_quests()

        return True

    def write_response(self, error):
        print error
        return self.redirect('/')
