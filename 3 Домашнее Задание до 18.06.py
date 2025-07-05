# Номер 1
# b_players = {}
#
# def menu():
#     while True:
#         option = input(""""Выберите опцию:
#         1 - Добавить баскетболиста
#         2 - Удалить баскетболиста
#         3 - Найти баскетболиста
#         4 - Изменить данные о баскетболисте
#         5 - Выход
#         """)
#
#         match option:
#             case "1":
#                 name = input("Введите имя баскетболиста: ")
#                 height = int(input("Введите рост баскетболиста: "))
#                 b_players[name] = height
#             case "2":
#                 del_name = input("Введите имя баскетболиста, которого хотите удалить: ")
#                 del b_players[del_name]
#             case "3":
#                 f_name = input("Введите имя баскетболиста, которого хотите найти: ")
#                 print(f"{f_name}: рост {b_players[f_name]}см")
#             case "4":
#                 upd_name = input("Введите имя баскетболиста, чьи данные хотите изменить: ")
#                 new_height = int(input("Новый рост: "))
#                 b_players[upd_name] = new_height
#             case"5":
#                 break
#
#
# menu()

# Номер 2
# dictionary = {}
#
#
# def dict_menu():
#     while True:
#         option = input(""""Выберите опцию:
#         1 - Добавить новое слово
#         2 - Удалить существующее слово
#         3 - Найти слово
#         4 - Заменить слово
#         5 - Выход
#         """)
#
#         match option:
#             case "1":
#                 eng = input("Введите слово на английском: ")
#                 fr = input("Введите перевод на французском: ")
#                 dictionary[eng] = fr
#             case "2":
#                 del_word = input("Введите слово, которое хотите удалить: ")
#                 del dictionary[del_word]
#             case "3":
#                 f_word = input("Введите слово, которое хотите найти: ")
#                 print(f"Слово {f_word} переводится как {dictionary[f_word]}")
#             case "4":
#                 upd_word = input("Введите слово, которое хотите изменить: ")
#                 new_tr = input("Введите новый перевод: ")
#                 dictionary[upd_word] = new_tr
#             case "5":
#                 break
#
#
# dict_menu()

# Номер 3
# employees = {}
#
# def company_menu():
#     while True:
#         option = input("""Выберите опцию:
#         1 - Добавить нового сотрудника
#         2 - Удалить сотрудника
#         3 - Найти информацию о сотруднике
#         4 - Изменить информацию о сотруднике
#         5 - Выход
#         Ваш выбор: """)
#
#         match option:
#             case "1":
#                 full_name = input("Введите ФИО сотрудника: ")
#                 phone = input("Введите телефон сотрудника: ")
#                 email = input("Введите рабочий email: ")
#                 position = input("Введите должность: ")
#                 office = input("Введите номер кабинета: ")
#                 skype = input("Введите skype: ")
#
#                 employees[full_name] = {
#                     'Телефон': phone,
#                     'Email': email,
#                     'Должность': position,
#                     'Кабинет': office,
#                     'Skype': skype
#                 }
#                 print(f"Сотрудник {full_name} успешно добавлен!")
#
#             case "2":
#                 name_to_delete = input("Введите ФИО сотрудника для удаления: ")
#                 if name_to_delete in employees:
#                     del employees[name_to_delete]
#                     print(f"Сотрудник {name_to_delete} удален.")
#                 else:
#                     print("Такой сотрудник не найден.")
#
#             case "3":
#                 name_to_find = input("Введите ФИО сотрудника для поиска: ")
#                 if name_to_find in employees:
#                     print(f"\nИнформация о сотруднике {name_to_find}:")
#                     for key, value in employees[name_to_find].items():
#                         print(f"{key}: {value}")
#                 else:
#                     print("Сотрудник не найден.")
#
#             case "4":
#                 name_to_update = input("Введите ФИО сотрудника для изменения: ")
#                 if name_to_update in employees:
#                     print("\nКакие данные изменить?")
#                     field = input("Доступные поля: Телефон, Email, Должность, Кабинет, Skype: ")
#                     if field in employees[name_to_update]:
#                         new_value = input(f"Введите новое значение для {field}: ")
#                         employees[name_to_update][field] = new_value
#                         print("Данные успешно обновлены!")
#                     else:
#                         print("Некорректное поле.")
#                 else:
#                     print("Сотрудник не найден.")
#
#             case "5":
#                 if not employees:
#                     print("В базе нет сотрудников.")
#                 else:
#                     print("\nСписок всех сотрудников:")
#                     for name, data in employees.items():
#                         print(f"\n{name}:")
#                         for key, value in data.items():
#                             print(f"  {key}: {value}")
#
#             case "6":
#                 print("Выход из программы.")
#                 break
#
#             case _:
#                 print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 6.")
#
#
# company_menu()

# Номер 4
# books = {}
#
# def book_menu():
#     while True:
#         choice = input("""Опции:
# 1 - Добавить
# 2 - Удалить
# 3 - Найти
# 4 - Изменить
# 5 - Выход
# > """)
#
#         match choice:
#             case "1":
#                 title = input("Название: ")
#                 books[title] = {
#                     'Автор': input("Автор: "),
#                     'Жанр': input("Жанр: "),
#                     'Год': input("Год: "),
#                     'Страницы': input("Страницы: "),
#                     'Издательство': input("Издательство: ")
#                 }
#                 print(f"{title} добавлена!")
#
#             case "2":
#                 title = input("Название для удаления: ")
#                 books.pop(title, None)
#                 print(f"{title} удалена")
#
#             case "3":
#                 title = input("Название для поиска: ")
#                 print(f"\n{title}:")
#                 for k, v in books.get(title, {}).items():
#                     print(f"{k}: {v}")
#
#             case "4":
#                 title = input("Название для изменения: ")
#                 field = input("Поле (Автор/Жанр/Год/Страницы/Издательство): ")
#                 if title in books and field in books[title]:
#                     books[title][field] = input("Новое значение: ")
#                     print("Изменено!")
#
#             case "5":
#                 for title, data in books.items():
#                     print(f"\n{title}:")
#                     for k, v in data.items():
#                         print(f"{k}: {v}")
#
#             case "6":
#                 break
#
# book_menu()