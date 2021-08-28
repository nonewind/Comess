'''
Author: Ziheng
Date: 2021-08-27 11:57:44
LastEditTime: 2021-08-28 09:29:42
'''
# -*- coding: utf8 -*-
import requests, json
from setting import GD_API_TOKEN

cityID = '340104'

pushMess = "早上好！今天是：{} 星期{} 。今天的天气是：{}转{}。温度：{}-{}。今日一言：{} By{}-{}"
week_dict = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "日"}
# 340101 合肥市市区
# https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1 高德天气api文档
YIYAN = 'https://v1.hitokoto.cn/'


def index():
    #GD_API_TOKEN : 高德开放平台 - web服务 - token
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={cityID}&key={GD_API_TOKEN}&extensions=all"
    req = json.loads(requests.get(url).text)
    weahter = req['forecasts'][0]['casts'][0]
    yiyan_data = json.loads(requests.get(url=YIYAN).text)
    pushMess_push_will = pushMess.format(weahter.get("date",
                                                     None), week_dict[weahter.get("week", None)],
                                         weahter.get("dayweather", None),
                                         weahter.get("nightweather", None),
                                         weahter.get("nighttemp", None),
                                         weahter.get("daytemp", None),
                                         yiyan_data.get("hitokoto", None),
                                         yiyan_data.get("from_who", None),
                                         yiyan_data.get("from", None))

    # 消息推送
    requests.get(
        f"https://service-e5pbfglh-1259049233.sh.apigw.tencentcs.com/release/none_woo?text={pushMess_push_will}"
    )


index()