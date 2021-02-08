#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'PyCon mini Shizuoka'
SITENAME = 'PyCon mini Shizuoka 公式ページ'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME = "pelican-clean-blog"

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

# STATIC_PATHS = ['extra/front_img']
# EXTRA_PATH_METADATA = {'extra/front_img': {'path': './front_img/'},
# }

SOCIAL = (('twitter', 'https://twitter.com/PyConShizu'),
          ('github', 'https://github.com/pycon-mini-shizuoka/'),
          ('connpass', 'https://pycon-shizu.connpass.com'),
)   
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# theme config
HEADER_COVER = 'images/header-bg-mini.jpg'
HEADER_COLOR = 'white'


