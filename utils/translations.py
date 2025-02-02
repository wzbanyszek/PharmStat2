translations = {
    "Polski": {
        "general": {
            "menu_title": "Menu",
            "intro": "Witaj w aplikacji Santo Pharmstat!",
            "intro_desc": "Aplikacja umożliwia przeprowadzanie analizy danych statystycznych i jakościowych w prosty i intuicyjny sposób. W bocznym menu znajdziesz moduły, które pomogą Ci w analizie danych z różnych perspektyw.",
            "choose_page": "Wybierz podstronę:",
            "upload_data": "Wczytaj dane do analizy przy pomocy wbudowanych formularzy.",
            "view_results": "Wyniki analizy (wykresy, tabele, statystyki) pojawią się w głównym obszarze strony.",
            "customize_view": "Możesz ukrywać lub wyświetlać szczegóły analizy, dostosowując widok do swoich potrzeb.",
            "how_to_use": "Jak korzystać z aplikacji?"
        },
        "descriptive_statistics": {
            "descriptive_stats": "Statystyki opisowe",
            "descriptive_stats_desc": "Obliczanie podstawowych statystyk, takich jak średnia, mediana, odchylenie standardowe.",
            "title": "Statystyki opisowe",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_columns": "Wybierz kolumny, dla których chcesz obliczyć statystyki opisowe.",
                "stats_summary": "Otrzymasz zestawienie najważniejszych statystyk, takich jak średnia, mediana, odchylenie standardowe i inne.",
                "normality_skew_kurtosis": "Dodatkowo ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie."
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
            "histograms": "Histogramy",
            "histograms_desc": "Tworzenie histogramów z oceną normalności rozkładu i analizą skośności oraz kurtozy.",
            "title": "Analiza histogramów",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_column": "Wybierz kolumnę do analizy, aby wygenerować histogram i wyświetlić statystyki opisowe.",
                "normality_test": "Ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie."
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
            "boxplot": "Wykresy pudełkowe BoxPlot",
            "boxplot_desc": "Wizualizacja rozkładu danych i identyfikacja wartości odstających."
        },
        "control_charts": {
            "control_charts": "Karty kontrolne ImR",
            "control_charts_desc": "Monitorowanie stabilności procesów za pomocą kart kontrolnych ImR.",
            "title": "Karty kontrolne ImR",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "data_format": "Plik powinien zawierać dwie kolumny: daty lub ID próbek oraz dane liczbowe.",
                "extra_columns": "Jeśli plik zawiera więcej niż 2 kolumny, dodatkowe kolumny zostaną pominięte.",
                "chart_info": "Generowane będą wykresy ImR, w tym wykres wartości indywidualnych (I) oraz ruchomego rozstępu (MR)."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd wczytanych danych",
                "data_preview": "Podgląd wczytanych danych (pierwsze 10 wierszy):",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej.",
                "error_two_columns": "Plik musi zawierać co najmniej 2 kolumny (Czas/ID, Wartość).",
                "warning_extra_columns": "Plik zawiera dodatkowe kolumny:",
                "using_first_two": "Wykorzystane zostaną tylko pierwsze dwie kolumny."
            },
            "chart_labels": {
                "time_series": "Czas/ID",
                "values": "Wartość",
                "individual_values": "I (Wartości indywidualne)",
                "moving_range": "MR (Ruchomy rozstęp)",
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
            "process_capability": "Analiza zdolności procesowej",
            "process_capability_desc": "Ocena zdolności procesu na podstawie wskaźników Cp i Cpk."
        },
        "stability_regression": {
            "stability_regression": "Regresja dla stabilności",
            "stability_regression_desc": "Analiza regresji dla danych stabilnościowych."
        },
        "temp_humidity_analysis": {
            "temp_humidity": "Analiza temperatury i wilgotności",
            "temp_humidity_desc": "Analiza danych środowiskowych i identyfikacja przekroczeń limitów."
        }
    }
}
