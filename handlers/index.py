#!/usr/bin/env python
# encoding: utf-8

from base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        '''
        if the user passed the game, return the lottery;
        and if he failed and didn;t choose to play again, web page will stay in the result html;
        else it's mean that the user can continue to play the game, including the first time.
        '''
        if self.is_game_continue():
            return self.render('index.html')
