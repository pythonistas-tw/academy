#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""DbConnecter
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DbConnecter(object):
    dbname = 'sqlite:///example.sqlite'

    def __init__(self):
        self._connect_db()
        self._create_session()

    def _connect_db(self):
        self.engine = create_engine(self.dbname)

    def _create_session(self):
        self.session = scoped_session(sessionmaker())
        self.session.configure(bind=self.engine)

    def get_session(self):
        return self.session

    def init_db(self, base):
        base.metadata.drop_all(self.engine)
        base.metadata.create_all(self.engine)
