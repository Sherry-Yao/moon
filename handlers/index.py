#!/usr/bin/env python
# encoding: utf-8

from base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        self.is_game_pass()
        self.reset_current_quests()
        return self.render('index.html')
