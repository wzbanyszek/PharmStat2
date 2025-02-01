import streamlit as st

def show():
    st.header("Wprowadzenie")
    st.write("""
    **Witaj w aplikacji Santo Pharmstat!**  
    Aplikacja umożliwia przeprowadzanie analizy danych statystycznych i jakościowych w prosty i intuicyjny sposób. W bocznym menu znajdziesz moduły, które pomogą Ci w analizie danych z różnych perspektyw.

    **Moduły dostępne w aplikacji:**

    1. **Wprowadzenie**  
       Ogólny przegląd funkcji aplikacji oraz instrukcje obsługi.

    2. **Statystyki opisowe**  
       Umożliwia wczytanie pliku Excel i obliczenie podstawowych statystyk opisowych, takich jak średnia, mediana, odchylenie standardowe, skośność i kurtoza. Wyniki można szybko porównać dla wielu kolumn.

    3. **Histogramy**  
       Generowanie histogramów dla danych z pliku Excel. Moduł oferuje ocenę normalności rozkładu (test Shapiro-Wilka) oraz analizę skośności i kurtozy.

    4. **Wykresy pudełkowe BoxPlot**  
       Wizualizacja rozkładu danych za pomocą wykresów pudełkowych (BoxPlot). Umożliwia szybkie wykrycie wartości odstających i porównanie rozkładów dla różnych zmiennych.

    5. **Karty kontrolne ImR**  
       Tworzenie kart kontrolnych ImR (Individual & Moving Range), które pomagają monitorować stabilność procesów produkcyjnych. Moduł umożliwia identyfikację odchyleń i trendów w danych.

    6. **Analiza zdolności procesowej**  
       Ocena zdolności procesu na podstawie wskaźników Cp i Cpk. Pozwala określić, na ile proces spełnia wymagania specyfikacji i czy jest stabilny.

    7. **Regresja dla stabilności**  
       Analiza danych stabilnościowych z wykorzystaniem regresji liniowej. Moduł umożliwia ocenę zmian parametrów w czasie oraz wizualizację danych z uwzględnieniem limitów specyfikacji.

    8. **Analiza temperatury i wilgotności**  
       Analiza danych środowiskowych, takich jak temperatura i wilgotność. Umożliwia identyfikację przekroczeń limitów specyfikacji i wizualizację zmian w czasie.

    ---
    **Jak korzystać z aplikacji?**  
    - Wybierz interesującą Cię podstronę w bocznym panelu.
    - Wczytaj dane do analizy przy pomocy wbudowanych formularzy.
    - Wyniki analizy (wykresy, tabele, statystyki) pojawią się w głównym obszarze strony.
    - Możesz ukrywać lub wyświetlać szczegóły analizy, dostosowując widok do swoich potrzeb.
    """)
