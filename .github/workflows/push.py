import requests
import os

# 读取配置
PUSHPLUS_TOKEN = os.getenv("PUSHPLUS_TOKEN")
CITY_CODE = os.getenv("CITY_CODE")

# 1. 获取天气（和风天气免费API）
weather_url = f"https://devapi.qweather.com/v7/weather/3d?location={CITY_CODE}&key=HE1000000000000000000000000000"
weather_res = requests.get(weather_url).json()
today = weather_res["daily"][0]
weather_text = f"🌤️ 今日天气\n温度：{today['tempMin']}℃ ~ {today['tempMax']}℃\n天气：{today['textDay']}\n风力：{today['windDirDay']} {today['windScale']}级"

# 2. 获取早报（免费API）
news_url = "https://60s.viki.moe/?v2"
news_res = requests.get(news).json()
news_text = "📰 今日资讯\n" + "\n".join([f"• {item}" for item in news_res["news"][:5]])

# 3. 合并内容
content = f"☀️ 每日天气资讯\n\n{weather_text}\n\n{news_text}"

# 4. 推送到微信（PushPlus）
push_url = f"http://www.pushplus.plus/send?token={PUSHPLUS_TOKEN}&title=每日推送&content={content}&template=txt"
requests.get(push_url)
