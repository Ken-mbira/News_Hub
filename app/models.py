class Source:
    """
    This will define everything to do with sources
    """
    def __init__(self,id,name,description,category,country,link):
        """
        This will define all the properties of the source class
        
        Args:
            id: The id of the news source
            name: The name of the news source
            description: The short bio of the news source
            category: The news category the news source works on
            country: The country the news source are based out of
        """
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.country = country
        self.link = link

class Article:
    """
    This will define everything about a news article
    """
    def __init__(self,source,author,title,description,link,image_url,published):
        """
        This will define all the properties in the article class
        
        Args:
            source: This is the name of the news source
            author: This is the individual who wrote the news article
            title: This is the heading of the news article
            description: This is the brief summary of the article
            link: This is the direct link to the source of the news
            image_url: This is the link to the image attached to the article
            published: This is the date of publication
        """
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.link = link
        self.image_url = image_url
        self.published = published

    article_findings = []

    def save_article(self):
        """
        This function will add an article to the article_findings array
        """
        self.article_findings.append(self)