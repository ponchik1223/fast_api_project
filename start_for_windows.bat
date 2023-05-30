@echo off
set project=%1
cd %project%
docker-compose up --build -d
timeout /t 5 /nobreak
python -m venv myenv
call myenv\Scripts\activate
pip install -r requirements.txt
echo "API %project% готов к использованию!"

python start_api.py
