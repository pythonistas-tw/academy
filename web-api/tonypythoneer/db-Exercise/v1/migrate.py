#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160121
#  @date          20160121
"""migrate
"""
from db_connector import DbConnecter
from models import Base


if __name__ == "__main__":
    db_connecter = DbConnecter()
    db_connecter.init_db(base=Base)
