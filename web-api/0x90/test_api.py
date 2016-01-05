import unittest
from flask import json
import api


class FlaskrTestCase(unittest.TestCase):
    def requestURL_maker(self, operatior, value1, value2):
        url_result = ''
        if operatior != '':
            url_result = '/' + operatior
        if value1 != '':
            url_result = url_result + '?value1=' + value1
        if value2 != '':
            if value1 != '':
                url_result = url_result + '&value2=' + value2
            else:
                url_result = url_result + '?value2=' + value2
        return url_result

    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    # sum
    def test_sun_correct_case(self):
        requestURL = self.requestURL_maker('sum', '2000', '16')
        rv = self.app.get(requestURL)
        data = json.loads(rv.data)
        self.assertEqual(
            data['status'],
            'ok',
            'Correct values testing of sum Failed, status: ' + data['status'])
        self.assertEqual(
            data['data'],
            '2016.0',
            'Correct values testing of sum Failed, data: ' + data['data'])

    def test_sun_missing_case(self):
        requestURL = self.requestURL_maker('sum', '', '2015')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Missing values testing of sum Failed")

    def test_sun_invalid_case(self):
        requestURL = self.requestURL_maker('sum', 'Merry', '1225')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Invalid values testing of sum Failed")

    # minus
    def test_minus_correct_case(self):
        requestURL = self.requestURL_maker('minus', '2048', '32')
        rv = self.app.get(requestURL)
        data = json.loads(rv.data)
        self.assertEqual(
            data['status'],
            'ok',
            'Correct values testing of minus Failed, status: ' + data['status'])
        self.assertEqual(
            data['data'],
            '2016.0',
            'Correct values testing of minus Failed, data: ' + data['data'])

    def test_minus_missing_case(self):
        requestURL = self.requestURL_maker('minus', '', '2015')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Missing values testing of minus Failed")

    def test_minus_invalid_case(self):
        requestURL = self.requestURL_maker('minus', 'X mas', '1225')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Invalid values testing of minus Failed")

    # multiply
    def test_multiply_correct_case(self):
        requestURL = self.requestURL_maker('multiply', '126', '16')
        rv = self.app.get(requestURL)
        data = json.loads(rv.data)
        self.assertEqual(
            data['status'],
            'ok',
            'Correct values testing of multiply Failed, status: ' + data['status'])
        self.assertEqual(
            data['data'],
            '2016.0',
            'Correct values testing of multiply Failed, data: ' + data['data'])

    def test_multiply_missing_case(self):
        requestURL = self.requestURL_maker('multiply', '', '2016')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Missing values testing of multiply Failed")

    def test_multiply_invalid_case(self):
        requestURL = self.requestURL_maker('multiply', 'happy', '11')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Invalid values testing of multiply Failed")

    # divide
    def test_divide_correct_case(self):
        requestURL = self.requestURL_maker('divide', '10080', '5')
        rv = self.app.get(requestURL)
        data = json.loads(rv.data)
        self.assertEqual(
            data['status'],
            'ok',
            'Correct values testing of divide Failed, status: ' + data['status'])
        self.assertEqual(
            data['data'],
            '2016.0',
            'Correct values testing of divide Failed, data: ' + data['data'])

    def test_divide_missing_case(self):
        requestURL = self.requestURL_maker('divide', '', '2016')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Missing values testing of divide Failed")

    def test_divide_invalid_case(self):
        requestURL = self.requestURL_maker('divide', 'new year ', '11')
        rv = self.app.get(requestURL)
        self.assertIn(
            '<title>406 Not Acceptable</title>', rv.data,
            "Invalid values testing of divide Failed")

if __name__ == '__main__':
    unittest.main()
