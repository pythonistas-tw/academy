import os
import api
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def test_sum(self):
    	# test correct
        rv = self.app.get('/sum?value1=1&value2=1')
        assert rv.data == b'2.0'

        rv = self.app.get('/sum?value1=52&value2=7')
        assert rv.data == b'59.0'

        rv = self.app.get('/sum?value1=100.5&value2=33.1')
        assert rv.data == b'133.6'

        # test missing
        rv = self.app.get('/sum?value1=1')
        assert rv.data == b'Missing values'

        rv = self.app.get('/sum?value2=10')
        assert rv.data == b'Missing values'

        rv = self.app.get('/sum')
        assert rv.data == b'Missing values'

        rv = self.app.get('/sum?value1=&value2=8')
        assert rv.data == b'Missing values'

        # test invalid
        rv = self.app.get('/sum?value1=kk&value2=1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/sum?value1=9&value2=ss1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/minus?value1=p9&value2=121')
        assert rv.data == b'Invalid values'

    def test_minus(self):
    	# test correct
        rv = self.app.get('/minus?value1=1&value2=1')
        assert rv.data == b'0.0'

        rv = self.app.get('/minus?value1=52&value2=7')
        assert rv.data == b'45.0'

        rv = self.app.get('/minus?value1=100.5&value2=33.1')
        assert rv.data == b'67.4'

        # test missing
        rv = self.app.get('/minus?value1=1')
        assert rv.data == b'Missing values'

        rv = self.app.get('/minus?value2=10')
        assert rv.data == b'Missing values'

        rv = self.app.get('/minus')
        assert rv.data == b'Missing values'

        rv = self.app.get('/minus?value1=&value2=8')
        assert rv.data == b'Missing values'

        # test invalid
        rv = self.app.get('/minus?value1=kk&value2=1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/minus?value1=9&value2=ss1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/minus?value1=p9&value2=121')
        assert rv.data == b'Invalid values'

    def test_multiply(self):
    	# test correct
        rv = self.app.get('/multiply?value1=1&value2=1')
        assert rv.data == b'1.0'

        rv = self.app.get('/multiply?value1=52&value2=7')
        assert rv.data == b'364.0'

        rv = self.app.get('/multiply?value1=100.5&value2=33.1')
        assert rv.data == b'3326.55'

        # test missing
        rv = self.app.get('/multiply?value1=1')
        assert rv.data == b'Missing values'

        rv = self.app.get('/multiply?value2=10')
        assert rv.data == b'Missing values'

        rv = self.app.get('/multiply')
        assert rv.data == b'Missing values'

        rv = self.app.get('/multiply?value1=&value2=8')
        assert rv.data == b'Missing values'

        # test invalid
        rv = self.app.get('/multiply?value1=kk&value2=1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/multiply?value1=9&value2=ss1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/multiply?value1=p9&value2=121')
        assert rv.data == b'Invalid values'

    def test_divide(self):
        # test correct
        rv = self.app.get('/divide?value1=1&value2=1')
        assert rv.data == b'1.0'

        rv = self.app.get('/divide?value1=10&value2=4')
        assert rv.data == b'2.5'

        rv = self.app.get('/divide?value1=52&value2=7')
        assert rv.data == b'7.428571428571429'

        rv = self.app.get('/divide?value1=100.5&value2=33.1')
        assert rv.data == b'3.036253776435045'

        # test missing
        rv = self.app.get('/divide?value1=1')
        assert rv.data == b'Missing values'

        rv = self.app.get('/divide?value2=10')
        assert rv.data == b'Missing values'

        rv = self.app.get('/divide')
        assert rv.data == b'Missing values'

        rv = self.app.get('/divide?value1=&value2=8')
        assert rv.data == b'Missing values'

        # test invalid
        rv = self.app.get('/divide?value1=kk&value2=1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/divide?value1=9&value2=ss1')
        assert rv.data == b'Invalid values'

        rv = self.app.get('/divide?value1=p9&value2=121')
        assert rv.data == b'Invalid values'


if __name__ == '__main__':
    unittest.main()