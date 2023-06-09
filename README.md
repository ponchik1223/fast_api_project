
# project_1
## Описание функциональности
Проект представляет собой веб-сервис, разработанный с использованием FastAPI, для выполнения следующих действий:

1. Веб-сервис предоставляет POST REST-метод, который принимает запросы с данными в формате {"questions_num": integer}.

2. После получения запроса, сервис выполняет запрос к публичному API (англоязычные вопросы для викторин) по адресу https://jservice.io/api/random?count=questions_num, указывая количество вопросов, полученное из запроса.

3. Полученные ответы на запрос к публичному API сохраняются в базе данных PostgreSQL. В базе данных сохраняется следующая информация о каждом вопросе: ID вопроса, текст вопроса, текст ответа и дата создания вопроса. При сохранении проверяется, чтобы вопросы были уникальными, и в случае существования такого же вопроса выполняются дополнительные запросы к публичному API до получения уникального вопроса для викторины.
4. Ответом на запрос из пункта 2 веб-сервис возвращает предыдущий сохраненный вопрос для викторины. Если вопросов в базе данных нет, то возвращается пустой объект.


# project_2
## Описание функциональности
Проект представляет собой веб-сервис, который реализует следующие REST-методы:

1. Метод "Создание пользователя" (POST):
- Принимает запросы с именем пользователя.
- Создает нового пользователя в базе данных с указанным именем.
- Генерирует уникальный идентификатор пользователя и токен доступа в формате UUID.
- Возвращает сгенерированный идентификатор пользователя и токен доступа.
2. Метод "Добавление аудиозаписи" (POST):
- Принимает запросы с уникальным идентификатором пользователя, токеном доступа и аудиозаписью в формате WAV.
- Преобразует аудиозапись в формат MP3.
- Генерирует уникальный идентификатор в формате UUID для аудиозаписи.
- Сохраняет аудиозапись и ее идентификатор в базе данных.
- Возвращает URL для скачивания аудиозаписи вида "http://host:port/record?id=id_записи&user=id_пользователя".
3. Метод "Доступ к аудиозаписи" (GET):
- Предоставляет возможность скачать аудиозапись по предоставленной ссылке из метода "Добавление аудиозаписи".



## Процесс установки и запуска проекта

Для начала необходимо создать виртуальное окружение Python (Для корректной работы проекта необходима версия Python 3.10 и выше), чтобы изолировать зависимости проекта. Выполните следующие команды:

### Шаг 1: Проверка компонентов
Проверьте наличие библиотеки ffmpeg, если нет, то установите ее на свой компьютер

### Шаг 2: Установка Docker Compose
Для начала работы с проектом вам потребуется установить Docker Compose. Следуйте инструкциям ниже:

1. Перейдите на официальный сайт Docker по ссылке https://docs.docker.com/compose/install/.

2. Следуйте инструкциям, соответствующим вашей операционной системе, чтобы скачать и установить Docker Compose.

3. Убедитесь, что установка прошла успешно, выполнив команду docker-compose --version в командной строке. Если вы видите версию Docker Compose, значит, установка прошла успешно.

### Шаг 3: Запуск проекта
Для запуска нашего веб-сервиса необходимо выполнить следующие действия:

1. Скачайте проект с репозитория и перейдите в его корневую директорию.

2. В корневой директории проекта вы найдете скрипты запуска для различных операционных систем: start_for_Unix.sh для Linux и macOS, и start_for_windows.bat для Windows.

3. Откройте командную строку или терминал и перейдите в директорию проекта.

4. Выполните следующую команду, чтобы запустить проект:
- #### Для Linux и macOS:
```bash
chmod +x start_for_Unix.sh # Даем исполняемое разрешение скрипту
./start_for_Unix.sh "имя_проекта"
```

- #### Для Windows:

```bash
start_for_windows.bat "имя_проекта"
```

Здесь "имя_проекта" - это project_1/project_2, который вы хотите запустить.

5. Docker Compose загрузит и настроит необходимые контейнеры, базу данных PostgreSQL и запустит веб-сервис.

6. После успешного запуска проект будет доступен по адресу: 
- project_1_api: http://127.0.0.1:8000/docs
- project_2_api: http://127.0.0.1:9000/docs
