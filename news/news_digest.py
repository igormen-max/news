
import requests
import xml.etree.ElementTree as ET

# Данные со скриншотов 05d251c6-d660-47a4-982b-05144f126584 и 1ec134ca-4821-4d81-ac58-73b74d0c23cc
TOKEN = "7888738077:AAHcgy42M_r_EIssK3Ljj8HlL_jnLTBoO8k"
CHAT_ID = "7904774473"

def get_ai_news():
    # Ленты новостей: ИИ на Хабре и Технологии
    urls = [
        "https://habr.com/ru/rss/hub/artificial_intelligence/all/?fl=ru",
        "https://habr.com/ru/rss/hub/robot/all/?fl=ru"
    ]
    news = []
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            root = ET.fromstring(res.content)
            for item in root.findall('.//item')[:15]: # Собираем по 15 с каждой ленты
                title = item.find('title').text
                link = item.find('link').text
                news.append(f"🤖 {title}\n🔗 {link}")
        except:
            continue
    return news[:30]

def send_digest():
    titles = get_ai_news()
    if not titles:
        text = "Сегодня новостей об ИИ не найдено. Проверьте источники."
    else:
        text = "🗞 **Ваш дайджест: ИИ и Агенты**\n\n" + "\n\n".join(titles)

    # Отправка в Telegram
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # Разбиваем сообщение, если оно слишком длинное для Telegram
    for i in range(0, len(text), 4000):
        requests.post(url, json={"chat_id": CHAT_ID, "text": text[i:i+4000], "parse_mode": "Markdown"})

if __name__ == "__main__":
    send_digest()
