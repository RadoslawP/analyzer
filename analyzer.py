"""
Moduł analyzer analizuje tekst na podstawie wzoru na obliczanie indeksu czytelności
Flescha i zwraca odpowiedni wynik. Wynik zostaje następnie przekonwertowany na kategorię
czytelności, wskazującą wykształcenie odpowiadające poziomowi trudności tekstu.
Uwaga: Moduł dostosowany jest do gramatyki w języku angielskim.
"""
#zliczanie sylab w tekscie
def policz_sylaby(slowa):
    """
    Ta funkcja pobiera listę słów i zwraca łączną liczbę sylab wszystkich słów z listy.
    """
    liczba = 0

    for slowo in slowa:
        liczba_slow = policz_sylaby_w_slowie(slowo)
        liczba = liczba + liczba_slow
    return liczba

#zliczanie sylab w pojedynczym słowie
def policz_sylaby_w_slowie(slowo):
    """
    Ta funkcja pobiera słowo w formie łańcucha i zweaca liczbę sylab. Zauważ,
    że jest  to heurystyka i może nie zweacać stuprocentowo dokładnego wyniku.
    """
    liczba = 0

    #usówanie znaków interpunkcyjnych po wyrazie
    koncowki = ',.;:!?'
    ostatni_znak = slowo[-1]

    if ostatni_znak in koncowki:
        przetworzone_slowo = slowo[0:-1]
    else:
        przetworzone_slowo = slowo

    #wyrazy trzy znakowe licone jako jedna sylaba
    if len(przetworzone_slowo) <= 3:
        return 1

    #sprawdzanie niemego e na koncu slowa
    if przetworzone_slowo[-1] in 'eE':
        przetworzone_slowo = przetworzone_slowo[0:-1]

    #zliczanie samogłosek w wyrazie
    samogloski = "aeiouAEIOU"
    poprzedni_znak_byl_samogloska = False

    for znak in przetworzone_slowo:
        if znak in samogloski:
            #sprawdzanie podwójnych samoglosek
            if not poprzedni_znak_byl_samogloska:
                liczba = liczba + 1
            poprzedni_znak_byl_samogloska = True
        else:
            poprzedni_znak_byl_samogloska = False

    #doliczanie y na koncu slowa
    if przetworzone_slowo[-1] in 'yY':
        liczba = liczba + 1

    return liczba

#zliczanie zdan na podstawie znaków interpunkcyjnych
def policz_zdania(tekst):
    """
    Ta funkcja liczy zdania w łańcuchu tekstowym, używając kropek, średników,
    znaków zapytania i wykrzykników jako znaków końcowych.
    """
    liczba = 0
    koncowe = '.?!'
    for znak in tekst:
        if znak in koncowe:
            liczba = liczba + 1
    return liczba

#wynik czytelności
def zwroc_wynik(wynik):
    """
    Ta funkcja pobiera wynik czytelności Flescha i wyświetla odpowiadający mu
    poziom trudności.
    """
    if wynik >= 90.0:
        print('5 klasa podstawówki')
    elif wynik >= 80.0:
        print('6 klasa podstawówki')
    elif wynik >= 70.0:
        print('7 klasa podstawówki')
    elif wynik >= 60.0:
        print('8 klasa podstawówki, 1 klasa liceum')
    elif wynik >= 50.0:
        print('2-4 klasa liceum')
    elif wynik >= 30.0:
        print('studia licencjackie')
    else:
        print('studia magisterskie')

#funkcja szacująca czutelność tekstu
def oblicz_czytelnosc(tekst):
    """
    Ta funkcja pobiera łańcuch tekstowy dowolnej długości
    i wyświetla poziom trudności tekstu.
    """
    liczba_slow = 0
    liczba_zdan = 0
    liczba_sylab = 0
    wynik = 0

    slowa = tekst.split()
    liczba_slow = len(slowa)
    liczba_zdan = policz_zdania(tekst)
    liczba_sylab = policz_sylaby(slowa)

    wynik = (206.835 - 1.015 * (liczba_slow / liczba_zdan)
            - 84.6 * (liczba_sylab / liczba_slow))

    print(liczba_slow, 'słów')
    print(liczba_zdan, 'zdań')
    print(liczba_sylab, 'sylab')
    print(wynik, 'indeks czytelności')

    zwroc_wynik(wynik)

#sprawdzanie czy kod jest uruchamiany w ramach modułu czy main
if __name__ == "__main__":
    #importowanie tekstu testowego
    import ch1text
    print('Tekst testowy:')
    oblicz_czytelnosc(ch1text.tekst)
