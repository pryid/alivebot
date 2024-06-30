import os
import asyncio
import random
from constants import apiid, apihash, phonenumbers, channelid, sessionfiles, pingtime
from datetime import datetime
from telethon import TelegramClient, errors, functions

async def send_alive_message(client, channel_id):
    while True:
        # Случайная задержка перед появлением в сети
        initial_online_delay = random.randint(3, 7)
        await asyncio.sleep(initial_online_delay)
        
        # Эмуляция появления в сети
        await client(functions.account.UpdateStatusRequest(offline=False))
        
        # Случайная задержка перед началом печати
        typing_delay = random.randint(3, 7)
        await asyncio.sleep(typing_delay)
        
        # Эмуляция статуса "печати"
        async with client.action(channel_id, 'typing'):
            typing_duration = random.randint(17, 50)
            await asyncio.sleep(typing_duration)
        
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        message = f"Alive: {current_time}"
        await client.send_message(channel_id, message)
        
        # Установка статуса оффлайн после отправки сообщения
        await client(functions.account.UpdateStatusRequest(offline=True))
        
        # Случайная задержка перед следующим сообщением
        random_delay = random.randint(5, 17)
        await asyncio.sleep(pingtime + random_delay)

async def authorize_and_save_session(client, phone_number):
    await client.send_code_request(phone_number)
    code = input(f"Введите код для номера {phone_number}: ")
    try:
        await client.sign_in(phone_number, code)
    except errors.SessionPasswordNeededError:
        password = input(f"Введите пароль двухфакторной аутентификации для номера {phone_number}: ")
        await client.sign_in(password=password)

async def manage_session(api_id, api_hash, session_file, phone_number, channel_id):
    client = TelegramClient(session_file, api_id, api_hash)
    await client.connect()
    
    if not await client.is_user_authorized():
        print(f"Файл сессии {session_file} не найден или не авторизован. Проводится авторизация...")
        await authorize_and_save_session(client, phone_number)
    else:
        print(f"Файл сессии {session_file} найден. Используется существующая сессия.")
    
    # Случайная задержка перед началом работы сессии
    initial_delay = random.randint(5, 17)
    await asyncio.sleep(initial_delay)
    
    await send_alive_message(client, channel_id)

async def main():
    tasks = [manage_session(apiid, apihash, session_file, phone_number, channelid)
             for session_file, phone_number in zip(sessionfiles, phonenumbers)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
