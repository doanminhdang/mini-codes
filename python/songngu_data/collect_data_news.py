# Use newspaper3k to collect data from website

from newspaper import Article
url='https://www.washingtonpost.com/graphics/2018/world/how-a-trump-decision-on-trade-became-a-setback-for-democracy-in-vietnam'
article = Article(url)
article.download()
article.parse()
print(article.authors)
with open('test_newspaper3k.txt','wt') as filename:
    filename.write(article.text)

#article.nlp()
