class Source:
    """
    This will define everything to do with sources
    """
    def __init__(self,id,name,description,category,country):
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