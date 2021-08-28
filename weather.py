'''
Author: Ziheng
Date: 2021-08-27 11:57:44
LastEditTime: 2021-08-28 11:31:28
'''
# -*- coding: utf8 -*-
import requests, json,datetime

pushMess = "早上好！今天是：{} 星期{}。\n\n{}\n\n未来10小时天气:\n{}\n今日一言：{} \nBy{}-{}"
week_dict = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "日"}
# 340101 合肥市市区
# https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1 高德天气api文档
YIYAN = 'https://v1.hitokoto.cn/'


def index():
    #GD_API_TOKEN : 高德开放平台 - web服务 - token
    url = f"https://wis.qq.com/weather/common?source=pc&weather_type=observe|forecast_1h|forecast_24h|index|alarm|limit|tips|rise&province=%E5%AE%89%E5%BE%BD%E7%9C%81&city=%E5%90%88%E8%82%A5%E5%B8%82"
    req = json.loads(requests.get(url).text)
    weahter = req['data']['forecast_1h']
    xx = 0
    all_data = []
    for xx in range(10):
        item = {}
        line = weahter[str(xx)]
        date = line['update_time']
        date_year = date[:4]
        date_month = date[4:6]
        date_day = date[6:8]
        date_hour = date[8:10]
        date_min = "00"
        item["date"] = f"{date_year}-{date_month}-{date_day} {date_hour}:{date_min}"
        item['weather'] = line['weather']
        all_data.append(item)
    #今天日期
    date_push = f"{date_year}-{date_month}-{date_day}"
    # 星期x
    dayOfWeek =week_dict[str(datetime.datetime.now().isoweekday())]
    # 天气消息提示
    is_unbrala = req['data']['tips']['forecast_24h']["0"]
    # 未来天气详细
    all_www = ''
    for line in all_data:
        all_www += f"{line['date']} - {line['weather']}\n"

    yiyan_data = json.loads(requests.get(url=YIYAN).text)
    pushMess_push_will = pushMess.format(date_push,dayOfWeek,is_unbrala,all_www,
                                         yiyan_data.get("hitokoto", None),
                                         yiyan_data.get("from_who", None),
                                         yiyan_data.get("from", None))

    # 消息推送
    requests.get(
        f"https://service-e5pbfglh-1259049233.sh.apigw.tencentcs.com/release/none_woo?text={pushMess_push_will}"
    )

if __name__ == "__main__":
    index()