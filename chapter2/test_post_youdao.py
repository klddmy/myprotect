import unittest 
import mock
from post_youdao import *


class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        # import time
        # t=time.time()
        # ts=str(int(round(t * 1000)))
        # print(ts)
        get_ts=mock.Mock(return_value= '1584684946402')
        self.assertEqual('1584684946402',get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15846849464028')
        self.assertEqual('15846849464028',get_salt())

    def test_get_sign(self):
        get_sign = mock.Mock(return_value='c0602e8a7ec7eface095889cad4926f0')
        self.assertEqual('c0602e8a7ec7eface095889cad4926f0',get_sign())

if __name__ == '__main__':
    unittest.main()
