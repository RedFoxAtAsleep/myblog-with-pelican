#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'zhjh'
SITENAME = 'crimson'
SITEURL = 'https://redfoxatasleep.github.io/myblog-with-pelican'
# SITEURL = 'https://blog.redfoxatasleep.top'
THEME = 'theme/notmyidea'

PATH = 'content'
# PAGE_PATHS
# ARTICLE_PATHS
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Markdown Extension
# MD_EXTENSIONS = []

# Plugins
PLUGIN_PATHS = ['plugins',]
PLUGINS = ['neighbors', 'sitemap', 'pelican-toc']