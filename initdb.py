#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from mysite.wsgi import *
from blog.models import Author, Article, Tag

author_name_list = ['Mike', 'Tom', 'Zack', 'Zero', 'Lina']
article_title_list = ['Django Session', 'Python Session', 'HTML Session']


def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % (random.randrange(1, 3))
        author.email = '%s@test.com' % (author.addr)
        author.save()


def create_articles_and_tags():
    for article_title in article_title_list:
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)

        random_author = random.choice(Author.objects.all())

        for i in range(1, 21):
            title = '%s_%s' % (article_title, i)
            article, created = Article.objects.get_or_create(
                title=title, defaults={
                    'author': random_author,
                    'content': '%s content ' % title,
                    'score': random.randrange(70, 101),
                }
            )
            article.tags.add(tag)


def main():
    create_authors()
    create_articles_and_tags()


if __name__ == '__main__':
    main()
    print 'initial DB DONE!'
