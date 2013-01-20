import unittest
from thinkstats.thinkstats import Mean

class TestThinkstats(unittest.TestCase):
    
    def setUp(self):
    	pass
    
    def test_mean_should_find_mean_value_in_list_of_numbers(self):
    	numbers = [4.0, 5.0, 6.0]
    	self.assertEqual(5.0, Mean(numbers))