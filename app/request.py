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
            news1_results_list = get_news_response['articles']
            news_results = process_results(news1_results_list)
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
    news1_results = []
    for news_item in news_list:
        id = news_item.get('source').get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        image = news_item.get('urlToImage')
        url = news_item.get('url')

        if image:
            news1_object = News(id=id,title=title,description=description,image=image,url=url)
            news1_results.append(news1_object)


     

    return news1_results

def get_news1(id):
    get_news1_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news1_details_url) as url:
        news1_details_data = url.read()
        news1_details_response = json.loads(news1_details_data)

        news1_object = None
        if news1_details_response:
            id = news1_details_response.get('id')
            title = news1_details_response.get('title')
            description = news1_details_response.get('description')

            news1_object = News(id,title,description)

    return news1_object