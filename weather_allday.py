'''
Author: Ziheng
Date: 2021-08-28 09:50:13
LastEditTime: 2021-08-28 09:58:05
'''
import json, requests
from setting import GD_API_TOKEN

pushMess = "天气预警！实时天气：{} 接口更新时间：{}"
cityID = '340104'
# 340101 合肥市市区
# https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1 高德天气api文档
def index():
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={cityID}&key={GD_API_TOKEN}&extensions=base"
    weather = json.loads(requests.get(url).text)['lives'][0]
    if "雨" in weather['weather']or "雪" in weather['weather'] or "暴" in weather['weather']:
        pushMess_will = pushMess.format(weather.get("weather",None),weather.get('reporttime',None))
        # 消息推送
        requests.get(
            f"https://service-e5pbfglh-1259049233.sh.apigw.tencentcs.com/release/none_woo?text={pushMess_will}"
        )

if __name__ == "__main__":
    index()