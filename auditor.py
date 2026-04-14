# auditor.py

def sprawdz_reguly(haslo):
    """
    Sprawdza hasło według 5 reguł bezpieczeństwa.
    Zwraca listę wyników — każdy wynik to słownik z nazwą i czy przeszło.
    """

    znaki_specjalne = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

    reguly = [
        {
            "nazwa": "Długość >= 12 znaków",
            "zaliczona": len(haslo) >= 12,
            "szczegol": f"({len(haslo)} znaków)"
        },
        {
            "nazwa": "Zawiera wielką literę",
            "zaliczona": any(znak.isupper() for znak in haslo),
            "szczegol": ""
        },
        {
            "nazwa": "Zawiera małą literę",
            "zaliczona": any(znak.islower() for znak in haslo),
            "szczegol": ""
        },
        {
            "nazwa": "Zawiera cyfrę",
            "zaliczona": any(znak.isdigit() for znak in haslo),
            "szczegol": ""
        },
        {
            "nazwa": "Zawiera znak specjalny",
            "zaliczona": any(znak in znaki_specjalne for znak in haslo),
            "szczegol": f"(np. {znaki_specjalne[:8]}...)"
        },
    ]

    return reguly

# Top 20 najpopularniejszych haseł na świecie
POPULARNE_HASLA = [
    "password", "123456", "123456789", "12345678", "12345",
    "1234567", "password1", "iloveyou", "admin", "welcome",
    "monkey", "login", "abc123", "starwars", "dragon",
    "master", "hello", "letmein", "qwerty", "sunshine"
]

def sprawdz_popularne(haslo):
    return haslo.lower() in POPULARNE_HASLA


def main():
    print("=== RAPORT BEZPIECZEŃSTWA HASŁA ===\n")
    haslo = input("Wpisz hasło do sprawdzenia: ")
    print()

    reguly = sprawdz_reguly(haslo)

    # Wyświetl każdą regułę
    for regula in reguly:
        ikona = "✅" if regula["zaliczona"] else "❌"
        print(f"{ikona} {regula['nazwa']} {regula['szczegol']}")
        
    if sprawdz_popularne(haslo):
        print("⚠️  UWAGA: To hasło znajduje się na liście najczęściej używanych haseł!")
        print("    Jest pierwszym kandydatem w atakach słownikowych.\n")


main()