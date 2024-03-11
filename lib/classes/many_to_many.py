class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
            if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
                self._title = new_title
            else:
                raise ValueError("Title must be of type str and between 5 and 50 characters")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
            if isinstance(author, Author):
                self._author = author
            else:
                raise ValueError("Author must be an instance of the Author class")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of the Magazine class")
        
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