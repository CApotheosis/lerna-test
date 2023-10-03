# ТЗ от Lerna: Тестовое задание к вакансии "Преподаватель курса Python Base" в Skillbox

Требования к формату

Решение тестовых задач 1-3 разместите в приватном репозитории в любой git системе github / bitbucket / gitlab, после необходимо дать доступ ks7100313@gmail.com. Для последнего задания создайте google docs с доступом “Редактировать можно всем, у кого есть ссылка”.

## Задание 1. Проанализируйте код.

```py
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "**": lambda a, b: a**b,
    "/": lambda a, b: a / b,
    "//": lambda a, b: a // b,
    "%": lambda a, b: a % b,
}

spam = operators.get("+")
print(spam(1, 2))
```

Перепишите код с использованием парадигмы ООП.

Требования к решению.

1. Код соответствует РЕР8.
2. Код имеет модульную структуру.
3. Используется type hinting (typing, collections.abc).
4. Особое внимание уделите неймингу.
5. Код отвечает рекомендациям SOLID.
6. Есть четкое разделение “реализация - интерфейс”.
7. Аргументов может быть больше двух (не только a, b).
8. Использованы минимум три паттерна проектирования “Декоратор”, “Фабричный метод”, “Одиночка”. “Декоратор” дополняет “Фабричный метод”. “Одиночка” используется для реализации простейшего логгера и может быть использован в связке со “Стратегией”. Например, пишем логи в консоль, если файл лога содержит более пяти строк (как показательное решение), то вывод в консоль.
9. При реализации обратите внимание, что калькуляторов может быть в будущем несколько, например, обычный, научный, инженерный и т.д.

## Задание 2. Не обязательное, но будет дополнительным плюсом если выполните.

Задача: спроектируйте API для онлайн-магазин породистых котят.

Используемые технологии: Flask, sqlalchemy + postgres, docker

Создайте простой портал для электронной библиотеки. Админка должна содержать две страницы:

список всех котиков с пагинацией (по 5 котов) и поиском. При нажатии на котика попадаем на вторую страницу
страница отдельного котика (на ней должен отображаться порода, картинка, имя, краткое описание и возраст в месяцах)

Должен поддерживаться полнотекстовый поиск по всем полям информации о котиках (порода, имя, возраст, описание). Должна быть возможность выбрать сортировку отдаваемого результата: по порода, по возрасту, по релевантности (сортировка по умолчанию)

Решение оформите в виде проекта на Flask в обвязке Docker контейнера. Запуск решения должен происходить по команде "docker-compose up". В магазине должно быть как минимум 20 котиков для проверки реализации.

Визуально проект не должен выглядеть отталкивающе. Мы любим котиков :-)

## Задание 3. (Проверка Soft скилов)

Два студента выполнили домашнее задание и прислали его на проверку. Ниже есть текст заданий и результат работы студентов. Определите, стоит принять выполненную работу или вернуть ее на доработку. Составьте ответ студенту по каждой задаче в отдельности.

Студент 1.

Задание: Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.

Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей, чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

[Решение студента](https://replit.com/@TopKesha/task1#main.py)

```py
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

ed, exp = 10000, 12000

m = 1
d = exp - ed
while m < 10:
	m += 1
	d += exp - ed
	exp *= 1.03
d = round(d, 2)
print('Студенту надо попросить', d, 'рублей.')
```

Комментарий: задание из модуля “Цикл while”

(Представьте, что студент прошел следующие темы: [Список](https://docs.google.com/spreadsheets/d/1oR_FPeQcRmF77_V1UuldBhCMX9sn31jImK0Eznl6W0A/edit#gid=0))

Ответьте студенту, который не правильно решил задание.

Студент 2.

Задание: По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней). Результат проверки вывести на консоль. Если номер месяца некорректен - сообщить об этом

[Решение студента](https://replit.com/@TopKesha/task2#main.py)

```py
# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
if month == 1:
    print('31 день')
elif month == 2:
    print('28 дней')
elif month == 3:
    print('31 день')
elif month == 4:
    print('30 дней')
elif month == 5:
    print('31 день')
elif month == 6:
    print('30 дней')
elif month == 7:
    print('31 день')
elif month == 8:
    print('31 день')
elif month == 9:
    print('30 дней')
elif month == 10:
    print('31 день')
elif month == 11:
    print('30 дней')
elif month == 12:
    print('31 день')
else:
    print('Такого месяца нет')
```

Комментарий: задание из модуля “Начало работы со списками”

Ответьте студенту, который правильно решил задание.

## Reference materials:

- [Website to purchase cats](https://www.avito.ru/all/koshki/poroda-abissinskaya-ASgBAgICAUSoA_QU)
- [How to return images in flask response?](https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response)
- [Send and receive images using Flask, Numpy and OpenCV](https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594)
- [Flask 101: Serve Images](https://naysan.ca/2021/02/28/flask-101-serve-images/)
- [Learn Django DRF - Building an Image API service](https://www.youtube.com/watch?v=ja5dCiMgyuk)
- [Managing files Django](https://docs.djangoproject.com/en/4.2/topics/files/#:~:text=Using%20files%20in%20models&text=The%20file%20is%20saved%20as,the%20model%20has%20been%20saved.&text=To%20save%20an%20existing%20file,core.)
- [File Uploads](https://docs.djangoproject.com/en/4.2/topics/http/file-uploads/)
- [Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)
- [Add a css class to a field in wtform](https://stackoverflow.com/questions/22084886/add-a-css-class-to-a-field-in-wtform)


"""py
Useful links
- https://docs.docker.com/compose/gettingstarted/
- Docker Compose + Postgres: Expose port: https://stackoverflow.com/questions/52567272/docker-compose-postgres-expose-port#:~:text=Each%20container%20can%20be%20accessed,running%20on%20the%20same%20compose.
- Official PSQl image on dockerhub: https://hub.docker.com/_/postgres/

└── services
    └── web
        ├── manage.py
        ├── project
        │   └── __init__.py
        └── requirements.txt
"""
