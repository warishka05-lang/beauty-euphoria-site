#!/bin/bash
echo "Instaluje wymagane biblioteki Python..."
pip3 install -r requirements.txt
echo ""
echo "Uruchamiam serwer Beauty Euphoria..."
echo ""
python3 server.py
