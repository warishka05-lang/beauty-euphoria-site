@echo off
echo Instaluje wymagane biblioteki Python...
pip install -r requirements.txt
echo.
echo Uruchamiam serwer Beauty Euphoria...
echo.
python server.py
pause
