import os
import api
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, api.app.config['DATABASE'] = tempfile.mkstemp()
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(api.app.config['DATABASE'])
#-------------------------------#
#-------- sum unit test
    def test_sum_value(self):
        rv = self.app.get('/sum?value1=1&value2=1')
        assert '2' in rv.data    
        rv = self.app.get('/sum?value1=2&value2=1')
        assert '3.00' in rv.data
    def test_sum_miss(self):
        rv = self.app.get('/sum?value1=1')
        assert '406 Error' in rv.data
    def test_sum_invalid(self):
        rv = self.app.get('/sum?value1=a&value=2')
        assert '406 Error' in rv.data
#-------------------------------#
#-------- minus unit test
    def test_minus_value(self):
        rv = self.app.get('/minus?value1=50&value2=1')
        assert '49.00' in rv.data    
        rv = self.app.get('/minus?value1=20&value2=30')
        assert '-10' in rv.data
        rv = self.app.get('/minus?value1=2.5&value2=1.22')
        assert '1.28' in rv.data
    def test_minus_miss(self):
        rv = self.app.get('/minus?value1=1')
        assert '406 Error' in rv.data
    def test_minus_invalid(self):
        rv = self.app.get('/minus?value1=a&value=2')
        assert '406 Error' in rv.data
#-------------------------------#
#-------- multiply unit test
    def test_multiply_value(self):
        rv = self.app.get('/multiply?value1=50&value2=1')
        assert '50.00' in rv.data    
        rv = self.app.get('/multiply?value1=1.33&value2=30')
        assert '39.9' in rv.data
        rv = self.app.get('/multiply?value1=2.5&value2=1.22')
        assert '3' in rv.data
#-------------------------------#
#-------- dividex unit test

if __name__ == '__main__':
    unittest.main()