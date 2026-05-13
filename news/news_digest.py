import requests
import xml.etree.ElementTree as ET

# Ваши данные (проверьте, что они совпадают с вашими)
TOKEN = "7888738077:AAHcgy42M_r_EIssK3Ljj8HlL_jnLTBoO8k"
CHAT_ID = "7904774473"

def get_news():
    # Источники новостей (RSS-ленты по ИИ и технологиям)
    feeds = [
        "https://habr.com/ru/rss/hub/artificial_intelligence/all/?fl=ru", # ИИ на Хабре
        "https://habr.com/ru/rss/hub/programming/all/?fl=ru",            # Инструменты и обучение
        "https://raw.githubusercontent.com/osint-bravery/news-feeds/main/ai_news.xml" # Агенты и ИИ
    ]
    
    news_list = []
    
    for url in feeds:
        try:
            response = requests.get(url, timeout=10)
            root = ET.fromstring(response.content)
            for item in root.findall('.//item')[:10]: # Берем по 10 из каждого источника
                title = item.find('title').text
                link = item.find('link').text
                news_list.append(f"🔹 {title}\n🔗 {link}")
        except:
            continue
            
    return news_list[:30] # Ограничиваем до 30 новостей

def send_to_telegram():
    all_news = get_news()
    
    if not all_news:
        text = "К сожалению, свежих новостей по теме ИИ сейчас не нашлось."
    else:
        header = "🤖 **Дайджест: ИИ, Агенты и Обучение**\n\n"
        # Разбиваем на части, так как в Telegram лимит на длину сообщения
        text = header + "\n\n".join(all_news)

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Если текста слишком много, Telegram его не примет, поэтому шлем частями
    for i in range(0, len(text), 4000):
        part = text[i:i+4000]
        requests.post(url, json={"chat_id": CHAT_ID, "text": part, "parse_mode": "Markdown"})

if __name__ == "__main__":
    send_to_telegram()
