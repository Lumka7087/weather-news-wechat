import requests
import os

SENDKEY = os.getenv("SENDKEY")

# 进贤坐标
LAT, LON = 28.37, 116.24

def get_weather():
    """使用 Open-Meteo 免费 API（无需 API Key）"""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&daily=temperature_2m_max,temperature_2m_min,weathercode"
        "&timezone=Asia%2FShanghai"
    )
    res = requests.get(url, timeout=10).json()
    daily = res["daily"]
    date = daily["time"][0]
    t_max = daily["temperature_2m_max"][0]
    t_min = daily["temperature_2m_min"][0]
    code = daily["weathercode"][0]

    weather_map = {
        0: "☀️ 晴", 1: "🌤 多云", 2: "⛅ 阴天", 3: "☁️ 阴",
        45: "🌫 雾", 48: "🌫 雾凇",
        51: "🌦 小雨", 53: "🌦 中雨", 55: "🌧 大雨",
        61: "🌧 小雨", 63: "🌧 中雨", 65: "🌧 大雨",
        71: "🌨 小雪", 73: "🌨 中雪", 75: "❄️ 大雪",
        80: "🌦 阵雨", 81: "🌧 中阵雨", 82: "🌧 大阵雨",
        95: "⛈ 雷暴", 96: "⛈ 雷暴+冰雹", 99: "⛈ 强雷暴+冰雹",
    }
    weather_desc = weather_map.get(code, f"🌡 {code}")

    return (
        f"🌤️ 进贤今日天气
"
        f"日期：{date}
"
        f"温度：{t_min}°C ~ {t_max}°C
"
        f"天气：{weather_desc}"
    )

def get_news():
    """获取 60 秒热点资讯"""
    news_res = requests.get("https://60s.viki.moe/?v2", timeout=10).json()
    news_list = news_res.get("news", [])[:5]
    txt = "📰 今日热点资讯
"
    for item in news_list:
        txt += f"• {item}
"
    return txt

if __name__ == "__main__":
    try:
        weather_info = get_weather()
        news_info = get_news()
        all_content = f"{weather_info}

{news_info}"

        push_url = f"https://sctapi.ftqq.com/{SENDKEY}.send"
        requests.post(push_url, data={
            "title": "☀️ 每日天气资讯",
            "desp": all_content,
        }, timeout=10)
        print("✅ 推送完成")
    except Exception as e:
        print(f"❌ 出错：{e}")
