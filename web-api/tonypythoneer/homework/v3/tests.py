#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20160101
#  @date          20160101
"""unittest practice

This is a list about api:

| value1 | value2 | meaning                             |
|--------|--------|-------------------------------------|
| 0      | 0      | correct_value1_and_value2           |
| 1      | 0      | incorrect_value1_and_correct_value2 |
| 2      | 0      | missing_value1_and_correct_value2   |
| 0      | 1      | correct_value1_and_incorrect_value2 |
| 1      | 1      | incorrect_value1_and_value2         |
| 2      | 1      | missing_value1_and_incorrect_value2 |
| 0      | 2      | correct_value1_and_missing_value2   |
| 1      | 2      | incorrect_value1_and_missing_value2 |
| 2      | 2      | missing_value1_and_value2           |
"""
from copy import copy
import unittest
import operator

from flask import json, url_for

from api import app


class CommonTestCase(object):
    val_map = {'value1': 9, 'value2': 1.5}

    def calculate_result(self, value1, value2, op):
        return op(value1, value2)

    def test_correct_value1_and_value2(self):
        '''#1'''
        # Initial process
        val_map = self.val_map
        result = self.calculate_result(op=self.op, **val_map)

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['result'], result)
        self.assertEqual(res.status_code, 200)

    def test_incorrect_value1_and_correct_value2(self):
        '''#2'''
        # Initial process
        val_map = copy(self.val_map)
        value1 = "This is a string"
        val_map["value1"] = value1

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value1'], 
                         "could not convert string to float: %s" % value1)
        self.assertEqual(res.status_code, 400)

    def test_missing_value1_and_correct_value2(self):
        '''#3'''
        # Initial process
        val_map = copy(self.val_map)
        del val_map["value1"]

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value1'], 
                         "Missing required parameter in the query string")
        self.assertEqual(res.status_code, 400)

    def test_correct_value1_and_incorrect_value2(self):
        '''#4'''
        # Initial process
        val_map = copy(self.val_map)
        value2 = "This is a string"
        val_map["value2"] = value2

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value2'],
                         "could not convert string to float: %s" % value2)
        self.assertEqual(res.status_code, 400)

    def test_incorrect_value1_and_value2(self):
        '''#5'''
        # Initial process
        val_map = copy(self.val_map)
        value1 = "This is a string"
        val_map['value1'] = value1
        value2 = "This is a string"
        val_map['value2'] = value2


        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value1'],
                         "could not convert string to float: %s" % value1)
        self.assertEqual(data['message']['value2'],
                         "could not convert string to float: %s" % value2)
        self.assertEqual(res.status_code, 400)

    def test_missing_value1_and_incorrect_value2(self):
        '''#6'''
        # Initial process
        val_map = copy(self.val_map)
        del val_map["value1"]
        value2 = "This is a string"
        val_map['value2'] = value2

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value1'],
                         "Missing required parameter in the query string")
        self.assertEqual(data['message']['value2'],
                         "could not convert string to float: %s" % value2)
        self.assertEqual(res.status_code, 400)


    def test_correct_value1_and_missing_value2(self):
        '''#7'''
        # Initial process
        val_map = copy(self.val_map)
        del val_map["value2"]

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value2'],
                         "Missing required parameter in the query string")
        self.assertEqual(res.status_code, 400)

    def test_incorrect_value1_and_missing_value2(self):
        '''#8'''
        # Initial process
        val_map = copy(self.val_map)
        value1 = "This is a string"
        val_map["value1"] = value1
        del val_map["value2"]

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value1'],
                         "could not convert string to float: %s" % value1)
        self.assertEqual(data['message']['value2'],
                         "Missing required parameter in the query string")
        self.assertEqual(res.status_code, 400)

    def test_missing_value1_and_value2(self):
        '''#9'''
        # Initial process
        val_map = copy(self.val_map)
        del val_map["value1"]
        del val_map["value2"]

        # Request process
        res = self.app.get(self.api_url, query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data['message']['value1'],
                         "Missing required parameter in the query string")
        self.assertEqual(data['message']['value2'],
                         "Missing required parameter in the query string")
        self.assertEqual(res.status_code, 400)


class SumTestCase(CommonTestCase, unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        with app.test_request_context():
            self.api_url = url_for('sum')

        self.op = operator.add


class SumTestCase(CommonTestCase, unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        with app.test_request_context():
            self.api_url = url_for('sum')

        self.op = operator.add


class MinusTestCase(CommonTestCase, unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        with app.test_request_context():
            self.api_url = url_for('minus')

        self.op = operator.sub


class MultiplyTestCase(CommonTestCase, unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        with app.test_request_context():
            self.api_url = url_for('multiply')

        self.op = operator.mul


class DivideTestCase(CommonTestCase, unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        with app.test_request_context():
            self.api_url = url_for('divide')

        self.op = operator.div

if __name__ == '__main__':
    unittest.main()
