class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError("Cannot modify the title attribute")
        
class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles))

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        return [author for author, count in author_counts.items() if count > 2]

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass