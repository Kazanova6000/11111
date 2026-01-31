import time
class Library:  # класс где хранятся архивы
    def init(self):  # конструктор
        self.archives = []  # список архивов

    def add_archive(self, name):  # добавить архив
        self.archives.append(name)  # просто добавляем в список
        print(f"Добавил архив: {name}")
        
    def get_archives(self):  # получить все архивы
        return self.archives  # возвращаем список

    def delete_archive(self, index):  # удалить по номеру
        if index < len(self.archives):  # проверяем есть ли такой
            deleted = self.archives.pop(index)  # удаляем
            print(f"Удалил архив: {deleted}")
        else:
            print("Такого номера нет!")

    def hack_archive(self, index):  # взломать архив
        if index < len(self.archives):  # проверяем
            archive = self.archives[index]  # берем архив
            print(f"Взламываю {archive}...")
            for i in range(5):  # цикл для красоты
                print(f"Прогресс: {(i + 1) * 20}%")
                time.sleep(0.5)  # ждем полсекунды
            print(f"Архив {archive} взломан!")
        else:
            print("Неверный номер архива!")


class Menu:  # класс менюшки
    def init(self, library):  # конструктор
        self.lib = library  # библиотека для работы

    def start(self):  # главная функция
        while True:  # бесконечный цикл
            print("\n" + "=" * 20)
            print("---BruteForce---")  # название
            print("1. Add archive")
            print("2. Show archives")
            print("3. Delete archive")
            print("4. Hack archive")
            print("5. Exit")
            print("=" * 20)

            choice = input("Выбери цифру: ")  # выбор пользователя

            if choice == "1":
                name = input("Название архива: ")
                self.lib.add_archive(name)

            elif choice == "2":
                print("\nВсе архивы:")
                for i, arch in enumerate(self.lib.get_archives()):
                    print(f"{i + 1}. {arch}")

            elif choice == "3":
                if self.lib.get_archives():
                    for i, arch in enumerate(self.lib.get_archives()):
                        print(f"{i + 1}. {arch}")
                    try:
                        num = int(input("Номер для удаления: ")) - 1
                        self.lib.delete_archive(num)
                    except:
                        print("Цифру надо!")
                else:
                    print("Нет архивов!")

            elif choice == "4":
                if self.lib.get_archives():
                    for i, arch in enumerate(self.lib.get_archives()):
                        print(f"{i + 1}. {arch}")
                    try:
                        num = int(input("Номер для взлома: ")) - 1
                        self.lib.hack_archive(num)
                    except:
                        print("Цифру вводи!")
                else:
                    print("Нет архивов!")

            elif choice == "5":
                print("Пока!")
                break  # выходим из цикла

            else:
                print("От 1 до 5 надо!")
                if name == "main":
                    print("Запускаю взломщик...")
                    time.sleep(1)

                    my_lib = Library()
                    my_lib.add_archive("паспорт.rar")
                    my_lib.add_archive("фото.zip")
                    my_lib.add_archive("игры.7z")

                    my_menu = Menu(my_lib)
                    my_menu.start()