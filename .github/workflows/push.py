import requests
import os

# 读取配置
QMSG_KEY = os.getenv("QMSG_KEY")
CITY_CODE = "101240105"  # 进贤

# 1. 获取天气（和风天气免费API）
weather_url = f"https://devapi.qweather.com/v7/weather/3d?location={CITY_CODE}&key=HE10000000000000000000000000"
weather_res = requests.get(weather_url).json()
today = weather_res["daily"][0]
weather_text = f"🌤️ 今日天气（进贤）\n温度：{today['tempMin']}℃ ~ {today['tempMax']}℃\n天气：{today['textDay']}\n风力：{today['windDirDay']} {today['windScale']}级"

# 2. 获取早报（免费API）
news_url = "https://60s.viki.moe/?v2"
news_res = requests.get(news).json()
news_text = "📰 今日资讯\n" + "\n".join([f"• {item}" for item in news_res["news"][:5]])

# 3. 合并内容
content = f"☀️ 每日天气资讯\n\n{weather_text}\n\n{news_text}"

# 4. Qmsg 免费推送（无需实名）
push_url = f"https://qmsg.zendee.cn/send?msg={content}&key={QMSG}"
requests.get(push)
