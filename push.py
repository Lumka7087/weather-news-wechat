import requests
import os

# 配置
SENDKEY = os.getenv("SENDKEY")
CITY_CODE = "101240105"  # 进贤

# 获取天气
weather_url = f"https://devapi.qweather.com/v7/weather/3d?location={CITY_CODE}&key=HE10000000000000000000000000"
weather = requests.get(weather_url).json()["daily"][0]
weather_text = f"🌤️ 进贤今日天气\n{weather['tempMin']}℃ ~ {weather['tempMax']}℃\n{weather['textDay']}"

# 获取资讯
news_data = requests.get("https://60s.viki.moe/?v2").json()
news_list = news_data["news"][:5]
news_text = "📰 今日资讯\n" + "\n".join(f"• {item}" for item in news_list)

# 推送微信
content = f"{weather_text}\n\n{news_text}"
push_url = f"https://sctapi.ftqq.com/{SENDKEY}.send?title=☀️每日天气资讯&desp={content}"
requests.post(push_url)

print("✅ 推送成功！")
