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
            "boxplot_desc": "Wizualizacja rozkładu danych i identyfikacja wartości odstających.",
            "title": "Wykresy BoxPlot",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_columns": "Wybierz kolumny do analizy, aby wygenerować wykresy BoxPlot.",
                "view_stats": "Otrzymasz statystyki opisowe dla wybranych kolumn."
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
            "process_capability_desc": "Ocena zdolności procesu na podstawie wskaźników Cp i Cpk.",
            "title": "Analiza zdolności procesowej",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "set_spec_limits": "Ustaw dolną (LSL) i górną (USL) granicę specyfikacji oraz wartość docelową (Target).",
                "view_results": "Otrzymasz wykres analizy zdolności procesowej oraz wskaźniki Cp i Cpk."
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
            "stability_regression": "Regresja dla stabilności",
            "stability_regression_desc": "Analiza regresji dla danych stabilnościowych.",
            "title": "Analiza danych ze stabilności",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane stabilności.",
                "display_series": "Na wykresie zostaną wyświetlone wybrane serie wraz z liniami regresji.",
                "view_regression_results": "Pod wykresem znajdziesz tabelę z parametrami regresji dla wybranych serii."
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
                "x_label": "Czas (miesiące)",
                "title": "Analiza stabilności"
            },
            "regression_results": {
                "header": "Wyniki analizy regresji dla wybranych serii",
                "series": "Seria",
                "slope": "Nachylenie (slope)",
                "intercept": "Wyraz wolny (intercept)",
                "r_value": "Współczynnik korelacji (r)",
                "p_value": "Wartość p (p-value)",
                "std_err": "Odchylenie standardowe"
            }
        },
        "temp_humidity_analysis": {
            "temp_humidity": "Analiza temperatury i wilgotności",
            "temp_humidity_desc": "Analiza danych środowiskowych i identyfikacja przekroczeń limitów.",
            "title": "Analiza temperatury i wilgotności",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane temperatury i wilgotności.",
                "set_limits": "Ustaw limity temperatury i wilgotności za pomocą suwaków.",
                "view_results": "Przeglądaj wykresy oraz listę przekroczeń limitów."
            },
            "settings": {
                "temp_lower": "Dolna granica temperatury (\u00b0C)",
                "temp_upper": "Górna granica temperatury (\u00b0C)",
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
        }

    }
    "English": {
            "general": {
                "menu_title": "Menu",
                "intro": "Welcome to the Santo Pharmstat application!",
                "intro_desc": "The application allows for statistical and quality data analysis in a simple and intuitive way. In the side menu, you will find modules that help you analyze data from various perspectives.",
                "choose_page": "Choose a page:",
                "upload_data": "Upload data for analysis using the built-in forms.",
                "view_results": "The analysis results (charts, tables, statistics) will appear in the main area of the page.",
                "customize_view": "You can hide or display analysis details, adjusting the view to your needs.",
                "how_to_use": "How to use the application?"
            },
            "descriptive_statistics": {
                "descriptive_stats": "Descriptive Statistics",
                "descriptive_stats_desc": "Calculating basic statistics such as mean, median, and standard deviation.",
                "title": "Descriptive Statistics",
                "instructions": {
                    "header": "Instructions",
                    "upload_file": "Upload an Excel file containing measurement data.",
                    "select_columns": "Select the columns for which you want to calculate descriptive statistics.",
                    "stats_summary": "You will receive a summary of the key statistics such as mean, median, standard deviation, and more.",
                    "normality_skew_kurtosis": "Additionally, assess the normality of the distribution and obtain information on skewness and kurtosis."
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
                "histograms": "Histograms",
                "histograms_desc": "Creating histograms with normality assessment and skewness and kurtosis analysis.",
                "title": "Histogram Analysis",
                "instructions": {
                    "header": "Instructions",
                    "upload_file": "Upload an Excel file containing measurement data.",
                    "select_column": "Select a column to analyze, generate a histogram, and display descriptive statistics.",
                    "normality_test": "Assess the normality of the distribution and obtain information on skewness and kurtosis."
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
            }    
}
