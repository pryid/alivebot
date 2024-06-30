import os
import asyncio
from telethon import TelegramClient, events
from constants import apiid, apihash

api_id = apiid  # Замените на ваш API ID
api_hash = apihash  # Замените на ваш API Hash
session_file = "user1.session"  # Замените на путь к вашему файлу сессии

# Проверьте, существует ли файл сессии
if not os.path.exists(session_file):
    print("Файл сессии не найден. Программа завершена.")
    exit()

async def main():
    client = TelegramClient(session_file, api_id, api_hash)
    
    await client.connect()
    
    if not await client.is_user_authorized():
        print("Файл сессии не авторизован. Программа завершена.")
        await client.disconnect()
        return
    
    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:
            print(f"Новое сообщение от {event.sender_id}: {event.message.message}")
    
    print("Клиент подключен и готов ловить сообщения.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
