#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rahul Gaur (@aregee)'
TAGLINE= u'Web | Linux | Open Source | G33K | Food | Booze'
SITENAME = u'rahulgaur.info'
SITEURL = 'http://myblog-rahulgaur.rhcloud.com'
#SITEURL = 'http://192.168.1.35:8080'
TIMEZONE = 'Asia/Kolkata'


DEFAULT_LANG = u'en'

THEME = '/Users/aregee/Workspace/pelican-themes/svbhack/'

USER_LOGO_URL = SITEURL  + '/images/image_1.jpeg'
STATIC_PATHS = ["images", "pdfs"]
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Resume', SITEURL + '/pdfs/rahulgaur.pdf'),)

# Social widget
#SOCIAL = (('GitHub', 'http://github.com/aregee'),
#          ('Twitter', 'http://twitter.com/iamaregee'),
#          ('email', 'mailto:rahul.nbg@gmail.com'),
#          ('Linkedin','http://www.linkedin.com/pub/rahul-gaur/20/b72/294'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
