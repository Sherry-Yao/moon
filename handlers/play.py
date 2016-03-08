#!/usr/bin/env python
# encoding: utf-8

from base import BaseHandler
from models.question import Question

class PlayHandler(BaseHandler):
    def get(self):
        try:
            '''
            if pass < 6 or questions <= 10, web pages display the new question.
            else return the result.
            '''
            if self.is_game_continue():
                old_questions = self.get_old_quests()
                new_question = Question().get_new_question(old_questions)
                if new_question:
                    new_question['num'] = len(old_questions) + 1
                    return self.render('play.html', question = new_question)

                return self.redirect('/play')
        except:
            return self.write_response("Get new question Fail!")

    def post(self):
        try:
            '''
            validate the answer of the question.
            '''
            player_answer = self.get_argument('answer', None)
            cur_quest_id = self._get_argument('question_id', None)
            if player_answer and cur_quest_id:
                if Question().validate_question(cur_quest_id, player_answer):
                    self.add_current_pass()
                self.add_current_quests()

            if self.is_game_continue():
                return self.redirect('/play')
        except:
            return self.write_response("Validate new question Fail!")
