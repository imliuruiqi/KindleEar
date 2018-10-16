#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Technews

class Technews(BaseFeedBook):
    title                 = u'科技新闻'
    description           = u'科技新闻精选,少数派，好奇心日报,36kr,果壳...'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = DEFAULT_MASTHEAD
    coverfile             = DEFAULT_COVER
    keep_image            = False
    network_timeout       = 60
    oldest_article        = 1
    max_articles_per_feed = 5
    oldest_article        = 1
    
    feeds = [
            (u'少数派', 'http://sspai.com/feed'),
            (u'好奇心日报', 'http://www.qdaily.com/feed'),
            ('36kr', 'http://www.36kr.com/feed?1.0'),
            (u'小道消息', 'http://hutu.me/feed'),
            (u'极客公园', 'http://www.geekpark.net/rss'),
            (u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
            (u'科学松鼠会', 'http://songshuhui.net/feed'),
            (u'果壳','http://feeds.brandipo.com/users/1/web_requests/21/guoke.xml'),
            (u'月光博客','http://feed.williamlong.info/'),
            (u'DeepTech深科技','http://feedmaker.kindle4rss.com/feeds/mit-tr.weixin.xml'),
            (u'InfoQ中文','http://feedmaker.kindle4rss.com/feeds/cn.infoq.xml'),
            (u'Engadget中文版','http://feedmaker.kindle4rss.com/feeds/cn.engadget.com.xml'),
            (u'环球科学', 'http://blog.sina.com.cn/rss/sciam.xml'),
            ]

