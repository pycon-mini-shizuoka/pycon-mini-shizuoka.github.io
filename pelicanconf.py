#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'pycon-mini-shizuoka main'
SITENAME = 'PyCon mini Shizuoka'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# THEME = "./pycon-mini-shizu-pelican-theme"

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# index.rst raw load html. exclude dir 
# ARTICLE_EXCLUDES = ["rst_htmls"]

# save_as

ARTICLE_URL = '{category}/{author}/'
ARTICLE_SAVE_AS = '{category}/{author}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# github pages add CNAME

STATIC_PATHS = ['extra/front_img']
EXTRA_PATH_METADATA = {'extra/front_img': {'path': './front_img/'},
}

