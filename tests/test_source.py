import unittest

from app import models
Source = models.Source

class SourceTest(unittest.TestCase):
    """
    This will test all the behaviours of the Source class
    
    Args: 
        unittest.TestCase: This is a class in the unittest module where we inherit the testing tools
    """
    def setUp(self):
        """
        This function will run before every test case does
        """
        self.new_source = Source('cnn','CNN','Your dedicated news source','general','US')

    def test_init(self):
        """
        This will test whether a source object is initialized correctly
        """
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()