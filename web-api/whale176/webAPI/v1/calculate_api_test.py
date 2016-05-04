from calculate_api import app
import json
import unittest

__author__ = 'whale176'


class CalculateAPITest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_sum_success_with_both_int(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1&value2=1')
        self.assertEqual(json.loads(response.data), 2)

    def test_sum_success_with_both_float(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1.1&value2=1.2')
        self.assertEqual(json.loads(response.data), 2.3)

    def test_sum_success_with_float_int(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1.1&value2=2')
        self.assertEqual(json.loads(response.data), 3.1)

    def test_sum_success_with_float_int_1(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1.0&value2=2.0')
        self.assertEqual(json.loads(response.data), 3.0)

    def test_sum_fail_with_char_input(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1&value2=3r')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Variables should be integer.')

    def test_sum_fail_with_missing_necessary_var(self):
        tester = app.test_client(self)
        response = tester.get('/sum?value1=1')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Missing necessary variables input.')

    def test_minus_success_with_both_int(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1&value2=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 0)

    def test_minus_success_with_both_float(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1.1&value2=1.2')
        self.assertEqual(json.loads(response.data), -0.1)

    def test_minus_success_with_float_int(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1.1&value2=2')
        self.assertEqual(json.loads(response.data), -0.9)

    def test_minus_success_with_float_int_1(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1.0&value2=2.0')
        self.assertEqual(json.loads(response.data), -1.0)

    def test_minus_fail_with_char_input(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1&value2=3r')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Variables should be integer.')

    def test_minus_fail_with_missing_necessary_var(self):
        tester = app.test_client(self)
        response = tester.get('/minus?value1=1')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Missing necessary variables input.')

    def test_multiply_success_with_both_int(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1&value2=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 1)

    def test_multiply_success_with_both_float(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=2.5&value2=2.5')
        self.assertEqual(json.loads(response.data), 6.25)

    def test_multiply_success_with_float_int(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1.1&value2=2')
        self.assertEqual(json.loads(response.data), 2.2)

    def test_multiply_success_with_float_int_1(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1.0&value2=2.0')
        self.assertEqual(json.loads(response.data), 2.0)

    def test_multiply_fail_with_char_input(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1&value2=3r')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Variables should be integer.')

    def test_multiply_fail_with_missing_necessary_var(self):
        tester = app.test_client(self)
        response = tester.get('/multiply?value1=1')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Missing necessary variables input.')

    def test_divide_success_with_both_int(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1&value2=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), 1)

    def test_divide_success_with_both_float(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=6.25&value2=2.5')
        self.assertEqual(json.loads(response.data), 2.5)

    def test_divide_success_with_float_int(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=10.5&value2=2')
        self.assertEqual(json.loads(response.data), 5.25)

    def test_divide_success_with_float_int_1(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1.0&value2=2.0')
        self.assertEqual(json.loads(response.data), 0.5)

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
        self.assertEqual(response.data, 'Value2 could not be zero.')

    def test_divide_fail_with_char_input(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1&value2=a')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Variables should be integer.')

    def test_divide_fail_with_missing_necessary_var(self):
        tester = app.test_client(self)
        response = tester.get('/divide?value1=1')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.data, 'Missing necessary variables input.')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
