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
# Markdown扩展
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {  # 表格
        },
        'markdown.extensions.toc': {  # 目录，设置看https://python-markdown.github.io/extensions/toc/
            'title': 'TOC:',  # 目录题头
            'toc_depth': 8,
        },
    },
    'output_format': 'html5',
}

# Plugins
PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['neighbors', 'sitemap']

# Plugin sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'weekly'
    }
}

