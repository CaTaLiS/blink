import unittest
from blink.blink import get_delay_in_sec

class TestBlink(unittest.TestCase):
    
    def test_set_correct_delay_param(self):
        # given
        given_delay = 0.5
        expected_delay = 0.5
        
        # when
        result = get_delay_in_sec(given_delay)
        
        # then
        self.assertEquals(result, expected_delay)
        
    def test_set_to_default_if_empty(self):
        # given
        expected_delay = 1
        
        # when
        result = get_delay_in_sec(None)
        
        # then
        self.assertEquals(result, expected_delay)
        
    def test_set_to_default_if_not_float(self):
        # given
        expected_delay = 1
        
        # when
        result = get_delay_in_sec('delay')
        
        # then
        self.assertEquals(result, expected_delay)
        
    if __name__ == '__main__':
        unittest.main()


