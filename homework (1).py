import pyttsx3

engine = pyttsx3.init()


def speak(text):
    print(f"Ассистент: {text}")
    engine.say(text)
    engine.runAndWait()


def help_me():
    commands = [
        "Помощь - скажите 'help me'"
    ]

    speak("Вот все что я пока умею:")
    for i, cmd in enumerate(commands, 1):
        print(f"{i}. {cmd}")
        engine.say(cmd)
        engine.runAndWait()


print("напишите 'help me' (извините у меня не получается сделать так чтобы можно было скахать) ")

# Имитация голосового ввода
while True:
    user_said = input("Что вы сказали? ").lower()

    if "help me" in user_said or "помощь" in user_said:
        help_me()
    elif "выход" in user_said:
        speak("До свидания!")
        break
    else:
        speak("Скажите 'help me' для списка команд")