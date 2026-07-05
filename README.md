# Beauty Euphoria — Instrukcja uruchomienia na komputerze

## Co potrzebujesz

- Zainstalowany Python (https://www.python.org/downloads/) — wersja 3.8 lub nowsza
- Wszystkie pliki tego projektu w jednym folderze

## Uruchomienie — Windows

1. Otwórz folder z plikami projektu
2. Kliknij dwukrotnie na plik `start_windows.bat`
3. Poczekaj, aż w oknie pojawi się napis "Beauty Euphoria - serwer wystartowal!"
4. Otwórz przeglądarkę i wejdź na adres: http://localhost:5000
5. Panel administracyjny: http://localhost:5000/admin.html (hasło: euphoria2026)

## Uruchomienie — Mac / Linux

1. Otwórz Terminal w folderze projektu
2. Wpisz: `chmod +x start_mac_linux.sh && ./start_mac_linux.sh`
3. Poczekaj na komunikat "Beauty Euphoria - serwer wystartowal!"
4. Otwórz przeglądarkę: http://localhost:5000
5. Panel administracyjny: http://localhost:5000/admin.html (hasło: euphoria2026)

## Uruchomienie ręczne (jeśli skrypty nie działają)

Otwórz terminal/wiersz polecenia w folderze projektu i wpisz:

```bash
pip install -r requirements.txt
python server.py
```

(na Mac/Linux czasem trzeba użyć `pip3` i `python3` zamiast `pip` i `python`)

## Ważne

- Serwer musi być włączony (okno terminala otwarte), aby strona działała
- Aby zamknąć serwer — zamknij okno terminala lub wciśnij Ctrl+C
- Dane (usługi, ceny, opinie) zapisują się w pliku `data.json` w tym samym folderze
- Zgłoszenia z formularza rezerwacji zapisują się w pliku `bookings.json`

## Zmiana hasła administratora

Domyślne hasło to `euphoria2026`. Aby je zmienić:

**Windows** — przed uruchomieniem `start_windows.bat`, w Wierszu polecenia wpisz:
```
set ADMIN_PASSWORD=twoje_nowe_haslo
start_windows.bat
```

**Mac/Linux** — w terminalu:
```bash
export ADMIN_PASSWORD=twoje_nowe_haslo
./start_mac_linux.sh
```

## Udostępnienie strony innym osobom w tej samej sieci Wi-Fi

Jeśli chcesz, aby np. właścicielka salonu zobaczyła stronę na swoim telefonie
podłączonym do tego samego Wi-Fi:

1. Sprawdź adres IP swojego komputera (Windows: `ipconfig`, Mac: `ifconfig`)
2. Na innym urządzeniu w tej samej sieci wejdź na: `http://TWOJE_IP:5000`

## Dodawanie zdjęć na stronę

Zdjęcia wgrywa się wyłącznie przez panel administracyjny — bez edycji kodu.

1. Wejdź na http://localhost:5000/admin.html i zaloguj się
2. Zakładka "Dane salonu" — sekcja "Zdjęcia strony głównej":
   - wgraj zdjęcie do bloku Hero (góra strony)
   - wgraj zdjęcie do sekcji "O salonie"
3. Zakładka "Usługi i cennik" — każda usługa ma swoje pole do wgrania zdjęcia (zamienia ikonę)
4. Zakładka "Portfolio" — każdy element portfolio ma pole do wgrania zdjęcia

Obsługiwane formaty: PNG, JPG, JPEG, WEBP, GIF.
Zdjęcia zapisują się automatycznie w folderze `images/` i są widoczne dla wszystkich odwiedzających.

## Podłączenie widżetu Booksy

1. Wejdź na http://localhost:5000/admin.html i zaloguj się
2. Zakładka "Rezerwacja (Booksy)"
3. Wklej kod widżetu skopiowany z Booksy Biz
4. Kliknij "Zapisz zmiany"
