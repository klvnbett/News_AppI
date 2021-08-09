from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']
sources_url=app.config["SOURCES_API_BASE_URL"]
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(source):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            newsBreak_results_list = get_news_response['articles']
            news_results = process_results(newsBreak_results_list)
        return news_results

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        return get_news_response['sources']#use sources key to pick sources list from the dictionary
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    
    '''
    newsBreak_results = []
    for news_item in news_list:
        id = news_item.get('source').get('id')
        title = news_item.get('title')
        author=news_item.get('author')
        description = news_item.get('description')
        image = news_item.get('urlToImage')
        url = news_item.get('url')

        if image:
            newsBreak_object = News(id=id,title=title,description=description,image=image,url=url)
            newsBreak_results.append(newsBreak_object)


     

    return newsBreak_results

def get_newsBreak(id):
    get_newsBreak_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_newsBreak_details_url) as url:
        newsBreak_details_data = url.read()
        newsBreak_details_response = json.loads(newsBreak_details_data)

        newsBreak_object = None
        if newsBreak_details_response:
            id = newsBreak_details_response.get('id')
            title = newsBreak_details_response.get('title')
            author=newsBreak_details_response.get('author')
            description = newsBreak_details_response.get('description')

            newsBreak_object = News(id,title,author,description)

    return newsBreak_object

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results