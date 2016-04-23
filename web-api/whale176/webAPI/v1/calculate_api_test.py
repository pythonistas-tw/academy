from calculate_api import app
import json
import unittest

__author__ = 'whale176'


class CalculateAPITest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_sum_success(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1&value2=1')
        self.assertEqual(json.loads(response.data), 2)

    def test_minus_success(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1&value2=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 0)

    def test_multiply_success(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1&value2=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 1)

    def test_divide_success_when_result_is_integer(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1&value2=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 1)

    def test_divide_success_when_result_is_float(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=10&value2=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 2.5)

    def test_divide_fail_with_invalidate_denominator(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1&value2=0')
        # pprint.pprint(response)
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, '[Invalid input] value2 could not be zero.')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
