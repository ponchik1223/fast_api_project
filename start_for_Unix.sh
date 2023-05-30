#!/bin/bash
project=$1
cd $project  # заходим в папку нужного проекта
docker-compose up --build -d # собираем контейнер 
sleep 5 #
python3 -m venv myenv # создаем виртуальное окружение
source myenv/bin/activate # активируем виртуальное окружение
pip install -r requirements.txt # подгружаем все необходимые библиотеки
echo "API $project готов к использованию!" 
python start_api.py # запускаем web-сервис
