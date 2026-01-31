import tkinter as tk
import time
import threading


def close_window():
    # Функция для блокировки закрытия окна
    pass


def simulate_virus():
    tasks = [
        "Поиск системных файлов...",
        "Удаление изображений...",
        "Удаление документов...",
        "Настройка удаленного доступа...",
        "Шифрование данных...",
        "Очистка следов..."
    ]

    for i, task in enumerate(tasks):
        percentage = (i + 1) * (100 // len(tasks))
        text_widget.insert(tk.END, f"[{percentage}%] {task}\n")
        text_widget.see(tk.END)
        time.sleep(1)  # задержка между задачами
        root.update()

    text_widget.insert(tk.END, "\nВирус успешно активирован. Система скомпрометирована.\n")


def start_simulation():
    thread = threading.Thread(target=simulate_virus)
    thread.start()


# Создание окна
root = tk.Tk()
root.title("Системная диагностика")
root.geometry("600x400")
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", close_window)  # Блокировка закрытия

# Текстовое поле для вывода
text_widget = tk.Text(root, bg="black", fg="green", font=("Courier", 12))
text_widget.pack(expand=True, fill="both")

# Кнопка запуска (опционально, можно автоматически)
start_button = tk.Button(root, text="Начать диагностику", command=start_simulation, bg="gray", fg="white")
start_button.pack(pady=10)

# Автозапуск симуляции
root.after(1000, start_simulation)

root.mainloop()