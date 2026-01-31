import pyautogui
import time

print("БОТ ДЛЯ DINO GAME")
print("=" * 40)
print("Инструкция:")
print("1. Откройте Chrome -> chrome://dino")
print("2. Разверните игру на весь экран")
print("3. У вас будет 5 секунд переключиться на игру")
print("=" * 40)

time.sleep(5)

pyautogui.press('space')
time.sleep(1)

pyautogui.keyDown('down')

try:
    jump_times = []
    jump_count = 0
    last_jump_time = time.time()

    while True:
        current_time = time.time()

        if jump_count == 0:
            wait_time = 2.0
        elif jump_count < 10:
            wait_time = 3.0 + (jump_count * 0.2)
        else:
            avg_time = sum(jump_times[-10:]) / min(10, len(jump_times))
            wait_time = avg_time * 0.90

        if current_time - last_jump_time >= wait_time:
            pyautogui.keyUp('down')
            time.sleep(0.02)
            pyautogui.press('space')
            time.sleep(0.02)
            pyautogui.keyDown('down')

            jump_count += 1
            if jump_count > 1:
                actual_wait = current_time - last_jump_time
                jump_times.append(actual_wait)

                if jump_count < 10:
                    print(f"Прыжок {jump_count}: ожидалось {wait_time:.2f}, фактически {actual_wait:.2f} сек")
                elif jump_count == 10:
                    avg = sum(jump_times) / len(jump_times)
                    print(f"Настроено! Среднее время: {avg:.2f} сек")
                elif jump_count % 5 == 0 and jump_count > 10:
                    avg = sum(jump_times[-10:]) / 10
                    print(f"Прыжок {jump_count}: среднее {avg:.2f} сек")

            last_jump_time = current_time

        time.sleep(0.01)

except KeyboardInterrupt:
    pyautogui.keyUp('down')
    if jump_times:
        avg = sum(jump_times) / len(jump_times)
        print(f"Остановлено. Прыжков: {jump_count}, среднее время: {avg:.2f} сек")