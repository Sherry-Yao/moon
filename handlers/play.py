#!/usr/bin/env python
# encoding: utf-8

from base import BaseHandler
from models.question import Question

class PlayHandler(BaseHandler):
    def get(self):
        try:
            self.is_game_pass()
            unget_questions = self.get_current_quests()
            new_question = Question().get_question(unget_questions)
            if new_question:
                new_question['num'] = Question().get_sum() - len(unget_questions) + 1
                self.set_current_id(new_question['id'])
                return self.render('play.html', new_question)

            return self.redirect('/play')
        except:
            return self.write_response("Get new question Fail!")

    def post(self):
        try:
            player_answer = self.get_argument('answer', None)
            if player_answer:
                cur_quest_id = self.get_current_id()
                if Question().validate_question(cur_quest_id, player_answer):
                    self.add_current_pass()
                self.sub_current_quests()
            self.is_game_pass()
            return self.redirect('/play')
        except:
            return self.write_response("Validate new question Fail!")
