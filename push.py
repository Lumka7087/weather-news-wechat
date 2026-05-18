import requests
import os
import sys

def main():
    try:
        sendkey = os.environ.get("SENDKEY", "")
        if not sendkey:
            print("未配置SENDKEY")
            return

        city = "101240105"
        weather_url = f"https://devapi.qweather.com/v7/weather/now?location={city}&key=HEaa99999999999999999999999999999"

        weather = requests.get(weather_url, timeout=10).json()
        now = weather.get("now", {})
        weather_text = f"🌤️ 进贤实时天气\n温度：{now.get('temp','--')}℃\n天气：{now.get('text','--')}"

        news_url = "https://60s.viki.moe/?v2"
        news_data = requests.get(news_url, timeout=10).json()
        news = news_data.get("news", [])[:5]
        news_text = "📰 今日资讯\n" + "\n".join(f"• {n}" for n in news)

        content = f"{weather_text}\n\n{news_text}"
        push_url = f"https://sctapi.ftqq.com/{sendkey}.send?title=☀️每日推送&desp={content}"
        requests.post(push_url, timeout=10)

        print("✅ 推送成功！")
    except Exception as e:
        print(f"错误：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
