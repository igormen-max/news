import requests

# Ваши данные со скриншота 05d251c6-d660-47a4-982b-05144f126584
TOKEN = "7888738077:AAHcgy42M_r_EIssK3Ljj8HlL_jnLTBoO8k"
CHAT_ID = "7904774473"

def send_news():
    message = "🚀 Игорь, проверка связи! Бот официально запущен из GitHub."
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Успех! Сообщение отправлено.")
        else:
            print(f"Ошибка Telegram: {response.text}")
    except Exception as e:
        print(f"Ошибка скрипта: {e}")

if __name__ == "__main__":
    send_news()
