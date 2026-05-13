import requests
import os

# Ваши данные (токен и ID чата уже должны быть в секретах GitHub, если мы их настраивали)
# Если нет — временно вставьте их сюда в кавычках для проверки
TOKEN = "ВАШ_ТОКЕН_БОТА"
CHAT_ID = "ВАШ_ID_ЧАТА"

def send_test_message():
    message = "🚀 Ура! Связь с GitHub установлена. Ваш новостной дайджест готов к работе!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Сообщение успешно отправлено в Telegram!")
    else:
        print(f"Ошибка отправки: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_test_message()
