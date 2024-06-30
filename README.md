
# AliveBot

AliveBot позволяет сохранять сессии Telegram активными, даже если не взаимодействовать с ними. Это полезно, так как Telegram удаляет аккаунты после года неактивности.

## Оглавление

- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)
- [Конфигурация](#конфигурация)
- [Зависимости](#зависимости)
- [Лицензия](#лицензия)

## Описание

AliveBot - это скрипт, который поддерживает активность сессий Telegram. Основной скрипт `main.py` запускается на сервере, чтобы сессии оставались активными. Скрипт `login.py` используется для авторизации на новых устройствах в случае утери всех сессий, кроме тех, что находятся на сервере.

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/yourusername/alivebot.git
    cd alivebot
    ```

2. Установите необходимые зависимости:

    ```bash
    pip install telethon
    ```

## Использование

### Запуск основного скрипта

Запустите `main.py` для поддержания активности сессий:

```bash
python main.py
```

Скрипт `main.py` выполняет следующие задачи:
1. Загружает конфигурацию из файла `constants.py`.
2. Авторизует и сохраняет сессии для каждого номера телефона.
3. Периодически отправляет сообщения и обновляет статус в Telegram, чтобы поддерживать сессии активными.

### Авторизация

Скрипт `login.py` используется для авторизации на новых устройствах в случае, если все сессии утеряны, кроме тех, что находятся на сервере.

Для этого измените переменную `session_file` в `login.py` на нужный вам файл сессии:

```python
session_file = "your_session_file.session"
```

Запустите скрипт:

```bash
python login.py
```

Этот скрипт будет отображать все сообщения, которые приходят на аккаунт пользователя в реальном времени. Запустите скрипт и начните процесс авторизации на новом устройстве. Код для авторизации придет в личные сообщения, и вы сможете увидеть его в консоли.

## Конфигурация

В файле `constants.py` укажите необходимые переменные для работы скриптов, такие как:

- `apiid` и `apihash` для подключения к API Telegram
- `phonenumbers` - список номеров телефонов для сессий
- `channelid` - ID канала Telegram
- `sessionfiles` - пути к файлам сессий
- `pingtime` - время задержки перед каждым сообщением

Пример `constants.py`:

```python
apiid = 123456789  # Замените на ваш API ID
apihash = "abcdef12345"  # Замените на ваш API Hash
phonenumbers = ["+123456", "+7890"]  # Замените на ваши номера телефонов
channelid = -1234567890  # Замените на ID вашего канала
sessionfiles = ["user1.session", "user2.session"]  # Замените на пути к вашим файлам сессий
pingtime = 3600 # Время задержки перед каждым сообщением
```

## Зависимости

Проект использует следующую библиотеку:
- [Telethon](https://pypi.org/project/Telethon/)

Для установки зависимости используйте следующую команду:

```bash
pip install telethon
```

## Лицензия

Этот проект лицензируется под GNU Affero General Public License v3.0. Подробности смотрите в файле [LICENSE](LICENSE).