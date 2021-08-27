'''
Author: Ziheng
Date: 2021-08-27 17:13:27
LastEditTime: 2021-08-27 17:13:30
'''
# -*- coding: utf8 -*-
import json
import os
import requests


def main_handler(event, context):
    # 读取 环境变量
    WECOM_CID = os.environ.get("WECOM_CID")
    WECOM_SECRET = os.environ.get("WECOM_SECRET")
    weComAId = os.environ.get("weComAId")
    # 获取 请求参数
    # test:text :: 发送文字
    test = event.get("queryString").get("text", None)
    if not test:
        data_body = json.dumps({"sug": "error", "data": "The message in None!please check!","event":event})
        data = {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": data_body
        }
        return data
    # WECOM_TOUID:for :: 发送给谁 默认全部人
    WECOM_TOUID = event.get("for", "@all")
    return_data = send_to_wecom(text=test, wecom_cid=WECOM_CID, wecom_aid=weComAId,
                                wecom_secret=WECOM_SECRET, wecom_touid=WECOM_TOUID)
    data_body = json.dumps({"sug": "sucess", "data": return_data})
    data = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": data_body
    }
    return data

# -- 以下代码来自方糖 --
def send_to_wecom(text, wecom_cid, wecom_aid, wecom_secret, wecom_touid='@all'):
    get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={wecom_cid}&corpsecret={wecom_secret}"
    response = requests.get(get_token_url).content
    access_token = json.loads(response).get('access_token')
    if access_token and len(access_token) > 0:
        send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
        data = {
            "touser": wecom_touid,
            "agentid": wecom_aid,
            "msgtype": "text",
            "text": {
                "content": text
            },
            "duplicate_check_interval": 600
        }
        # response = requests.post(send_msg_url, data=json.dumps(data)).context
        # return response
        response = requests.post(send_msg_url, data=json.dumps(data,ensure_ascii=False).encode("utf8"))
        return response.text
    else:
        return False
