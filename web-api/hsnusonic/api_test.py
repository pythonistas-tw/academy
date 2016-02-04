import api

import unittest
from operator import add, truediv, sub, mul

class ApiTestCase(unittest.TestCase):
  OpMap = {"sum":add, "minus":sub, "multiply":mul, "divide":truediv}

  def setUp(self):
    self.app = api.app.test_client();

  def template(self, op, value):
    """build test case for each operator
    """
    url = '/{0}?'.format(op)
    accept = True
    for i, v in enumerate(value, 1):
      try:
        v = float(v)
        url += "value{0}={1}&".format(i,v)
      except (ValueError, TypeError):
        accept = False
    # get response
    rv = self.app.get(url)
    if accept:
      ans = float(self.OpMap[op](*value))
      assert str(ans) == rv.data
    else:
      assert "406 Not Acceptable" in rv.data

  def test_sum_correct(self):
    self.template("sum", [32767, 32767])

  def test_sum_missing(self):
    self.template("sum", [1, None])
    self.template("sum", [None, 1])

  def test_sum_invalid(self):
    self.template("sum", ["a", 1])
    self.template("sum", [1, "a"])

  def test_minus_correct(self):
    self.template("minus", [32767, 32768])

  def test_minus_missing(self):
    self.template("minus", [1, None])
    self.template("minus", [None, 1])

  def test_minus_invalid(self):
    self.template("minus", ["a", 1])
    self.template("minus", [1, "a"])

  def test_multiply_correct(self):
    self.template("multiply", [32767, 32767])

  def test_multiply_missing(self):
    self.template("multiply", [1, None])
    self.template("multiply", [None, 1])

  def test_multiply_invalid(self):
    self.template("multiply", ["a", 1])
    self.template("multiply", [1, "a"])

  def test_divide_correct(self):
    self.template("divide", [32767, 1024])

  def test_divide_missing(self):
    self.template("divide", [1, None])
    self.template("divide", [None, 1])

  def test_divide_invalid(self):
    self.template("divide", ["a", 1])
    self.template("divide", [1, "a"])

if __name__ == "__main__":
  unittest.main()
