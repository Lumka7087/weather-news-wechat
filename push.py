import requests
import os

# 读取配置
SENDKEY = os.getenv("SENDKEY")

# 进贤 101240105
city_code = "101240105"

# 1. 获取天气（改用稳定免费接口）
def get_weather(city):
    url = f"http://wthrcdn.etouch.cn/weather_mini?citykey={city}"
    res = requests.get(url, timeout=10).json()
    data = res.get("data", {})
    today = data.get("forecast", [])[0]
    w_text = (
        f"🌤️ 进贤今日天气\n"
        f"日期：{today.get('date')}\n"
        f"温度：{today.get('low')} ~ {today.get('high')}\n"
        f"天气：{today.get('type')}\n"
        f"风向风力：{today.get('fengxiang')} {today.get('fengli')}"
    )
    return w_text

# 2. 获取60秒资讯
def get_news():
    news_res = requests.get("https://60s.viki.moe/?v2", timeout=10).json()
    news_list = news_res.get("news", [])[:5]
    txt = "📰 今日热点资讯\n"
    for item in news_list:
        txt += f"• {item}\n"
    return txt

# 合并推送
if __name__ == "__main__":
    try:
        weather_info = get_weather(city_code)
        news_info = get_news()
        all_content = f"{weather_info}\n\n{news_info}"
        push_api = f"https://sctapi.ftqq.com/{SENDKEY}.send?title=☀️每日天气资讯&desp={all_content}"
        requests.post(push_api)
        print("推送完成")
    except Exception as e:
        print("出错：",e)
