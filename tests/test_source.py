import unittest

from app.models import Source,Article

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
        self.new_source = Source("cnn",'CNN','Your dedicated news source','general','US',"link")

    def test_init(self):
        """
        This will test whether a source object is initialized correctly
        """
        self.assertTrue(isinstance(self.new_source,Source))

class ArticleTest(unittest.TestCase):
    """
    This will test all the behaviours of the Article class
    
    Args: 
        unittest.TestCase: This is a class in the unittest module where we inherit the testing tools
    """
    def setUp(self):
        """
        This will run before every test in the class is run
        """
        self.new_article = Article('cnn','Ken Mbira','Blinding lights','A tale of two dollars','htttps://blah','link to image','2/4/5')

    def test_init(self):
        """
        This will check if the article objects are being instantiated correctly
        """
        self.assertTrue(isinstance(self.new_article,Article))

    def test_save_article(self):
        """
        This test will check if we can save a news article
        """
        self.new_article.save_article()
        self.assertEqual(len(Article.article_findings),1)