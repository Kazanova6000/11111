import speech_recognition as sr
from datetime import datetime


def listen():
    """Слушает микрофон и возвращает текст"""
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Говори...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

            text = r.recognize_google(audio, language='ru-RU')
            print(f"Вы: {text}")
            return text.lower()

    except sr.UnknownValueError:
        print("Не расслышала, повтори")
        return None
    except sr.RequestError:
        print("Проблемы с интернетом")
        return None
    except Exception:
        print("Ошибка микрофона")
        return None


# Список всех доступных команд
COMMANDS = {
    "привет": "Поприветствовать ассистента",
    "время": "Узнать текущее время",
    "дата": "Узнать сегодняшнюю дату",
    "погода": "Узнать погоду",
    "хелп ми": "Показать список всех команд",
    "help me": "Показать список всех команд",
    "стоп": "Завершить работу ассистента",
    "выход": "Завершить работу ассистента"
}


def show_help():
    """Выводит список всех доступных команд"""
    print("\n" + "=" * 50)
    print("СПИСОК ДОСТУПНЫХ КОМАНД:")
    print("=" * 50)

    for command, description in COMMANDS.items():
        print(f"• '{command}' - {description}")

    print("=" * 50 + "\n")


# Основная программа
print("=" * 40)
print("ГОЛОСОВОЙ АССИСТЕНТ")
print("=" * 40)
print("Для списка команд скажите 'help me' или 'хелп ми'")

while True:
    command = listen()

    if command:
        if "привет" in command:
            print("Ассистент: Привет! Как дела?")

        elif "время" in command:
            current_time = datetime.now().strftime("%H:%M")
            print(f"Ассистент: Сейчас {current_time}")

        elif "дата" in command or "число" in command:
            current_date = datetime.now().strftime("%d.%m.%Y")
            print(f"Ассистент: Сегодня {current_date}")

        elif "погода" in command:
            print("Ассистент: На улице -34°C, ясно")

        elif "хелп ми" in command or "help me" in command or "помощь" in command:
            print("Ассистент: Вот список всех доступных команд:")
            show_help()

        elif "стоп" in command or "выход" in command:
            print("Ассистент: До свидания! Рад был помочь.")
            break

        else:
            print(f"Ассистент: Не поняла команду '{command}'")
            print("Ассистент: Скажите 'help me' для списка команд")

input("\nНажми Enter для выхода...")