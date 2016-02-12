import os
import api
import unittest
import tempfile

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()

    def tearDown(self):
    	pass

    def test_simple_alrithmatic(self):
        operation_list=["sum","minus","multiply","divide"]
        correct_values_results_list=[2,0,1,1]
        for operation,correct_value_results in zip(operation_list, correct_values_results_list):
        	# correct case
            value = self.app.get("/"+operation+"?value1=1&value2=1")
            if float(value.data.decode())==correct_value_results:
            	print(operation+": correct case success")
            else:
            	assert operation+": correct case wrong"
            # missing values
            value = self.app.get("/"+operation+"?value1=1")
            if value.status_code==406:
                print(operation+": missing values wrong case success")
            else:
                assert operation+": missing values wrong case wrong"
            # missing values
            value = self.app.get("/"+operation+"?value1=a&value=2")
            if value.status_code==406:
                print(operation+": invalid values wrong case success")
            else:
                assert operation+": invalid values wrong case wrong"

if __name__ == '__main__':
    unittest.main()