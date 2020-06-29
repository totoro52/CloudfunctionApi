#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json

def get_Config():
    config = {
        'apiUri': 'http://API地址',
        'funUrl': '/云函数模块名/'
    }

    return config


def main_handler(event, context):
    config = get_Config()
    # 封装用户发来的请求
    requestPath = config['apiUri'] + event['path'].replace(config['funUrl'], '/')
    requestBody = ''
    headers = {}
    # 查看是否为令牌请求
    if 'token' in event['headers'].keys():
        headers['token'] = event['headers']['token']
    # 判断请求头
    if 'content-type' in event['headers'].keys():
        headers['Content-type'] = event['headers']['content-type']
    if 'body' in event.keys():
        requestBody = event['body']
    response = requests.request(method=event['httpMethod'],url=requestPath,headers=headers,data=requestBody)
    return json.loads(response.text)
