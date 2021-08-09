from flask import render_template
from app import app
from .request import get_news, get_newsBreak,get_sources

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    sources=get_sources()
    title = 'Welcome to the News website'
    return render_template('index.html', title = title,  sources = sources)

@app.route('/articles/<string:source_id>')
def source(source_id):
    articles = get_news(source_id)
    return render_template('news.html', articles = articles)
    

    
@app.route('/news/<int:id>')
def movie(id):

    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)

@app.route('/search/<newsBreak_name>')
def search(newsBreak_name):
    '''
    View function to display the search results
    '''
    newsBreak_name_list = newsBreak_name.split(" ")
    newsBreak_name_format = "+".join(newsBreak_name_list)
    searched_news = search_news(newsBreak_name_format)
    title = f'search results for {newsBreak_name}'
    return render_template('search.html',news = searched_news)