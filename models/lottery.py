#!/usr/bin/env python
# encoding: utf-8

from conf.database import Database

class Lottery():
    #connect to db
    def __init__(self):
        self.db = Database()
        self.db.usecollection('codes')

    def gen_code(self, session_id):
        code_unget = self.db.queryoneitem({"s_id": 0})
        self.db.updateitems(code_unget,
                {"s_id": session_id, "code": code_unget['code']})
        print code_unget
        return code_unget['code']

    def get_code(self, session_id):
        win_code = self.db.queryoneitem({"s_id": session_id})

        return win_code['code']
