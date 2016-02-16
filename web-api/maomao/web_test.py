import os
import web
import unittest
import tempfile
from lxml import etree

case = [
"/count?op={}&value1=1&value2=1", "/count?op={}&value1=52&value2=7",
"/count?op={}&value1=100.5&value2=33.1", "/count?op={}",
"/count?op={}&value1=1", "/count?op={}&value2=10",
"/count?op={}&value1=&value2=10", "/count?op={}&value1=kk&value2=1",
"/count?op={}&value1=9&value2=ss1", "/count?op={}&value1=9p&value2=121"
]

sum_answer = ["The Answer of 1 + 1 is 2.0", "The Answer of 52 + 7 is 59.0", "The Answer of 100.5 + 33.1 is 133.6"]
sum_answer += ["Missing values"]*4
sum_answer += ["Invalid values"]*3

minus_answer = ["The Answer of 1 - 1 is 0.0", "The Answer of 52 - 7 is 45.0", "The Answer of 100.5 - 33.1 is 67.4"]
minus_answer += ["Missing values"]*4
minus_answer += ["Invalid values"]*3

multiply_answer = ["The Answer of 1 * 1 is 1.0", "The Answer of 52 * 7 is 364.0", "The Answer of 100.5 * 33.1 is 3326.55"]
multiply_answer += ["Missing values"]*4
multiply_answer += ["Invalid values"]*3

divide_answer = ["The Answer of 1 / 1 is 1.0", "The Answer of 52 / 7 is 7.428571428571429", "The Answer of 100.5 / 33.1 is 3.036253776435045"]
divide_answer += ["Missing values"]*4
divide_answer += ["Invalid values"]*3

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        web.app.config['TESTING'] = True
        self.app = web.app.test_client()

    def test_sum(self):
        num = 0
        for c in case:
            rv = self.app.get(c.format("sum"))
            page = etree.HTML(rv.data)
            for i in page.xpath(u"//em"):
                assert i.text == sum_answer[num], "The Response of {} isn't correct.".format(c.format("sum"))
            num += 1

    def test_minus(self):
        num = 0
        for c in case:
            rv = self.app.get(c.format("minus"))
            page = etree.HTML(rv.data)
            for i in page.xpath(u"//em"):
                assert i.text == minus_answer[num], "The Response of {} isn't correct.".format(c.format("minus"))
            num += 1

    def test_multiply(self):
        num = 0
        for c in case:
            rv = self.app.get(c.format("multiply"))
            page = etree.HTML(rv.data)
            for i in page.xpath(u"//em"):
                assert i.text == multiply_answer[num], "The Response of {} isn't correct.".format(c.format("multiply"))
            num += 1

    def test_divide(self):
        num = 0
        for c in case:
            rv = self.app.get(c.format("divide"))
            page = etree.HTML(rv.data)
            for i in page.xpath(u"//em"):
                assert i.text == divide_answer[num], "The Response of {} isn't correct.".format(c.format("divide"))
            num += 1

        rv = self.app.get("/count?op=divide&value1=22&value2=0")
        page = etree.HTML(rv.data)
        for i in page.xpath(u"//em"):
            assert i.text == "Zero Division Error", "The Response of {} isn't correct.".format("/count?op=divide&value1=22&value2=0")

if __name__ == '__main__':
    unittest.main()