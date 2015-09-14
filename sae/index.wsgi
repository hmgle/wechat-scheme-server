# coding: UTF-8

import os
import sae
import web

from weixin import WeixinInterface

urls = (
    '/', 'Hello',
    '/weixin', 'WeixinInterface'
)


class Hello:
    def GET(self):
        return "it work!"

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
