### Запуск проекта
Чтобы подключиться к базе данных нужная платформа. Как это сделать, будет показано на примере pgAdmin4.
В проекте параметры подключения выглядят так:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
```
Если настройки вашей платформы отличаются, то изменяем параметры тут в файле setting.py проекта.
В данном случае мы коннектимся к БД `my_bd`, имя пользовтеля - `postgres`, пароль -  `admin`, `locakhost` с портом `5432`.

В pgAdmin создаём БД `my_db`.

![image](https://github.com/zh0rchik/TestingTask/assets/99082375/3fece1c5-940d-40bd-a84e-5196b424d760)
![image](https://github.com/zh0rchik/TestingTask/assets/99082375/17cf2db2-09fe-4c1e-ba4a-bd734a51912c)

Вызываем контекстное меню, выбираем `Restore`.

![image](https://github.com/zh0rchik/TestingTask/assets/99082375/e5501691-8596-4e31-b241-ff803ea5b70d)

Указываем путь к файлу и `Restore`. (Примечение: )

![image](https://github.com/zh0rchik/TestingTask/assets/99082375/7d2ab801-7fc9-4788-8880-40c66fc0ff1f)

 Теперь можно подсоединяться к базе данных. Чтобы запустить сервер, в терминале из директории проекта выполняем команду:
```
python manage.py runserver
```

### Данные авторизации суперпользователя:
Login: admin

Email: admin@mail.ru

Password: admin

