import requests
import sys

# Ваши данные (проверьте каждую цифру!)
TOKEN = "7888738077:AAHcgy42M_r_EIssK3Ljj8HlL_jnLTBoO8k"
CHAT_ID = "7904774473"

def main():
    print("Начинаю работу...")
    message = "🤖 Тест дайджеста: Связь установлена!"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    print(f"Отправляю запрос в Telegram для ID: {CHAT_ID}")
    try:
        response = requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)
        print(f"Статус ответа: {response.status_code}")
        print(f"Ответ сервера: {response.text}")
        
        if response.status_code == 200:
            print("✅ СООБЩЕНИЕ УСПЕШНО ОТПРАВЛЕНО!")
        else:
            print("❌ ОШИБКА: Telegram отклонил запрос.")
    except Exception as e:
        print(f"💥 КРИТИЧЕСКАЯ ОШИБКА: {e}")

if __name__ == "__main__":
    main()
