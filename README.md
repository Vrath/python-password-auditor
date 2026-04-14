# Password Security Auditor

Skrypt w Pythonie który analizuje siłę hasła według 
standardów bezpieczeństwa NIST i OWASP.

## Co sprawdza

- Długość (minimum 12 znaków)
- Obecność wielkich i małych liter
- Obecność cyfr i znaków specjalnych
- Czy hasło nie jest na liście najpopularniejszych haseł (dictionary check)

## Jak uruchomić

python auditor.py

## Przykładowy wynik

✅ Długość >= 12 znaków (18 znaków)
✅ Zawiera wielką literę
✅ Zawiera małą literę  
✅ Zawiera cyfrę
✅ Zawiera znak specjalny

Wynik: 5/5  
Ocena: A — Silne hasło

## Czego się nauczyłem

Projekt wprowadził mnie w podstawy Pythona (funkcje, pętle, warunki) w kontekście security. Reguły oparte 
na wytycznych NIST SP 800-63B dotyczących haseł.