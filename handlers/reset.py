#!/usr/bin/env python
# encoding: utf-8

from base import BaseHandler

class ResetHandler(BaseHandler):
    def get(self):
        self.session.clear()
        self.session.save()
        return self.redirect("/")
