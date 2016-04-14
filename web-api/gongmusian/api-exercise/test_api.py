import os
import unittest
import api
# import flaskr
import json
import tempfile
from flask import Flask, jsonify
from api import app

class FlaskTestCase(unittest.TestCase):

    def test_sum_basic(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1&value2=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"status": 200,"sum": "2.00"})

    def test_sum_incorrect_value(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=a&value=2', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"Error":"Lose Key","status": 406})

    def test_sum_missing_value(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"Error":"Lose Key","status": 406})

    def test_minus_basic(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1&value2=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"minus":"0.00","status": 200})

    def test_minus_incorrect_value(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=a&value=2', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"Error":"Lose Key","status": 406})

    def test_minus_missing_value(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"Error": "Lose Key","status": 406})

    def test_multiply_basic(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1&value2=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"multiply": "1.00","status": 200})

    def test_multiply_incorrect_value(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=a&value=2', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), { "Error":"Lose Key","status": 406})

    def test_multiply_missing_value(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"Error": "Lose Key",
  "status": 406})

    def test_divide_basic(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1&value2=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"divide": "1.00","status": 200})

    def test_divide_incorrect_value(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=a&value=2', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), { "Error": "Lose Key","status": 406})

    def test_divide_missing_value(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), {"Error": "Lose Key","status": 406})

    def test_divide_zero_value(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1&value2=0', content_type='application/json')
        self.assertEqual(json.loads(response.data.decode('utf-8')), { "Error": "Value2 shold not be zero!","status": 200})

if __name__ == '__main__':
    unittest.main()
