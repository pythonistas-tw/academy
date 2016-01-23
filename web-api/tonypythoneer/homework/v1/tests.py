#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @first_date    20151230
#  @date          20151230
import unittest
import operator

from flask import json

from api import app


class ApiTestCase(unittest.TestCase):
    key_pair = ('value1', 'value2')

    def calculate_result(self, value1, value2, op):
        return op(value1, value2)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_sum(self):
        # Initial process
        val_pair = (1.5, 3.5)
        val_map = dict(zip(self.key_pair, val_pair))
        result = self.calculate_result(op=operator.add, **val_map)

        # Request process
        res = self.app.get('/sum', query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data.get('result', ''), result)
        self.assertEqual(res.status_code, 200)

    def test_minus(self):
        # Initial process
        val_pair = (6.5, 3.5)
        val_map = dict(zip(self.key_pair, val_pair))
        result = self.calculate_result(op=operator.sub, **val_map)

        # Request process
        res = self.app.get('/minus', query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data.get('result', ''), result)
        self.assertEqual(res.status_code, 200)

    def test_multiply(self):
        # Initial process
        val_pair = (6.5, 6)
        val_map = dict(zip(self.key_pair, val_pair))
        result = self.calculate_result(op=operator.mul, **val_map)

        # Request process
        res = self.app.get('/multiply', query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data.get('result', ''), result)
        self.assertEqual(res.status_code, 200)

    def test_divide(self):
        # Initial process
        val_pair = (9, 1.5)
        val_map = dict(zip(self.key_pair, val_pair))
        result = self.calculate_result(op=operator.div, **val_map)

        # Request process
        res = self.app.get('/divide', query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertEqual(data.get('result', ''), result)
        self.assertEqual(res.status_code, 200)

    def test_enter_non_number_as_value(self):
        # Initial process
        val_pair = ("hello", "world")
        val_map = dict(zip(self.key_pair, val_pair))

        # Request process
        res = self.app.get('/sum', query_string=val_map)
        data = json.loads(res.data)

        # Assert process
        self.assertTrue("Not a valid float value" in data.get('value1', ''))
        self.assertTrue("Not a valid float value" in data.get('value2', ''))
        self.assertEqual(res.status_code, 400)

if __name__ == '__main__':
    unittest.main()
