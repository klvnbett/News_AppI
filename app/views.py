from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
        '''

    popular_news = get_news('popular')
    now_showing_news = get_news('now_playing')
    print(popular_news)
    title = 'Welcome to the News website'
    return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)