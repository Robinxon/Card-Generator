# Card-Generator (Generator Kart)
Aplikacja do generowania kart numerycznych gotowych do druku.

## Opis

Ten skrypt Python generuje pliki PDF zawierające dwustronne karty z numerami (1-99) zoptymalizowane do druku. Karty zawierają:
- **Przód karty**: Duże, wycentrowane, podkreślone numery z czarnym obramowaniem do cięcia
- **Tył karty**: Duże, wycentrowane, podkreślone numery (bez obramowania)

Idealne dla materiałów edukacyjnych, gier lub każdej aplikacji wymagającej ponumerowanych kart.

## Funkcje

- ✅ Generowanie kart z numerami od 1 do 99
- ✅ Dwustronna konstrukcja z podkreślonymi numerami po obu stronach
- ✅ Czarne obramowanie na przedniej stronie dla precyzyjnego wycinania
- ✅ Naprzemienne strony przednie i tylne dla łatwego druku dwustronnego
- ✅ Konfigurowalne wymiary kart
- ✅ Elastyczny wybór numerów (generowanie tylko określonych numerów)
- ✅ Automatyczna optymalizacja układu dla papieru A4
- ✅ Gotowy do druku plik PDF

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Robinxon/Card-Generator.git
cd Card-Generator
```

2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

## Użycie

### Podstawowe użycie

Wygeneruj wszystkie karty (1-99):
```bash
python card_generator.py -o karty.pdf
```

### Generowanie określonych numerów

Wygeneruj karty dla numerów 1-10:
```bash
python card_generator.py -n "1-10" -o karty_1-10.pdf
```

Wygeneruj określone numery (np. 1-10, 15 i 20-25):
```bash
python card_generator.py -n "1-10,15,20-25" -o karty_wybrane.pdf
```

### Niestandardowe wymiary kart

Wygeneruj karty o niestandardowych wymiarach (np. 70mm × 100mm):
```bash
python card_generator.py -w 70 -H 100 -o duze_karty.pdf
```

### Niestandardowa czcionka

Użyj innej czcionki (wbudowanej lub niestandardowej):
```bash
# Użyj wbudowanej czcionki
python card_generator.py -f "Times-Bold" -o karty.pdf

# Użyj pliku z czcionką
python card_generator.py -f "/sciezka/do/czcionki.ttf" -o karty.pdf
```

### Wszystkie opcje

```
użycie: card_generator.py [-h] [-n NUMERY] [-o PLIK_WYJŚCIOWY] [-w SZEROKOŚĆ] [-H WYSOKOŚĆ] [-f CZCIONKA]

Generuj plik PDF z ponumerowanymi kartami do druku

opcje:
  -h, --help            pokaż tę wiadomość pomocy i wyjdź
  -n NUMERY, --numbers NUMERY
                        Numery do wygenerowania (np. "1-99", "1-10,15,20-25"). 
                        Domyślnie: 1-99
  -o PLIK_WYJŚCIOWY, --output PLIK_WYJŚCIOWY
                        Nazwa pliku PDF wyjściowego. Domyślnie: cards.pdf
  -w SZEROKOŚĆ, --width SZEROKOŚĆ
                        Szerokość karty w milimetrach. Domyślnie: 63mm (rozmiar karty pokerowej)
  -H WYSOKOŚĆ, --height WYSOKOŚĆ
                        Wysokość karty w milimetrach. Domyślnie: 88mm (rozmiar karty pokerowej)
  -f CZCIONKA, --font CZCIONKA
                        Nazwa czcionki lub ścieżka do pliku .ttf. Domyślnie: Helvetica-Bold
```

## Przykłady

### Przykład 1: Standardowe karty rozmiaru pokerowego (wszystkie numery)
```bash
python card_generator.py -o karty_1-99.pdf
```

### Przykład 2: Dodrukowanie tylko brakujących kart
Jeśli musisz dodrukować karty 45-50:
```bash
python card_generator.py -n "45-50" -o dodruk_45-50.pdf
```

### Przykład 3: Karty o niestandardowym rozmiarze
Utwórz większe karty (80mm × 120mm):
```bash
python card_generator.py -w 80 -H 120 -o duze_karty.pdf
```

### Przykład 4: Wiele zakresów
Wygeneruj karty: 1-20, 50 i 80-90:
```bash
python card_generator.py -n "1-20,50,80-90" -o wybrane_karty.pdf
```

### Przykład 5: Niestandardowa czcionka
Użyj innej czcionki dla numerów:
```bash
# Wbudowana czcionka
python card_generator.py -f "Times-Roman" -o karty_times.pdf

# Plik z czcionką
python card_generator.py -f "/sciezka/do/czcionki.ttf" -o karty_niestandardowe.pdf
```

## Instrukcje drukowania

1. **Wygeneruj PDF** używając jednego z powyższych poleceń
2. **Ustawienia druku**:
   - Użyj druku dwustronnego (duplex)
   - Wybierz "Odwróć na krótkiej krawędzi" dla prawidłowego wyrównania
   - Użyj rzeczywistego rozmiaru (100% skali, bez dopasowania)
   - Użyj grubego papieru (200-300g/m²) dla lepszej jakości kart
3. **Wycinanie**:
   - Czarne obramowanie na przedniej stronie służy jako wskazówka do wycinania
   - Użyj gilotyny papierowej lub noża do rękodzieła dla czystych krawędzi
   - Ciąć wzdłuż zewnętrznej krawędzi czarnego obramowania

## Układ kart

Skrypt automatycznie oblicza optymalny układ dla papieru A4 na podstawie wymiarów karty:
- **Standardowe karty (63×88mm)**: 3 karty na rząd, 3 karty na kolumnę (9 kart na stronę)
- PDF zawiera naprzemienne strony przednie i tylne (strona 1: przód, strona 2: tył, strona 3: przód, itd.)
- Obie strony wyświetlają numer z podkreśleniem
- Przednia strona ma czarne obramowanie do cięcia
- Strony tylne są odbite poziomo dla prawidłowego wyrównania podczas druku dwustronnego

## Wymagania

- Python 3.6+
- reportlab 4.0.0+

## Licencja

Ten projekt jest open source i dostępny do użytku osobistego i komercyjnego.

## Wkład

Wkłady są mile widziane! Nie wahaj się przesłać Pull Request.

## Wsparcie

Jeśli napotkasz jakiekolwiek problemy lub masz pytania, otwórz zgłoszenie na GitHub.
