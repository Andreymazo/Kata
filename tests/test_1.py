import unittest

from main import rimsk_to_arab

class TestSum(unittest.TestCase):

    def test_rimsk_to_arab(self):
        data1 = [2, 2]
        data2 = ['+']#lst_nums, list_of_actions
        result = rimsk_to_arab(data1, data2)
        self.assertEqual(result, ('smth', ['+']))
      #python -m unittest discover -p 'test_1.py'# start test

if __name__ == '__main__':
    unittest.main()