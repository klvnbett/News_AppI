class News:
    '''
    news class to define news Objects
    '''

    def __init__(self,id,title,author,description,image,url):
        self.id =id
        self.title = title
        self.author=author
        self.description = description
        self.image=image        
        self.url=url