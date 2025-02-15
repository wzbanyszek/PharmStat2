translations = {
"Polski": {
        "general": {
            "menu_title": "Menu",
            "intro": "Witaj w aplikacji Pharmstat2!",
            "intro_desc": "Aplikacja umożliwia przeprowadzanie analizy danych statystycznych i jakościowych w prosty i intuicyjny sposób. W bocznym menu znajdziesz moduły, które pomogą Ci w analizie danych z różnych perspektyw.",
            "choose_page": "Wybierz podstronę:",
            "upload_data": "Wczytaj dane do analizy przy pomocy wbudowanych formularzy.",
            "view_results": "Wyniki analizy (wykresy, tabele, statystyki) pojawią się w głównym obszarze strony.",
            "customize_view": "Możesz ukrywać lub wyświetlać szczegóły analizy, dostosowując widok do swoich potrzeb.",
            "how_to_use": "Jak korzystać z aplikacji?"
        },
        "descriptive_statistics": {
            "title": "Statystyki opisowe",
            "show_instructions": "Pokaż instrukcje",
            "descriptive_stats": "Statystyki opisowe",
            "descriptive_stats_desc": "Obliczanie podstawowych statystyk, takich jak średnia, mediana, odchylenie standardowe. Moduł ten pozwala na szybkie i łatwe uzyskanie podstawowych informacji o Twoich danych, co jest kluczowe dla dalszej analizy. Statystyki opisowe są fundamentem analizy danych, ponieważ umożliwiają szybkie zrozumienie rozkładu i zmienności danych.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nagłówki kolumn określające nazwy zmiennych, np. \"Zawartość substancji czynnej\" lub \"Wilgotność\". Kolejne wiersze powinny zawierać wartości liczbowe odpowiadające tym zmiennym. Każda kolumna reprezentuje inną zmienną do analizy.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_columns": "Wybierz kolumny, dla których chcesz obliczyć statystyki opisowe.",
                "stats_summary": "Otrzymasz zestawienie najważniejszych statystyk, takich jak średnia, mediana, odchylenie standardowe i inne.",
                "normality_skew_kurtosis": "Dodatkowo ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie.",
                "interpretation": "Interpretacja wyników: Średnia określa wartość przeciętną, mediana wskazuje środek zbioru danych, a odchylenie standardowe informuje o zmienności wyników. Wysoka skośność może wskazywać na asymetrię rozkładu, a wysoka kurtoza na obecność wartości odstających."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd wczytanych danych",
                "data_preview": "Podgląd wczytanych danych (pierwsze 10 wierszy):",
                "select_columns": "Wybierz kolumny do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "statistics": {
                "shapiro_test": "Shapiro-Wilk p-wartość",
                "skewness": "Skośność",
                "kurtosis": "Kurtoza"
            }
        },
        "histogram_analysis": {
            "title": "Analiza histogramów",
            "show_instructions": "Pokaż instrukcje",
            "histograms": "Histogramy",
            "histograms_desc": "Tworzenie histogramów z oceną normalności rozkładu i analizą skośności oraz kurtozy. Dzięki temu modułowi możesz wizualizować rozkład swoich danych i ocenić, czy mają one charakterystykę rozkładu normalnego. Histogramy są użytecznym narzędziem do identyfikacji kształtu rozkładu danych oraz do wykrywania ewentualnych odchyleń lub anomalii.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nazwy zmiennych opisujące typ danych, np. \"Wyniki badania stężenia\". Każda kolumna powinna reprezentować jedną serię pomiarową. Kolejne wiersze powinny zawierać wartości liczbowe bez pustych komórek.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_column": "Wybierz kolumnę do analizy, aby wygenerować histogram i wyświetlić statystyki opisowe.",
                "normality_test": "Ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie.",
                "interpretation": "Interpretacja wyników: Histogram pozwala ocenić kształt rozkładu danych. Jeśli histogram ma kształt dzwonowy, sugeruje to rozkład normalny. Skośność histogramu może wskazywać na asymetrię wyników, a szerokość rozkładu świadczy o rozrzucie wartości."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "select_column": "Wybierz kolumnę do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "statistics": {
                "sample_size": "Liczba próbek",
                "mean": "Średnia",
                "std_dev": "Odchylenie standardowe",
                "max": "Maksimum",
                "min": "Minimum",
                "median": "Mediana",
                "rsd": "Współczynnik zmienności (RSD %)",
                "shapiro_test": "Test Shapiro-Wilka",
                "skewness": "Skośność",
                "kurtosis": "Kurtoza"
            },
            "plot": {
                "histogram_title": "Histogram danych",
                "x_label": "Wartości",
                "y_label": "Częstość"
            },
            "normality_results": {
                "normal_distribution": "Brak podstaw do odrzucenia hipotezy o normalności rozkładu.",
                "non_normal_distribution": "Dane nie pochodzą z rozkładu normalnego."
            }
        },
        "boxplot_charts": {
            "title": "Wykresy BoxPlot",
            "show_instructions": "Pokaż instrukcje",
            "boxplot": "Wykresy pudełkowe BoxPlot",
            "boxplot_desc": "Wizualizacja rozkładu danych i identyfikacja wartości odstających. Wykresy pudełkowe umożliwiają szybkie zrozumienie rozkładu danych, pokazując medianę, kwartyle oraz wartości odstające. Są one szczególnie przydatne w identyfikacji potencjalnych błędów pomiarowych lub nietypowych obserwacji.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nazwy grup danych, np. \"Seria 1\", \"Seria 2\", \"Seria 3\". Każda kolumna reprezentuje inną grupę porównawczą. Kolejne wiersze powinny zawierać wartości liczbowe przypisane do danej grupy.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_columns": "Wybierz kolumny do analizy, aby wygenerować wykresy BoxPlot.",
                "view_stats": "Otrzymasz statystyki opisowe dla wybranych kolumn.",
                "interpretation": "Interpretacja wyników: Wykres pudełkowy pozwala ocenić medianę, rozstęp międzykwartylowy oraz obecność wartości odstających. Długie wąsy mogą wskazywać na duże zróżnicowanie danych, a pojedyncze punkty poza wąsami sugerują obecność wartości odstających."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx, xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 5 wierszy):",
                "select_columns": "Wybierz kolumny do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "plot": {
                "title": "Wykresy BoxPlot dla wybranych kolumn",
                "y_label": "Wartości"
            },
            "statistics": {
                "title": "Statystyki opisowe"
            }
        },
        "control_charts": {
            "title": "Karty kontrolne ImR",
            "show_instructions": "Pokaż instrukcje",
            "control_charts": "Karty kontrolne ImR",
            "control_charts_desc": "Monitorowanie stabilności procesów za pomocą kart kontrolnych ImR. Karty kontrolne pozwalają na śledzenie zmian w procesach produkcyjnych lub badawczych, wykrywając ewentualne odchylenia od normy. Są niezbędnym narzędziem w zarządzaniu jakością i ciągłym doskonaleniu procesów.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nagłówki kolumn, gdzie pierwszy kolumna to identyfikatory próbek lub numery serii, a kolejne kolumny zawierają wartości pomiarowe. Jeśli plik zawiera więcej niż jedną kolumnę z wynikami, użytkownik będzie mógł wybrać, którą analizować.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "data_format": "Plik powinien zawierać dwie kolumny: daty lub ID próbek oraz dane liczbowe.",
                "extra_columns": "Jeśli plik zawiera więcej niż 2 kolumny, dodatkowe kolumny zostaną pominięte.",
                "chart_info": "Generowane będą wykresy ImR, w tym wykres wartości indywidualnych (I) oraz ruchomego rozstępu (MR).",
                "interpretation": "Interpretacja wyników: Karty kontrolne pozwalają monitorować stabilność procesu. Punkty znajdujące się poza liniami kontrolnymi mogą wskazywać na nieprawidłowości w procesie. Wykrycie trendów lub serii wartości po jednej stronie średniej może sugerować systematyczne zmiany w procesie."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej.",
                "error_two_columns": "Plik musi zawierać co najmniej 2 kolumny (Czas/ID, Wartość).",
                "warning_extra_columns": "Plik zawiera dodatkowe kolumny:",
                "select_result_column": "Wybierz kolumnę z wynikami do analizy:",
                "select_result_column_help": "Wybierz kolumnę zawierającą dane, które chcesz przeanalizować na karcie kontrolnej.",
                "using_first_two": "Wykorzystane zostaną tylko pierwsze dwie kolumny."
            },
            "chart_labels": {
                "time_series": "Czas/ID",
                "values": "Wartość",
                "individual_values": "I (Wartości indywidualne)",
                "moving_range": "MR (ruchomy rozstęp)",
                "observation": "Obserwacja"
            },
            "analysis_results": {
                "normal_distribution_check": "Czy rozkład wartości I jest normalny (test α=0.05)?",
                "process_stable": "Czy proces jest stabilny wg reguł?",
                "show_I_chart": "Pokaż dane wykresu I (wartości indywidualne)",
                "show_MR_chart": "Pokaż dane wykresu MR (ruchomy rozstęp)",
                "I_chart_data": "Dane wykresu I (wartości indywidualne)",
                "MR_chart_data": "Dane wykresu MR (ruchomy rozstęp)"
            }
        },
        "process_capability": {
            "title": "Analiza zdolności procesowej",
            "show_instructions": "Pokaż instrukcje",
            "process_capability": "Analiza zdolności procesowej",
            "process_capability_desc": "Ocena zdolności procesu na podstawie wskaźników Cp i Cpk. Analiza zdolności procesowej pozwala ocenić, czy proces jest w stanie spełniać określone wymagania jakościowe. Wskaźniki Cp i Cpk pomagają w identyfikacji potencjalnych problemów i obszarów do poprawy.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nazwy zmiennych, np. \"Średnica tabletki\" lub \"Wilgotność proszku\". Kolejne wiersze powinny zawierać wartości liczbowe odpowiadające danej zmiennej. Każda kolumna reprezentuje oddzielną analizowaną cechę produktu.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "set_spec_limits": "Ustaw dolną (LSL) i górną (USL) granicę specyfikacji oraz wartość docelową (Target).",
                "view_results": "Otrzymasz wykres analizy zdolności procesowej oraz wskaźniki Cp i Cpk.",
                "interpretation": "Interpretacja wyników: Wskaźniki Cp i Cpk oceniają zdolność procesu do spełnienia wymagań specyfikacji. Wartość Cp > 1.33 sugeruje dobrą zdolność procesu, natomiast Cpk uwzględnia zarówno zmienność, jak i przesunięcie względem środka specyfikacji."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "select_column": "Wybierz kolumnę do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "spec_settings": {
                "target": "Wartość docelowa (Target)",
                "lsl": "Dolna granica specyfikacji (LSL)",
                "usl": "Górna granica specyfikacji (USL)"
            },
            "plot": {
                "title": "Analiza zdolności procesowej",
                "x_label": "Wartości",
                "y_label": ""
            },
            "results": {
                "header": "Wyniki analizy",
                "cp": "Cp",
                "cpk": "Cpk",
                "sample_size": "Liczba próbek",
                "sample_mean": "Średnia próbki",
                "sample_std": "Odchylenie standardowe",
                "sample_max": "Maksimum",
                "sample_min": "Minimum",
                "sample_median": "Mediana",
                "pct_below_lsl": "Procent próbek poniżej LSL",
                "pct_above_usl": "Procent próbek powyżej USL"
            }
        },
        "stability_regression": {
            "title": "Analiza danych ze stabilności",
            "show_instructions": "Pokaż instrukcje",
            "stability_regression": "Regresja dla stabilności",
            "stability_regression_desc": "Analiza regresji dla danych stabilnościowych. Regresja stabilnościowa umożliwia przewidywanie trwałości produktów na podstawie wyników długoterminowych badań stabilności. Jest to kluczowe w przemyśle farmaceutycznym i spożywczym, gdzie stabilność produktów ma bezpośredni wpływ na ich bezpieczeństwo i skuteczność.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nagłówki kolumn, gdzie pierwsza kolumna to nazwa badanego parametru (np. \"Zawartość API\", \"Wilgotność\"), druga kolumna to wartości czasu (np. \"Czas [miesiące]\"), trzecia kolumna to dolna specyfikacja (\"LSL\"), czwarta kolumna to górna specyfikacja (\"USL\"), a kolejne kolumny zawierają wyniki pomiarów dla poszczególnych serii produktów. Wartości muszą być liczbowe, a w przypadku brakujących danych komórki powinny pozostawać puste.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane stabilności.",
                "display_series": "Na wykresie zostaną wyświetlone wybrane serie wraz z liniami regresji.",
                "view_regression_results": "Pod wykresem znajdziesz tabelę z parametrami regresji dla wybranych serii.",
                "interpretation": "Interpretacja wyników: Regresja liniowa pomaga określić trend zmian wartości parametru w czasie. Współczynnik determinacji R² bliski 1 wskazuje na dobrą dopasowalność modelu do danych. Nachylenie linii regresji pokazuje, czy wartości parametru rosną, maleją czy pozostają stabilne."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 12 wierszy):",
                "select_series": "Wybierz serie do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "plot": {
                "data": "dane",
                "regression": "regresja",
                "spec_limit": "Limit specyfikacji",
                "x_label": "Czas (mies.)",
                "title": "Analiza stabilności"
            },
            "regression_results": {
                "header": "Wyniki analizy regresji dla wybranych serii",
                "series": "Seria",
                "slope": "Nachylenie (slope)",
                "intercept": "Wyraz wolny (intercept)",
                "r_value": "Współczynnik korelacji (r)",
                "p_value": "P-значenie (p-value)",
                "std_err": "Стандартная ошибка"
            }
        },
        "temp_humidity_analysis": {
            "title": "Analiza temperatury i wilgotności",
            "show_instructions": "Pokaż instrukcje",
            "temp_humidity": "Analiza temperatury i wilgotności",
            "temp_humidity_desc": "Analiza danych środowiskowych i identyfikacja przekroczeń limitów. Moduł ten pozwala na monitorowanie warunków środowiskowych, takich jak temperatura i wilgotność, oraz wykrywanie ewentualnych przekroczeń ustalonych limitów. Jest to szczególnie ważne w procesach produkcyjnych i magazynowych, gdzie warunki środowiskowe mogą wpływać na jakość i trwałość produktów.",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nagłówki kolumn, gdzie pierwsza kolumna to data lub znacznik czasu (\"Data\"), druga kolumna to wartości temperatury (\"Temperatura [°C]\"), trzecia kolumna to wartości wilgotności (\"Wilgotność [%]\"). Wszystkie wartości muszą być liczbowe, a format dat musi być jednolity w całym pliku.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane temperatury i wilgotności.",
                "set_limits": "Ustaw limity temperatury i wilgotności za pomocą suwaków.",
                "view_results": "Przeglądaj wykresy oraz listę przekroczeń limitów.",
                "interpretation": "Interpretacja wyników: Wykresy temperatury i wilgotności pomagają monitorować warunki środowiskowe. Stabilne wartości oznaczają dobrą kontrolę warunków przechowywania. Znaczne wahania mogą sugerować problemy z utrzymaniem warunków stabilności."
            },
            "settings": {
                "temp_lower": "Dolna granica temperatury (°C)",
                "temp_upper": "Górna granica temperatury (°C)",
                "hum_lower": "Dolna granica wilgotności (%)",
                "hum_upper": "Górna granica wilgotności (%)"
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx, xls):",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "statistics": {
                "temp_stats": "Statystyki temperatury",
                "hum_stats": "Statystyki wilgotności",
                "mean": "Średnia",
                "min": "Min",
                "max": "Max",
                "rsd": "Współczynnik zmienności (RSD %)"
            },
            "thresholds": {
                "crossings": "Przekroczenia limitów",
                "no_crossings": "Brak przekroczeń granic temperatury / wilgotności.",
                "time": "Czas",
                "temperature": "Temperatura",
                "humidity": "Wilgotność"
            },
            "plot": {
                "temp": "Temperatura",
                "hum": "Wilgotność",
                "temp_lower_limit": "Dolna granica temperatury",
                "temp_upper_limit": "Górna granica temperatury",
                "hum_lower_limit": "Dolna granica wilgotności",
                "hum_upper_limit": "Górna granica wilgotności",
                "x_label": "Czas",
                "y_label": "Wartość",
                "title": "Temperatura i Wilgotność"
            }
        },
        "pqr_module": {
            "title": "Moduł PQR",
            "show_instructions": "Pokaż instrukcje",
            "pqr_module": "Moduł PQR",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nagłówki kolumn, gdzie pierwsza kolumna to identyfikatory próbek lub numery serii (\"Seria\"), a kolejne kolumny to wartości pomiarowe dla różnych parametrów jakościowych (\"Zawartość API\", \"Wilgotność\"). Jeśli plik zawiera więcej niż jedną kolumnę z danymi, użytkownik będzie mógł wybrać, którą analizować. Użytkownik będzie mógł także podać dolną i górną granicę specyfikacji.",
                "header": "Instrukcje",
                "upload_file": "Prześlij plik z danymi",
                "select_series": "Wybierz serię do analizy",
                "input_spec_limits": "Wprowadź górny i dolny limit specyfikacji",
                "view_charts": "Wyświetl wykresy",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Wybierz plik",
                "error_two_columns": "Plik musi zawierać co najmniej dwie kolumny",
                "select_result_column": "Wybierz kolumnę z wynikami",
                "select_result_column_help": "Wybierz kolumnę zawierającą dane do analizy",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych",
                "error_no_numeric_data": "Brak danych numerycznych do analizy",
                "error_processing_file": "Błąd podczas przetwarzania pliku",
                "no_file_uploaded": "Plik nie przesłano"
            },
            "chart_labels": {
                "time_series": "Identyfikator serii",
                "values": "Wartości",
                "observation": "Obserwacja",
                "individual_values": "Wartości indywidualne",
                "moving_range": "Zakres ruchomy",
                "frequency": "Częstotliwość",
                "histogram_with_spec_limits": "Histogram z limitami specyfikacji",
                "control_chart_with_spec_limits": "Karta kontrolna z limitami specyfikacji"
            },
            "subheaders": {
                "imr_chart": "Karta kontrolna ImR",
                "cpk_analysis": "Analiza zdolności procesowej Cpk",
                "spec_limits_comparison": "Porównanie wyników z limitami specyfikacji"
            },
            "spec_limits": {
                "usl": "Górny limit specyfikacji (USL)",
                "lsl": "Dolny limit specyfikacji (LSL)"
            },
            "warnings": {
                "spec_limits_equal": "Górny i dolny limit specyfikacji są równe. Wprowadź poprawne wartości."
            },
            "cpk_results": {
                "mean": "Średnia",
                "std_dev": "Odchylenie standardowe",
                "cpk": "Wskaźnik Cpk"
            }
        },
        "anova_module": {
            "title": "Analiza Wariancji (ANOVA)",
            "show_instructions": "Pokaż instrukcje",
            "anova_module": "Analiza Wariancji (ANOVA)",
            "instructions": {
                "prepare_file": "Podaj plik Excel zgodnie z wymaganiami modułu.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane dla różnych grup.",
                "select_groups": "Wybierz grupy do analizy.",
                "perform_anova": "Przeprowadź analizę wariancji (ANOVA) dla wybranych grup.",
                "view_results": "Zobacz wyniki testu ANOVA oraz testu Tukeya.",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd wczytanych danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "select_groups": "Wybierz grupy do analizy:",
                "error_two_columns": "Plik musi zawierać co najmniej 2 kolumny z danymi.",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "warnings": {
                "need_two_groups": "Wybierz co najmniej dwie grupy do analizy."
            },
            "anova_results": {
                "header": "Wyniki analizy wariancji (ANOVA)",
                "statistic": "F-Statystyka",
                "p_value": "P-Wartość",
                "significant_result": "Między grupami są istotne statystycznie różnice.",
                "no_significant_result": "Brak istotnych różnic między grupami."
            },
            "subheaders": {
                "boxplot": "Wykres pudełkowy (BoxPlot)",
                "tukey_test": "Test Tukeya – porównanie parowe"
            },
            "boxplot": {
                "x_label": "Grupa",
                "y_label": "Wartości"
            }
        },
        "dissolution_testing": {
            "title": "Porównanie profili uwalniania",
            "show_instructions": "Pokaż instrukcje",
            "dissolution_testing": "Porównanie profili uwalniania",
            "instructions": {
                "prepare_file": "Przygotuj plik Excel: pierwszy wiersz powinien zawierać nagłówki kolumn, gdzie pierwszy kolumna to czas pomiaru (\"Czas [min]\"), druga kolumna to wyniki dla produktu referencyjnego (\"Oryginał [%]\"), a kolejne kolumny to wyniki dla poszczególnych serii produktu generycznego (\"Seria 1 [%]\", \"Seria 2 [%]\"). Wartości muszą być liczbowe, a czas pomiaru powinien być taki sam dla wszystkich serii.",
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane uwalniania.",
                "select_groups": "Wybierz grupy do porównania:",
                "perform_analysis": "Oblicz współczynniki f1 i f2.",
                "view_results": "Zobacz wykresy i wyniki analizy.",
                "interpretation": "Interpretacja wyników: Współczynniki f1 i f2 określają stopień podobieństwa profilu uwalniania produktu referencyjnego i badanego. Wartość f1 bliska 0 oraz f2 powyżej 50 oznaczają wysoki stopień podobieństwa."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "select_groups": "Wybierz serie do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku.",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "warnings": {
                "need_two_groups": "Wybierz przynajmniej dwie serie do porównania."
            },
            "plot": {
                "title": "Wykres profili uwalniania",
                "x_label": "Czas (min)",
                "y_label": "Procent uwolnionej substancji"
            },
            "analysis_results": {
                "header": "Wyniki analizy",
                "f1": "Współczynnik różnicy (f1)",
                "f2": "Współczynnik podobieństwa (f2)",
                "significant_result": "Profil uznany za podobny (f2 ≥ 50).",
                "no_significant_result": "Profil uznany za różny (f2 < 50)."
            }
        }
    }, 
    "English": {
        "general": {
            "menu_title": "Menu",
            "intro": "Welcome to the Pharmstat2 application!",
            "intro_desc": "The application allows for statistical and quality data analysis in a simple and intuitive way. In the side menu, you will find modules that help you analyze data from various perspectives.",
            "choose_page": "Choose a page:",
            "upload_data": "Upload data for analysis using the built-in forms.",
            "view_results": "The analysis results (charts, tables, statistics) will appear in the main area of the page.",
            "customize_view": "You can hide or display analysis details, adjusting the view to your needs.",
            "how_to_use": "How to use the application?"
        },
        "descriptive_statistics": {
            "title": "Descriptive Statistics",
            "show_instructions": "Show instructions",
            "descriptive_stats": "Descriptive Statistics",
            "descriptive_stats_desc": "Calculating basic statistics such as mean, median, and standard deviation. This module allows for quick and easy access to fundamental information about your data, which is crucial for further analysis. Descriptive statistics are the foundation of data analysis as they enable a quick understanding of data distribution and variability.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers specifying the variable names, e.g., \"Active substance content\" or \"Humidity\". Subsequent rows should contain numerical values corresponding to these variables. Each column represents a different variable for analysis.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "select_columns": "Select the columns for which you want to calculate descriptive statistics.",
                "stats_summary": "You will receive a summary of the key statistics such as mean, median, standard deviation, and more.",
                "normality_skew_kurtosis": "Additionally, assess the normality of the distribution and obtain information on skewness and kurtosis.",
                "interpretation": "Interpretation of results: The mean represents the average value, the median indicates the center of the dataset, and the standard deviation reflects the variability of the results. High skewness may indicate asymmetry in the distribution, while high kurtosis suggests the presence of outliers."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_columns": "Select columns for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "statistics": {
                "shapiro_test": "Shapiro-Wilk p-value",
                "skewness": "Skewness",
                "kurtosis": "Kurtosis"
            }
        },
        "histogram_analysis": {
            "title": "Histogram Analysis",
            "show_instructions": "Show instructions",
            "histograms": "Histograms",
            "histograms_desc": "Creating histograms with normality assessment and skewness and kurtosis analysis. This module allows you to visualize the distribution of your data and assess whether it exhibits characteristics of a normal distribution. Histograms are a useful tool for identifying the shape of data distribution and detecting any deviations or anomalies.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers describing the data type, e.g., \"Concentration test results\". Each column should represent a single measurement series. Subsequent rows should contain numerical values without empty cells.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "select_column": "Select a column to analyze, generate a histogram, and display descriptive statistics.",
                "normality_test": "Assess the normality of the distribution and obtain information on skewness and kurtosis.",
                "interpretation": "Interpretation of results: The histogram helps assess the shape of the data distribution. A bell-shaped histogram suggests a normal distribution. Skewness may indicate an asymmetric distribution, while the width of the distribution represents data dispersion."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_column": "Select a column for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "statistics": {
                "sample_size": "Sample Size",
                "mean": "Mean",
                "std_dev": "Standard Deviation",
                "max": "Maximum",
                "min": "Minimum",
                "median": "Median",
                "rsd": "Relative Standard Deviation (RSD %)",
                "shapiro_test": "Shapiro-Wilk Test",
                "skewness": "Skewness",
                "kurtosis": "Kurtosis"
            },
            "plot": {
                "histogram_title": "Data Histogram",
                "x_label": "Values",
                "y_label": "Frequency"
            },
            "normality_results": {
                "normal_distribution": "No reason to reject the hypothesis of normal distribution.",
                "non_normal_distribution": "The data does not follow a normal distribution."
            }
        },
        "boxplot_charts": {
            "title": "BoxPlot Charts",
            "show_instructions": "Show instructions",
            "boxplot": "BoxPlot Charts",
            "boxplot_desc": "Visualizing data distribution and identifying outliers. BoxPlot charts provide a quick understanding of data distribution, showing the median, quartiles, and outliers. They are particularly useful for identifying potential measurement errors or unusual observations.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain the names of the data groups, e.g., \"Series 1\", \"Series 2\", \"Series 3\". Each column represents a different comparison group. Subsequent rows should contain numerical values assigned to the respective group.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "select_columns": "Select columns for analysis to generate BoxPlot charts.",
                "view_stats": "You will receive descriptive statistics for the selected columns.",
                "interpretation": "Interpretation of results: The box plot helps assess the median, interquartile range, and the presence of outliers. Long whiskers indicate high variability in the data, while individual points outside the whiskers suggest outliers."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx, xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 5 rows):",
                "select_columns": "Select columns for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "plot": {
                "title": "BoxPlot Charts for Selected Columns",
                "y_label": "Values"
            },
            "statistics": {
                "title": "Descriptive Statistics"
            }
        },
        "control_charts": {
            "title": "ImR Control Charts",
            "show_instructions": "Show instructions",
            "control_charts": "ImR Control Charts",
            "control_charts_desc": "Monitoring process stability using ImR control charts. Control charts allow tracking of changes in production or research processes, detecting any deviations from the norm. They are an essential tool in quality management and continuous process improvement.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is sample identifiers or series numbers, and the subsequent columns contain measurement values. If the file contains more than one column of results, the user will be able to choose which one to analyze.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "data_format": "The file should contain two columns: sample dates or IDs and numerical data.",
                "extra_columns": "If the file contains more than 2 columns, additional columns will be ignored.",
                "chart_info": "ImR charts will be generated, including the Individual Values (I) chart and the Moving Range (MR) chart.",
                "interpretation": "Interpretation of results: Control charts help monitor process stability. Points outside the control limits may indicate irregularities. Detecting trends or a sequence of values on one side of the mean may suggest systematic changes in the process."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above.",
                "error_two_columns": "The file must contain at least 2 columns (Time/ID, Value).",
                "warning_extra_columns": "The file contains extra columns:",
                "select_result_column": "Select the result column for analysis:",
                "select_result_column_help": "Choose the column containing the data you want to analyze in the control chart.",
                "using_first_two": "Only the first two columns will be used."
            },
            "chart_labels": {
                "time_series": "Time/ID",
                "values": "Value",
                "individual_values": "I (Individual Values)",
                "moving_range": "MR (Moving Range)",
                "observation": "Observation"
            },
            "analysis_results": {
                "normal_distribution_check": "Is the distribution of I values normal (α=0.05 test)?",
                "process_stable": "Is the process stable according to the rules?",
                "show_I_chart": "Show I Chart Data (Individual Values)",
                "show_MR_chart": "Show MR Chart Data (Moving Range)",
                "I_chart_data": "I Chart Data (Individual Values)",
                "MR_chart_data": "MR Chart Data (Moving Range)"
            }
        },
        "process_capability": {
            "title": "Process Capability Analysis",
            "show_instructions": "Show instructions",
            "process_capability": "Process Capability Analysis",
            "process_capability_desc": "Assessing process capability based on Cp and Cpk indices. Process capability analysis allows evaluating whether a process can meet specified quality requirements. Cp and Cpk indices help identify potential issues and areas for improvement.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain the variable names, e.g., \"Tablet diameter\" or \"Powder humidity\". Subsequent rows should contain numerical values corresponding to the variable. Each column represents a separate product attribute to be analyzed.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "set_spec_limits": "Set the lower (LSL) and upper (USL) specification limits and the target value.",
                "view_results": "You will receive a process capability analysis chart and Cp and Cpk indices.",
                "interpretation": "Interpretation of results: Cp and Cpk indices evaluate the process capability to meet specification requirements. A Cp > 1.33 suggests good process capability, while Cpk considers both variability and shift relative to the specification target."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_column": "Select a column for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "spec_settings": {
                "target": "Target Value",
                "lsl": "Lower Specification Limit (LSL)",
                "usl": "Upper Specification Limit (USL)"
            },
            "plot": {
                "title": "Process Capability Analysis",
                "x_label": "Values",
                "y_label": ""
            },
            "results": {
                "header": "Analysis Results",
                "cp": "Cp",
                "cpk": "Cpk",
                "sample_size": "Sample Size",
                "sample_mean": "Sample Mean",
                "sample_std": "Standard Deviation",
                "sample_max": "Maximum",
                "sample_min": "Minimum",
                "sample_median": "Median",
                "pct_below_lsl": "Percentage of Samples Below LSL",
                "pct_above_usl": "Percentage of Samples Above USL"
            }
        },
        "stability_regression": {
            "title": "Stability Data Analysis",
            "show_instructions": "Show instructions",
            "stability_regression": "Stability Regression",
            "stability_regression_desc": "Regression analysis for stability data. Stability regression enables predicting product shelf life based on long-term stability study results. This is crucial in the pharmaceutical and food industries, where product stability directly impacts safety and efficacy.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the name of the parameter under study (e.g., \"API content\", \"Humidity\"), the second column is the time values (e.g., \"Time [months]\"), the third column is the lower specification limit (\"LSL\"), the fourth column is the upper specification limit (\"USL\"), and the subsequent columns contain the measurement results for individual product series. Values must be numerical, and cells should remain blank if data is missing.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing stability data.",
                "display_series": "The selected series will be displayed on the chart along with regression lines.",
                "view_regression_results": "Below the chart, you will find a table with regression parameters for the selected series.",
                "interpretation": "Interpretation of results: Linear regression helps determine the trend of parameter changes over time. An R² value close to 1 indicates a good model fit. The slope of the regression line shows whether the parameter values increase, decrease, or remain stable."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_series": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "plot": {
                "data": "data",
                "regression": "regression",
                "spec_limit": "Specification Limit",
                "x_label": "Time (months)",
                "title": "Stability Analysis"
            },
            "regression_results": {
                "header": "Regression Analysis Results for Selected Series",
                "series": "Series",
                "slope": "Slope",
                "intercept": "Intercept",
                "r_value": "Correlation Coefficient (r)",
                "p_value": "p-value",
                "std_err": "Standard Deviation"
            }
        },
        "temp_humidity_analysis": {
            "title": "Temperature and Humidity Analysis",
            "show_instructions": "Show instructions",
            "temp_humidity": "Temperature and Humidity Analysis",
            "temp_humidity_desc": "Environmental data analysis and identification of limit exceedances. This module allows monitoring environmental conditions, such as temperature and humidity, and detecting any exceedances of established limits. It is particularly important in production and storage processes where environmental conditions can affect product quality and durability.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the date or timestamp (\"Data\"), the second column is temperature values (\"Temperature [°C]\"), and the third column is humidity values (\"Humidity [%]\"). All values must be numerical, and the date format must be consistent throughout the file.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing temperature and humidity data.",
                "set_limits": "Set temperature and humidity limits using sliders.",
                "view_results": "Browse charts and the list of limit exceedances.",
                "interpretation": "Interpretation of results: Temperature and humidity charts help monitor environmental conditions. Stable values indicate good control of storage conditions. Significant fluctuations may suggest issues with maintaining stability conditions."
            },
            "settings": {
                "temp_lower": "Lower Temperature Limit (°C)",
                "temp_upper": "Upper Temperature Limit (°C)",
                "hum_lower": "Lower Humidity Limit (%)",
                "hum_upper": "Upper Humidity Limit (%)"
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "data_preview": "Data preview (first 10 rows):",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "statistics": {
                "temp_stats": "Temperature Statistics",
                "hum_stats": "Humidity Statistics",
                "mean": "Mean",
                "min": "Minimum",
                "max": "Maximum",
                "rsd": "Relative Standard Deviation (RSD %)"
            },
            "thresholds": {
                "crossings": "Limit Exceedances",
                "no_crossings": "No temperature/humidity limit exceedances.",
                "time": "Time",
                "temperature": "Temperature",
                "humidity": "Humidity"
            },
            "plot": {
                "temp": "Temperature",
                "hum": "Humidity",
                "temp_lower_limit": "Lower Temperature Limit",
                "temp_upper_limit": "Upper Temperature Limit",
                "hum_lower_limit": "Lower Humidity Limit",
                "hum_upper_limit": "Upper Humidity Limit",
                "x_label": "Time",
                "y_label": "Value",
                "title": "Temperature and Humidity"
            }
        },
        "pqr_module": {
            "title": "PQR Module",
            "show_instructions": "Show instructions",
            "pqr_module": "PQR Module",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is sample identifiers or series numbers (\"Series\"), and the subsequent columns are measurement values for various quality parameters (\"API content\", \"Humidity\"). If the file contains more than one data column, the user will be able to choose which one to analyze. The user can also provide lower and upper specification limits.",
                "header": "Instructions",
                "upload_file": "Upload data file",
                "select_series": "Select series for analysis",
                "input_spec_limits": "Enter upper and lower specification limits",
                "view_charts": "View charts",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Choose file",
                "error_two_columns": "The file must contain at least two columns",
                "select_result_column": "Select result column",
                "select_result_column_help": "Choose the column containing data for analysis",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview",
                "error_no_numeric_data": "No numeric data available for analysis",
                "error_processing_file": "Error processing file",
                "no_file_uploaded": "No file uploaded"
            },
            "chart_labels": {
                "time_series": "Series Identifier",
                "values": "Values",
                "observation": "Observation",
                "individual_values": "Individual Values",
                "moving_range": "Moving Range",
                "frequency": "Frequency",
                "histogram_with_spec_limits": "Histogram with Specification Limits",
                "control_chart_with_spec_limits": "Control Chart with Specification Limits"
            },
            "subheaders": {
                "imr_chart": "ImR Control Chart",
                "cpk_analysis": "Process Capability Analysis Cpk",
                "spec_limits_comparison": "Comparison of Results with Specification Limits"
            },
            "spec_limits": {
                "usl": "Upper Specification Limit (USL)",
                "lsl": "Lower Specification Limit (LSL)"
            },
            "warnings": {
                "spec_limits_equal": "Upper and lower specification limits are equal. Please enter valid values."
            },
            "cpk_results": {
                "mean": "Mean",
                "std_dev": "Standard Deviation",
                "cpk": "Cpk Index"
            }
        },
        "anova_module": {
            "title": "Analysis of Variance (ANOVA)",
            "show_instructions": "Show instructions",
            "anova_module": "Analysis of Variance (ANOVA)",
            "instructions": {
                "prepare_file": "Provide an Excel file as required by the module.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing data for different groups.",
                "select_groups": "Select groups for analysis.",
                "perform_anova": "Perform an analysis of variance (ANOVA) on the selected groups.",
                "view_results": "View the results of the ANOVA test and Tukey test.",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Select an Excel file (xlsx or xls):",
                "show_data_preview": "Show preview of uploaded data",
                "data_preview": "Data preview (first 10 rows):",
                "select_groups": "Select groups for analysis:",
                "error_two_columns": "The file must contain at least 2 columns with data.",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "warnings": {
                "need_two_groups": "Select at least two groups for analysis."
            },
            "anova_results": {
                "header": "ANOVA (Analysis of Variance) Results",
                "statistic": "F-Statistic",
                "p_value": "P-Value",
                "significant_result": "There are statistically significant differences between groups.",
                "no_significant_result": "No significant differences between groups."
            },
            "subheaders": {
                "boxplot": "BoxPlot Chart",
                "tukey_test": "Tukey Test – Pairwise Comparison"
            },
            "boxplot": {
                "x_label": "Group",
                "y_label": "Values"
            }
        },
        "dissolution_testing": {
            "title": "Dissolution Profile Comparison",
            "show_instructions": "Show instructions",
            "dissolution_testing": "Dissolution Profile Comparison",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the measurement time (\"Time [min]\"), the second column is the results for the reference product (\"Original [%]\"), and the subsequent columns are the results for individual series of the generic product (\"Series 1 [%]\", \"Series 2 [%]\"). Values must be numerical, and the measurement time should be the same for all series.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing dissolution data.",
                "select_groups": "Select groups for comparison:",
                "perform_analysis": "Calculate f1 and f2 similarity factors.",
                "view_results": "View charts and analysis results.",
                "interpretation": "Interpretation of results: The f1 and f2 factors assess the similarity of dissolution profiles between the reference and test product. An f1 value close to 0 and an f2 value above 50 indicate a high degree of similarity."
            },
            "file_handling": {
                "choose_file": "Select an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_groups": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file.",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "warnings": {
                "need_two_groups": "Select at least two series for comparison."
            },
            "plot": {
                "title": "Dissolution Profile Chart",
                "x_label": "Time (min)",
                "y_label": "Percentage of drug released"
            },
            "analysis_results": {
                "header": "Analysis Results",
                "f1": "Difference Factor (f1)",
                "f2": "Similarity Factor (f2)",
                "significant_result": "Profile considered similar (f2 ≥ 50).",
                "no_significant_result": "Profile considered different (f2 < 50)."
            }
        }
    },
    "Russian": {
        "general": {
            "menu_title": "Меню",
            "intro": "Добро пожаловать в приложение Pharmstat2!",
            "intro_desc": "Приложение позволяет просто и интуитивно проводить анализ статистических и качественных данных. В боковом меню вы найдёте модули, которые помогут вам анализировать данные с различных позиций.",
            "choose_page": "Выберите страницу:",
            "upload_data": "Загрузите данные для анализа с помощью встроенных форм.",
            "view_results": "Результаты анализа (графики, таблицы, статистика) появятся в главной области страницы.",
            "customize_view": "Вы можете скрывать или отображать детали анализа, настраивая вид согласно вашим потребностям.",
            "how_to_use": "Как использовать приложение?"
        },
        "descriptive_statistics": {
            "title": "Описательная статистика",
            "show_instructions": "Показать инструкции",
            "descriptive_stats": "Описательная статистика",
            "descriptive_stats_desc": "Вычисление основных статистических показателей, таких как среднее значение, медиана, стандартное отклонение. Этот модуль позволяет быстро и легко получить основную информацию о ваших данных, что является ключевым для дальнейшего анализа. Описательная статистика является основой анализа данных, так как позволяет быстро понять распределение и изменчивость данных.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать заголовки столбцов, определяющие названия переменных, например, \"Содержание действующего вещества\" или \"Влажность\". Последующие строки должны содержать числовые значения, соответствующие этим переменным. Каждый столбец представляет собой отдельную переменную для анализа.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "select_columns": "Выберите столбцы для расчета описательной статистики.",
                "stats_summary": "Вы получите сводку основных статистических показателей, таких как среднее значение, медиана, стандартное отклонение и другие.",
                "normality_skew_kurtosis": "Дополнительно вы сможете оценить нормальность распределения и получить информацию об асимметрии и эксцессе.",
                "interpretation": "Интерпретация результатов: Среднее значение показывает средний показатель, медиана указывает центр набора данных, а стандартное отклонение отражает изменчивость результатов. Высокая асимметрия может указывать на несбалансированность распределения, а высокая эксцессия – на наличие выбросов."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx или xls):",
                "show_data_preview": "Показать предварительный просмотр загруженных данных",
                "data_preview": "Предварительный просмотр загруженных данных (первые 10 строк):",
                "select_columns": "Выберите столбцы для анализа:",
                "error_processing_file": "Произошла ошибка при анализе файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
            },
            "statistics": {
                "shapiro_test": "Шапиро-Уилка p-значение",
                "skewness": "Асимметрия",
                "kurtosis": "Эксцесс"
            }
        },
        "histogram_analysis": {
            "title": "Анализ гистограмм",
            "show_instructions": "Показать инструкции",
            "histograms": "Гистограммы",
            "histograms_desc": "Создание гистограмм с оценкой нормальности распределения и анализом асимметрии и эксцесса. Этот модуль позволяет визуализировать распределение ваших данных и оценить, имеют ли они характеристики нормального распределения. Гистограммы являются полезным инструментом для идентификации формы распределения данных и выявления любых отклонений или аномалий.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать заголовки столбцов, описывающие тип данных, например, \"Результаты измерения концентрации\". Каждый столбец должен представлять отдельную серию измерений. Последующие строки должны содержать числовые значения без пустых ячеек.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "select_column": "Выберите столбец для анализа, чтобы создать гистограмму и отобразить описательную статистику.",
                "normality_test": "Оцените нормальность распределения и получите информацию об асимметрии и эксцессе.",
                "interpretation": "Интерпретация результатов: Гистограмма помогает оценить форму распределения данных. Если гистограмма имеет колоколообразную форму, это указывает на нормальное распределение. Асимметрия может свидетельствовать о смещении распределения, а ширина – о разбросе данных."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx или xls):",
                "show_data_preview": "Показать предварительный просмотр данных",
                "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                "select_column": "Выберите столбец для анализа:",
                "error_processing_file": "Произошла ошибка при анализе файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
            },
            "statistics": {
                "sample_size": "Количество образцов",
                "mean": "Среднее значение",
                "std_dev": "Стандартное отклонение",
                "max": "Максимум",
                "min": "Минимум",
                "median": "Медиана",
                "rsd": "Коэффициент вариации (RSD %)",
                "shapiro_test": "Тест Шапиро-Уилка",
                "skewness": "Асимметрия",
                "kurtosis": "Эксцесс"
            },
            "plot": {
                "histogram_title": "Гистограмма данных",
                "x_label": "Значения",
                "y_label": "Частота"
            },
            "normality_results": {
                "normal_distribution": "Нет оснований для отклонения гипотезы о нормальности распределения.",
                "non_normal_distribution": "Данные не соответствуют нормальному распределению."
            }
        },
        "boxplot_charts": {
            "title": "Ящичные диаграммы (BoxPlot)",
            "show_instructions": "Показать инструкции",
            "boxplot": "Ящичные диаграммы (BoxPlot)",
            "boxplot_desc": "Визуализация распределения данных и идентификация выбросов. Ящичные диаграммы обеспечивают быстрое понимание распределения данных, показывая медиану, квартили и выбросы. Они особенно полезны для выявления потенциальных ошибок измерения или необычных наблюдений.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать названия групп данных, например, \"Серия 1\", \"Серия 2\", \"Серия 3\". Каждый столбец представляет собой отдельную группу для сравнения. Последующие строки должны содержать числовые значения, соответствующие каждой группе.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "select_columns": "Выберите столбцы для анализа, чтобы создать ящичные диаграммы.",
                "view_stats": "Вы получите описательную статистику для выбранных столбцов.",
                "interpretation": "Интерпретация результатов: Ящичная диаграмма позволяет оценить медиану, межквартильный размах и наличие выбросов. Длинные «усы» могут указывать на высокую изменчивость данных, a отдельные точки за пределами усов – на выбросы."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx, xls):",
                "show_data_preview": "Показать предварительный просмотр данных",
                "data_preview": "Предварительный просмотр данных (первые 5 строк):",
                "select_columns": "Выберите столбцы для анализа:",
                "error_processing_file": "Произошла ошибка при анализе файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
            },
            "plot": {
                "title": "Ящичные диаграммы для выбранных столбцов",
                "y_label": "Значения"
            },
            "statistics": {
                "title": "Описательная статистика"
            }
        },
        "control_charts": {
            "title": "Контрольные карты ImR",
            "show_instructions": "Показать инструкции",
            "control_charts": "Контрольные карты ImR",
            "control_charts_desc": "Мониторинг стабильности процессов с использованием контрольных карт ImR. Контрольные карты позволяют отслеживать изменения в производственных или исследовательских процессах, выявляя любые отклонения от нормы. Они являются неотъемлемым инструментом в управлении качеством и непрерывном улучшении процессов.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать заголовки столбцов, где первый столбец – это идентификаторы образцов или номера серий, а последующие столбцы содержат измеренные значения. Если файл содержит более одного столбца с результатами, пользователь сможет выбрать, какой анализировать.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "data_format": "Файл должен содержать два столбца: даты или идентификаторы образцов и численные данные.",
                "extra_columns": "Если файл содержит более двух столбцов, дополнительные столбцы будут проигнорированы.",
                "chart_info": "Будут сгенерированы графики ImR, включая график индивидуальных значений (I) и скользящего диапазона (MR).",
                "interpretation": "Интерпретация результатов: Контрольные карты помогают отслеживать стабильность процесса. Точки за пределами контрольных границ могут свидетельствовать о нарушениях. Обнаружение трендов или последовательности значений с одной стороны от среднего может указывать на систематические изменения в процессе."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx или xls):",
                "show_data_preview": "Показать предварительный просмотр данных",
                "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                "error_processing_file": "Ошибка при обработке файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel.",
                "error_two_columns": "Файл должен содержать как минимум 2 столбца (Время/ID, Значение).",
                "warning_extra_columns": "Файл содержит дополнительные столбцы:",
                "select_result_column": "Выберите столбец с результатами для анализа:",
                "select_result_column_help": "Выберите столбец, содержащий данные, которые вы хотите проанализировать на контрольной карте.",
                "using_first_two": "Будут использованы только первые два столбца."
            },
            "chart_labels": {
                "time_series": "Время/ID",
                "values": "Значение",
                "individual_values": "I (Индивидуальные значения)",
                "moving_range": "MR (Скользящий диапазон)",
                "observation": "Наблюдение"
            },
            "analysis_results": {
                "normal_distribution_check": "Распределение значений I является нормальным (тест α=0.05)?",
                "process_stable": "Процесс стабилен в соответствии с правилами?",
                "show_I_chart": "Показать данные графика I (индивидуальные значения)",
                "show_MR_chart": "Показать данные графика MR (скользящий диапазон)",
                "I_chart_data": "Данные графика I (индивидуальные значения)",
                "MR_chart_data": "Данные графика MR (скользящий диапазон)"
            }
        },
        "process_capability": {
            "title": "Process Capability Analysis",
            "show_instructions": "Show instructions",
            "process_capability": "Process Capability Analysis",
            "process_capability_desc": "Assessing process capability based on Cp and Cpk indices. Process capability analysis allows evaluating whether a process can meet specified quality requirements. Cp and Cpk indices help identify potential issues and areas for improvement.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain the variable names, e.g., \"Tablet diameter\" or \"Powder humidity\". Subsequent rows should contain numerical values corresponding to the variable. Each column represents a separate product attribute to be analyzed.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "set_spec_limits": "Set the lower (LSL) and upper (USL) specification limits and the target value.",
                "view_results": "You will receive a process capability analysis chart and Cp and Cpk indices.",
                "interpretation": "Interpretation of results: Cp and Cpk indices evaluate the process capability to meet specification requirements. A Cp > 1.33 suggests good process capability, while Cpk considers both variability and shift relative to the specification target."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_column": "Select a column for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "spec_settings": {
                "target": "Target Value",
                "lsl": "Lower Specification Limit (LSL)",
                "usl": "Upper Specification Limit (USL)"
            },
            "plot": {
                "title": "Process Capability Analysis",
                "x_label": "Values",
                "y_label": ""
            },
            "results": {
                "header": "Analysis Results",
                "cp": "Cp",
                "cpk": "Cpk",
                "sample_size": "Sample Size",
                "sample_mean": "Sample Mean",
                "sample_std": "Standard Deviation",
                "sample_max": "Maximum",
                "sample_min": "Minimum",
                "sample_median": "Median",
                "pct_below_lsl": "Percentage of Samples Below LSL",
                "pct_above_usl": "Percentage of Samples Above USL"
            }
        },
        "stability_regression": {
            "title": "Stability Data Analysis",
            "show_instructions": "Show instructions",
            "stability_regression": "Stability Regression",
            "stability_regression_desc": "Regression analysis for stability data. Stability regression enables predicting product shelf life based on long-term stability study results. This is crucial in the pharmaceutical and food industries, where product stability directly impacts safety and efficacy.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the name of the parameter under study (e.g., \"API content\", \"Humidity\"), the second column is the time values (e.g., \"Time [months]\"), the third column is the lower specification limit (\"LSL\"), the fourth column is the upper specification limit (\"USL\"), and the subsequent columns contain the measurement results for individual product series. Values must be numerical, and cells should remain blank if data is missing.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing stability data.",
                "display_series": "The selected series will be displayed on the chart along with regression lines.",
                "view_regression_results": "Below the chart, you will find a table with regression parameters for the selected series.",
                "interpretation": "Interpretation of results: Linear regression helps determine the trend of parameter changes over time. An R² value close to 1 indicates a good model fit. The slope of the regression line shows whether the parameter values increase, decrease, or remain stable."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_series": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "plot": {
                "data": "data",
                "regression": "regression",
                "spec_limit": "Specification Limit",
                "x_label": "Time (months)",
                "title": "Stability Analysis"
            },
            "regression_results": {
                "header": "Regression Analysis Results for Selected Series",
                "series": "Series",
                "slope": "Slope",
                "intercept": "Intercept",
                "r_value": "Correlation Coefficient (r)",
                "p_value": "p-value",
                "std_err": "Standard Deviation"
            }
        },
        "temp_humidity_analysis": {
            "title": "Temperature and Humidity Analysis",
            "show_instructions": "Show instructions",
            "temp_humidity": "Temperature and Humidity Analysis",
            "temp_humidity_desc": "Environmental data analysis and identification of limit exceedances. This module allows monitoring environmental conditions, such as temperature and humidity, and detecting any exceedances of established limits. It is particularly important in production and storage processes where environmental conditions can affect product quality and durability.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the date or timestamp (\"Data\"), the second column is temperature values (\"Temperature [°C]\"), and the third column is humidity values (\"Humidity [%]\"). All values must be numerical, and the date format must be consistent throughout the file.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing temperature and humidity data.",
                "set_limits": "Set temperature and humidity limits using sliders.",
                "view_results": "Browse charts and the list of limit exceedances.",
                "interpretation": "Interpretation of results: Temperature and humidity charts help monitor environmental conditions. Stable values indicate good control of storage conditions. Significant fluctuations may suggest issues with maintaining stability conditions."
            },
            "settings": {
                "temp_lower": "Lower Temperature Limit (°C)",
                "temp_upper": "Upper Temperature Limit (°C)",
                "hum_lower": "Lower Humidity Limit (%)",
                "hum_upper": "Upper Humidity Limit (%)"
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "data_preview": "Data preview (first 10 rows):",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "statistics": {
                "temp_stats": "Temperature Statistics",
                "hum_stats": "Humidity Statistics",
                "mean": "Mean",
                "min": "Minimum",
                "max": "Maximum",
                "rsd": "Relative Standard Deviation (RSD %)"
            },
            "thresholds": {
                "crossings": "Limit Exceedances",
                "no_crossings": "No temperature/humidity limit exceedances.",
                "time": "Time",
                "temperature": "Temperature",
                "humidity": "Humidity"
            },
            "plot": {
                "temp": "Temperature",
                "hum": "Humidity",
                "temp_lower_limit": "Lower Temperature Limit",
                "temp_upper_limit": "Upper Temperature Limit",
                "hum_lower_limit": "Lower Humidity Limit",
                "hum_upper_limit": "Upper Humidity Limit",
                "x_label": "Time",
                "y_label": "Value",
                "title": "Temperature and Humidity"
            }
        },
        "pqr_module": {
            "title": "PQR Module",
            "show_instructions": "Show instructions",
            "pqr_module": "PQR Module",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is sample identifiers or series numbers (\"Series\"), and the subsequent columns are measurement values for various quality parameters (\"API content\", \"Humidity\"). If the file contains more than one data column, the user will be able to choose which one to analyze. The user can also provide lower and upper specification limits.",
                "header": "Instructions",
                "upload_file": "Upload data file",
                "select_series": "Select series for analysis",
                "input_spec_limits": "Enter upper and lower specification limits",
                "view_charts": "View charts",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Choose file",
                "error_two_columns": "The file must contain at least two columns",
                "select_result_column": "Select result column",
                "select_result_column_help": "Choose the column containing data for analysis",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview",
                "error_no_numeric_data": "No numeric data available for analysis",
                "error_processing_file": "Error processing file",
                "no_file_uploaded": "No file uploaded"
            },
            "chart_labels": {
                "time_series": "Series Identifier",
                "values": "Values",
                "observation": "Observation",
                "individual_values": "Individual Values",
                "moving_range": "Moving Range",
                "frequency": "Frequency",
                "histogram_with_spec_limits": "Histogram with Specification Limits",
                "control_chart_with_spec_limits": "Control Chart with Specification Limits"
            },
            "subheaders": {
                "imr_chart": "ImR Control Chart",
                "cpk_analysis": "Process Capability Analysis Cpk",
                "spec_limits_comparison": "Comparison of Results with Specification Limits"
            },
            "spec_limits": {
                "usl": "Upper Specification Limit (USL)",
                "lsl": "Lower Specification Limit (LSL)"
            },
            "warnings": {
                "spec_limits_equal": "Upper and lower specification limits are equal. Please enter valid values."
            },
            "cpk_results": {
                "mean": "Mean",
                "std_dev": "Standard Deviation",
                "cpk": "Cpk Index"
            }
        },
        "anova_module": {
            "title": "Analysis of Variance (ANOVA)",
            "show_instructions": "Show instructions",
            "anova_module": "Analysis of Variance (ANOVA)",
            "instructions": {
                "prepare_file": "Provide an Excel file as required by the module.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing data for different groups.",
                "select_groups": "Select groups for analysis.",
                "perform_anova": "Perform an analysis of variance (ANOVA) on the selected groups.",
                "view_results": "View the results of the ANOVA test and Tukey test.",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Select an Excel file (xlsx or xls):",
                "show_data_preview": "Show preview of uploaded data",
                "data_preview": "Data preview (first 10 rows):",
                "select_groups": "Select groups for analysis:",
                "error_two_columns": "The file must contain at least 2 columns with data.",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "warnings": {
                "need_two_groups": "Select at least two groups for analysis."
            },
            "anova_results": {
                "header": "ANOVA (Analysis of Variance) Results",
                "statistic": "F-Statistic",
                "p_value": "P-Value",
                "significant_result": "There are statistically significant differences between groups.",
                "no_significant_result": "No significant differences between groups."
            },
            "subheaders": {
                "boxplot": "BoxPlot Chart",
                "tukey_test": "Tukey Test – Pairwise Comparison"
            },
            "boxplot": {
                "x_label": "Group",
                "y_label": "Values"
            }
        },
        "dissolution_testing": {
            "title": "Dissolution Profile Comparison",
            "show_instructions": "Show instructions",
            "dissolution_testing": "Dissolution Profile Comparison",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the measurement time (\"Time [min]\"), the second column is the results for the reference product (\"Original [%]\"), and the subsequent columns are the results for individual series of the generic product (\"Series 1 [%]\", \"Series 2 [%]\"). Values must be numerical, and the measurement time should be the same for all series.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing dissolution data.",
                "select_groups": "Select groups for comparison:",
                "perform_analysis": "Calculate f1 and f2 similarity factors.",
                "view_results": "View charts and analysis results.",
                "interpretation": "Interpretation of results: The f1 and f2 factors assess the similarity of dissolution profiles between the reference and test product. An f1 value close to 0 and f2 above 50 indicate a high degree of similarity."
            },
            "file_handling": {
                "choose_file": "Select an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_groups": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file.",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "warnings": {
                "need_two_groups": "Select at least two series for comparison."
            },
            "plot": {
                "title": "Dissolution Profile Chart",
                "x_label": "Time (min)",
                "y_label": "Percentage of drug released"
            },
            "analysis_results": {
                "header": "Analysis Results",
                "f1": "Difference Factor (f1)",
                "f2": "Similarity Factor (f2)",
                "significant_result": "Profile considered similar (f2 ≥ 50).",
                "no_significant_result": "Profile considered different (f2 < 50)."
            }
        }
    },
    "Russian": {
        "general": {
            "menu_title": "Меню",
            "intro": "Добро пожаловать в приложение Pharmstat2!",
            "intro_desc": "Приложение позволяет просто и интуитивно проводить анализ статистических и качественных данных. В боковом меню вы найдёте модули, которые помогут вам анализировать данные с различных позиций.",
            "choose_page": "Выберите страницу:",
            "upload_data": "Загрузите данные для анализа с помощью встроенных форм.",
            "view_results": "Результаты анализа (графики, таблицы, статистика) появятся в главной области страницы.",
            "customize_view": "Вы можете скрывать или отображать детали анализа, настраивая вид согласно вашим потребностям.",
            "how_to_use": "Как использовать приложение?"
        },
        "descriptive_statistics": {
            "title": "Описательная статистика",
            "show_instructions": "Показать инструкции",
            "descriptive_stats": "Описательная статистика",
            "descriptive_stats_desc": "Вычисление основных статистических показателей, таких как среднее значение, медиана, стандартное отклонение. Этот модуль позволяет быстро и легко получить основную информацию о ваших данных, что является ключевым для дальнейшего анализа. Описательная статистика является основой анализа данных, так как позволяет быстро понять распределение и изменчивость данных.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать заголовки столбцов, определяющие названия переменных, например, \"Содержание действующего вещества\" или \"Влажность\". Последующие строки должны содержать числовые значения, соответствующие этим переменным. Каждый столбец представляет собой отдельную переменную для анализа.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "select_columns": "Выберите столбцы для расчета описательной статистики.",
                "stats_summary": "Вы получите сводку основных статистических показателей, таких как среднее значение, медиана, стандартное отклонение и другие.",
                "normality_skew_kurtosis": "Дополнительно вы сможете оценить нормальность распределения и получить информацию об асимметрии и эксцессе.",
                "interpretation": "Интерпретация результатов: Среднее значение показывает средний показатель, медиана указывает центр набора данных, а стандартное отклонение отражает изменчивость результатов. Высокая асимметрия может указывать на несбалансированность распределения, а высокая эксцессия – на наличие выбросов."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx или xls):",
                "show_data_preview": "Показать предварительный просмотр загруженных данных",
                "data_preview": "Предварительный просмотр загруженных данных (первые 10 строк):",
                "select_columns": "Выберите столбцы для анализа:",
                "error_processing_file": "Произошла ошибка при анализе файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
            },
            "statistics": {
                "shapiro_test": "Шапиро-Уилка p-значение",
                "skewness": "Асимметрия",
                "kurtosis": "Эксцесс"
            }
        },
        "histogram_analysis": {
            "title": "Анализ гистограмм",
            "show_instructions": "Показать инструкции",
            "histograms": "Гистограммы",
            "histograms_desc": "Создание гистограмм с оценкой нормальности распределения и анализом асимметрии и эксцесса. Этот модуль позволяет визуализировать распределение ваших данных и оценить, имеют ли они характеристики нормального распределения. Гистограммы являются полезным инструментом для идентификации формы распределения данных и выявления любых отклонений или аномалий.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать заголовки столбцов, описывающие тип данных, например, \"Результаты измерения концентрации\". Каждый столбец должен представлять отдельную серию измерений. Последующие строки должны содержать числовые значения без пустых ячеек.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "select_column": "Выберите столбец для анализа, чтобы создать гистограмму и отобразить описательную статистику.",
                "normality_test": "Оцените нормальность распределения и получите информацию об асимметрии и эксцессе.",
                "interpretation": "Интерпретация результатов: Гистограмма помогает оценить форму распределения данных. Если гистограмма имеет колоколообразную форму, это указывает на нормальное распределение. Асимметрия может свидетельствовать о смещении распределения, а ширина – о разбросе данных."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx или xls):",
                "show_data_preview": "Показать предварительный просмотр данных",
                "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                "select_column": "Выберите столбец для анализа:",
                "error_processing_file": "Произошла ошибка при анализе файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
            },
            "statistics": {
                "sample_size": "Количество образцов",
                "mean": "Среднее значение",
                "std_dev": "Стандартное отклонение",
                "max": "Максимум",
                "min": "Минимум",
                "median": "Медиана",
                "rsd": "Коэффициент вариации (RSD %)",
                "shapiro_test": "Тест Шапиро-Уилка",
                "skewness": "Асимметрия",
                "kurtosis": "Эксцесс"
            },
            "plot": {
                "histogram_title": "Гистограмма данных",
                "x_label": "Значения",
                "y_label": "Частота"
            },
            "normality_results": {
                "normal_distribution": "Нет оснований для отклонения гипотезы о нормальности распределения.",
                "non_normal_distribution": "Данные не соответствуют нормальному распределению."
            }
        },
        "boxplot_charts": {
            "title": "Ящичные диаграммы (BoxPlot)",
            "show_instructions": "Показать инструкции",
            "boxplot": "Ящичные диаграммы (BoxPlot)",
            "boxplot_desc": "Визуализация распределения данных и идентификация выбросов. Ящичные диаграммы обеспечивают быстрое понимание распределения данных, показывая медиану, квартели и выбросы. Они особенно полезны для выявления потенциальных ошибок измерения или необычных наблюдений.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать названия групп данных, например, \"Серия 1\", \"Серия 2\", \"Серия 3\". Каждый столбец представляет собой отдельную группу для сравнения. Последующие строки должны содержать числовые значения, соответствующие каждой группе.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "select_columns": "Выберите столбцы для анализа, чтобы создать ящичные диаграммы.",
                "view_stats": "Вы получите описательную статистику для выбранных столбцов.",
                "interpretation": "Интерпретация результатов: Ящичная диаграмма позволяет оценить медиану, межквартильный размах и наличие выбросов. Длинные «усы» могут указывать на высокую изменчивость данных, а отдельные точки за пределами усов – на выбросы."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx, xls):",
                "show_data_preview": "Показать предварительный просмотр данных",
                "data_preview": "Предварительный просмотр данных (первые 5 строк):",
                "select_columns": "Выберите столбцы для анализа:",
                "error_processing_file": "Произошла ошибка при анализе файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
            },
            "plot": {
                "title": "Ящичные диаграммы для выбранных столбцов",
                "y_label": "Значения"
            },
            "statistics": {
                "title": "Описательная статистика"
            }
        },
        "control_charts": {
            "title": "Контрольные карты ImR",
            "show_instructions": "Показать инструкции",
            "control_charts": "Контрольные карты ImR",
            "control_charts_desc": "Мониторинг стабильности процессов с использованием контрольных карт ImR. Контрольные карты позволяют отслеживать изменения в производственных или исследовательских процессах, выявляя любые отклонения от нормы. Они являются неотъемлемым инструментом в управлении качеством и непрерывном улучшении процессов.",
            "instructions": {
                "prepare_file": "Подготовьте файл Excel: первая строка должна содержать заголовки столбцов, где первый столбец — это идентификаторы образцов или номера серий, а последующие столбцы содержат измеренные значения. Если файл содержит более одного столбца с результатами, пользователь сможет выбрать, какой анализировать.",
                "header": "Инструкции",
                "upload_file": "Загрузите файл Excel с данными измерений.",
                "data_format": "Файл должен содержать два столбца: даты или идентификаторы образцов и численные данные.",
                "extra_columns": "Если файл содержит более двух столбцов, дополнительные столбцы будут проигнорированы.",
                "chart_info": "Будут сгенерированы графики ImR, включая график индивидуальных значений (I) и скользящего диапазона (MR).",
                "interpretation": "Интерпретация результатов: Контрольные карты помогают отслеживать стабильность процесса. Точки за пределами контрольных границ могут свидетельствовать о нарушениях. Обнаружение трендов или последовательности значений с одной стороны от среднего может указывать на систематические изменения в процессе."
            },
            "file_handling": {
                "choose_file": "Выберите файл Excel (xlsx или xls):",
                "show_data_preview": "Показать предварительный просмотр данных",
                "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                "error_processing_file": "Ошибка при обработке файла",
                "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel.",
                "error_two_columns": "Файл должен содержать как минимум 2 столбца (Время/ID, Значение).",
                "warning_extra_columns": "Файл содержит дополнительные столбцы:",
                "select_result_column": "Выберите столбец с результатами для анализа:",
                "select_result_column_help": "Выберите столбец, содержащий данные, которые вы хотите проанализировать на контрольной карте.",
                "using_first_two": "Будут использованы только первые два столбца."
            },
            "chart_labels": {
                "time_series": "Время/ID",
                "values": "Значение",
                "individual_values": "I (Индивидуальные значения)",
                "moving_range": "MR (Скользящий диапазон)",
                "observation": "Наблюдение"
            },
            "analysis_results": {
                "normal_distribution_check": "Распределение значений I является нормальным (тест α=0.05)?",
                "process_stable": "Процесс стабилен в соответствии с правилами?",
                "show_I_chart": "Показать данные графика I (индивидуальные значения)",
                "show_MR_chart": "Показать данные графика MR (скользящий диапазон)",
                "I_chart_data": "Данные графика I (индивидуальные значения)",
                "MR_chart_data": "Данные графика MR (скользящий диапазон)"
            }
        },
        "process_capability": {
            "title": "Process Capability Analysis",
            "show_instructions": "Show instructions",
            "process_capability": "Process Capability Analysis",
            "process_capability_desc": "Assessing process capability based on Cp and Cpk indices. Process capability analysis allows evaluating whether a process can meet specified quality requirements. Cp and Cpk indices help identify potential issues and areas for improvement.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain the variable names, e.g., \"Tablet diameter\" or \"Powder humidity\". Subsequent rows should contain numerical values corresponding to the variable. Each column represents a separate product attribute to be analyzed.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "set_spec_limits": "Set the lower (LSL) and upper (USL) specification limits and the target value.",
                "view_results": "You will receive a process capability analysis chart and Cp and Cpk indices.",
                "interpretation": "Interpretation of results: Cp and Cpk indices evaluate the process capability to meet specification requirements. A Cp > 1.33 suggests good process capability, while Cpk considers both variability and shift relative to the specification target."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_column": "Select a column for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "spec_settings": {
                "target": "Target Value",
                "lsl": "Lower Specification Limit (LSL)",
                "usl": "Upper Specification Limit (USL)"
            },
            "plot": {
                "title": "Process Capability Analysis",
                "x_label": "Values",
                "y_label": ""
            },
            "results": {
                "header": "Analysis Results",
                "cp": "Cp",
                "cpk": "Cpk",
                "sample_size": "Sample Size",
                "sample_mean": "Sample Mean",
                "sample_std": "Standard Deviation",
                "sample_max": "Maximum",
                "sample_min": "Minimum",
                "sample_median": "Median",
                "pct_below_lsl": "Percentage of Samples Below LSL",
                "pct_above_usl": "Percentage of Samples Above USL"
            }
        },
        "stability_regression": {
            "title": "Stability Data Analysis",
            "show_instructions": "Show instructions",
            "stability_regression": "Stability Regression",
            "stability_regression_desc": "Regression analysis for stability data. Stability regression enables predicting product shelf life based on long-term stability study results. This is crucial in the pharmaceutical and food industries, where product stability directly impacts safety and efficacy.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the name of the parameter under study (e.g., \"API content\", \"Humidity\"), the second column is the time values (e.g., \"Time [months]\"), the third column is the lower specification limit (\"LSL\"), the fourth column is the upper specification limit (\"USL\"), and the subsequent columns contain the measurement results for individual product series. Values must be numerical, and cells should remain blank if data is missing.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing stability data.",
                "display_series": "The selected series will be displayed on the chart along with regression lines.",
                "view_regression_results": "Below the chart, you will find a table with regression parameters for the selected series.",
                "interpretation": "Interpretation of results: Linear regression helps determine the trend of parameter changes over time. An R² value close to 1 indicates a good model fit. The slope of the regression line shows whether the parameter values increase, decrease, or remain stable."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_series": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "plot": {
                "data": "data",
                "regression": "regression",
                "spec_limit": "Specification Limit",
                "x_label": "Time (months)",
                "title": "Stability Analysis"
            },
            "regression_results": {
                "header": "Regression Analysis Results for Selected Series",
                "series": "Series",
                "slope": "Slope",
                "intercept": "Intercept",
                "r_value": "Correlation Coefficient (r)",
                "p_value": "p-value",
                "std_err": "Standard Deviation"
            }
        },
        "temp_humidity_analysis": {
            "title": "Temperature and Humidity Analysis",
            "show_instructions": "Show instructions",
            "temp_humidity": "Temperature and Humidity Analysis",
            "temp_humidity_desc": "Environmental data analysis and identification of limit exceedances. This module allows monitoring environmental conditions, such as temperature and humidity, and detecting any exceedances of established limits. It is particularly important in production and storage processes where environmental conditions can affect product quality and durability.",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the date or timestamp (\"Data\"), the second column is temperature values (\"Temperature [°C]\"), and the third column is humidity values (\"Humidity [%]\"). All values must be numerical, and the date format must be consistent throughout the file.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing temperature and humidity data.",
                "set_limits": "Set temperature and humidity limits using sliders.",
                "view_results": "Browse charts and the list of limit exceedances.",
                "interpretation": "Interpretation of results: Temperature and humidity charts help monitor environmental conditions. Stable values indicate good control of storage conditions. Significant fluctuations may suggest issues with maintaining stability conditions."
            },
            "settings": {
                "temp_lower": "Lower Temperature Limit (°C)",
                "temp_upper": "Upper Temperature Limit (°C)",
                "hum_lower": "Lower Humidity Limit (%)",
                "hum_upper": "Upper Humidity Limit (%)"
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "data_preview": "Data preview (first 10 rows):",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "statistics": {
                "temp_stats": "Temperature Statistics",
                "hum_stats": "Humidity Statistics",
                "mean": "Mean",
                "min": "Minimum",
                "max": "Maximum",
                "rsd": "Relative Standard Deviation (RSD %)"
            },
            "thresholds": {
                "crossings": "Limit Exceedances",
                "no_crossings": "No temperature/humidity limit exceedances.",
                "time": "Time",
                "temperature": "Temperature",
                "humidity": "Humidity"
            },
            "plot": {
                "temp": "Temperature",
                "hum": "Humidity",
                "temp_lower_limit": "Lower Temperature Limit",
                "temp_upper_limit": "Upper Temperature Limit",
                "hum_lower_limit": "Lower Humidity Limit",
                "hum_upper_limit": "Upper Humidity Limit",
                "x_label": "Time",
                "y_label": "Value",
                "title": "Temperature and Humidity"
            }
        },
        "pqr_module": {
            "title": "PQR Module",
            "show_instructions": "Show instructions",
            "pqr_module": "PQR Module",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is sample identifiers or series numbers (\"Series\"), and the subsequent columns are measurement values for various quality parameters (\"API content\", \"Humidity\"). If the file contains more than one data column, the user will be able to choose which one to analyze. The user can also provide lower and upper specification limits.",
                "header": "Instructions",
                "upload_file": "Upload data file",
                "select_series": "Select series for analysis",
                "input_spec_limits": "Enter upper and lower specification limits",
                "view_charts": "View charts",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Choose file",
                "error_two_columns": "The file must contain at least two columns",
                "select_result_column": "Select result column",
                "select_result_column_help": "Choose the column containing data for analysis",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview",
                "error_no_numeric_data": "No numeric data available for analysis",
                "error_processing_file": "Error processing file",
                "no_file_uploaded": "No file uploaded"
            },
            "chart_labels": {
                "time_series": "Series Identifier",
                "values": "Values",
                "observation": "Observation",
                "individual_values": "Individual Values",
                "moving_range": "Moving Range",
                "frequency": "Frequency",
                "histogram_with_spec_limits": "Histogram with Specification Limits",
                "control_chart_with_spec_limits": "Control Chart with Specification Limits"
            },
            "subheaders": {
                "imr_chart": "ImR Control Chart",
                "cpk_analysis": "Process Capability Analysis Cpk",
                "spec_limits_comparison": "Comparison of Results with Specification Limits"
            },
            "spec_limits": {
                "usl": "Upper Specification Limit (USL)",
                "lsl": "Lower Specification Limit (LSL)"
            },
            "warnings": {
                "spec_limits_equal": "Upper and lower specification limits are equal. Please enter valid values."
            },
            "cpk_results": {
                "mean": "Mean",
                "std_dev": "Standard Deviation",
                "cpk": "Cpk Index"
            }
        },
        "anova_module": {
            "title": "Analysis of Variance (ANOVA)",
            "show_instructions": "Show instructions",
            "anova_module": "Analysis of Variance (ANOVA)",
            "instructions": {
                "prepare_file": "Provide an Excel file as required by the module.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing data for different groups.",
                "select_groups": "Select groups for analysis.",
                "perform_anova": "Perform an analysis of variance (ANOVA) on the selected groups.",
                "view_results": "View the results of the ANOVA test and Tukey test.",
                "interpretation": ""
            },
            "file_handling": {
                "choose_file": "Select an Excel file (xlsx or xls):",
                "show_data_preview": "Show preview of uploaded data",
                "data_preview": "Data preview (first 10 rows):",
                "select_groups": "Select groups for analysis:",
                "error_two_columns": "The file must contain at least 2 columns with data.",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "warnings": {
                "need_two_groups": "Select at least two groups for analysis."
            },
            "anova_results": {
                "header": "ANOVA (Analysis of Variance) Results",
                "statistic": "F-Statistic",
                "p_value": "P-Value",
                "significant_result": "There are statistically significant differences between groups.",
                "no_significant_result": "No significant differences between groups."
            },
            "subheaders": {
                "boxplot": "BoxPlot Chart",
                "tukey_test": "Tukey Test – Pairwise Comparison"
            },
            "boxplot": {
                "x_label": "Group",
                "y_label": "Values"
            }
        },
        "dissolution_testing": {
            "title": "Dissolution Profile Comparison",
            "show_instructions": "Show instructions",
            "dissolution_testing": "Dissolution Profile Comparison",
            "instructions": {
                "prepare_file": "Prepare an Excel file: the first row should contain column headers, where the first column is the measurement time (\"Time [min]\"), the second column is the results for the reference product (\"Original [%]\"), and the subsequent columns are the results for individual series of the generic product (\"Series 1 [%]\", \"Series 2 [%]\"). Values must be numerical, and the measurement time should be the same for all series.",
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing dissolution data.",
                "select_groups": "Select groups for comparison:",
                "perform_analysis": "Calculate f1 and f2 similarity factors.",
                "view_results": "View charts and analysis results.",
                "interpretation": "Interpretation of results: The f1 and f2 factors assess the similarity of dissolution profiles between the reference and test product. An f1 value close to 0 and f2 above 50 indicate a high degree of similarity."
            },
            "file_handling": {
                "choose_file": "Select an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_groups": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file.",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "warnings": {
                "need_two_groups": "Select at least two series for comparison."
            },
            "plot": {
                "title": "Dissolution Profile Chart",
                "x_label": "Time (min)",
                "y_label": "Percentage of drug released"
            },
            "analysis_results": {
                "header": "Analysis Results",
                "f1": "Difference Factor (f1)",
                "f2": "Similarity Factor (f2)",
                "significant_result": "Profile considered similar (f2 ≥ 50).",
                "no_significant_result": "Profile considered different (f2 < 50)."
            }
        }
    }
}
