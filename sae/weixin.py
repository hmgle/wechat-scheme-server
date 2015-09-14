# coding: UTF-8

import hashlib
import web
import lxml
import time
import os
import socket
from lxml import etree

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.s.connect(('56.78.90.12', 2345))
        self.s.connect(('your server ip addr', 2345)) # 2345: server port

    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        # your token
        token = "xxxxxxxxxxxxxxxx"
        # 字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        # sha1 加密算法
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        # 如果是来自微信的请求，则回复 echostr
        if hashcode == signature:
            return echostr
        return 'access verification fail'

    def POST(self):
        # 获取 xml 构造 xml dom 树
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        # 提取信息
        content = xml.find("Content").text
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        self.s.send(content + "\n")
        reply = self.s.recv(1024)
        return self.render.reply_text(fromUser, toUser, int(time.time()),
                "scheme: "+ reply)
