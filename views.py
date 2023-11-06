from django.shortcuts import render
#importar el array de articles.py
from . import articles

def home(request):
    return render(request, 'index.html')

def art(request, id):
    # Get the recent articles list
    new_articles = articles.recent_articles  
    # Create an empty list to store the articles to show
    articles_to_show = []  
    # Iterate over each article in the recent articles list
    for article in new_articles:  
        # Check if the article's id is not equal to the given id
        if article['id_article'] != id:  
            # Add the article to the articles to show list
            articles_to_show.append(article)  
            # Print the title of the article 
    # Check if the number of articles to show is greater than or equal to 4
    if len(articles_to_show) == 4:  
        # Remove the last article from the articles to show list
        articles_to_show.pop()  
    
    print(len(articles_to_show)) 
    # Render the template for the given id
    return render(request, 'articles/' + str(id) + '.html', {
        "articles": articles_to_show,
    })  

# Create your views here.
