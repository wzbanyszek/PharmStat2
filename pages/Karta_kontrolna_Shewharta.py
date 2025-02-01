import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importujemy klasy i reguły z biblioteki SPC
from SPC import IMRControlChart, Rule01, Rule02, Rule03, Rule04, Rule05, Rule06, Rule07, Rule08

def show():
    """
    Strona aplikacji Streamlit do generowania wykresu I-MR (Individual – Moving Range).
    Wczytujemy dane z pliku Excel: 
    - 1. kolumna: Daty / ID serii (np. numery próbki, daty),
    - 2. kolumna: Wartości pomiarowe (liczby).
    
    Jeśli plik zawiera więcej kolumn, pomijamy je i informujemy użytkownika.
    Użytkownik może zdecydować, czy chce wyświetlić podgląd danych.
    """

    st.header("Karta kontrolna I-MR (Individual – Moving Range)")

    st.write("""
    **Instrukcje**:
    - Wczytaj plik Excel zawierający **co najmniej 2 kolumny**:
      1. **Czas / ID serii** (np. daty, numery próbki),
      2. **Wartości** (liczby).
    - Jeśli plik zawiera więcej niż 2 kolumny, zostaną one pominięte.
    - Wykres **I-MR** (Individual – Moving Range) pokazuje:
      - Wartości indywidualne (I-chart),
      - Ruchomy rozstęp między kolejnymi pomiarami (MR-chart).
    """)

    # Uploader pliku
    uploaded_file = st.file_uploader(
        "Wybierz plik Excel (xlsx lub xls):",
        type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            # Sprawdzamy liczbę kolumn
            col_count = df.shape[1]
            if col_count < 2:
                st.error("Plik musi zawierać co najmniej 2 kolumny (Czas/ID, Wartość).")
                return

            # Informacja, jeśli jest więcej kolumn
            if col_count > 2:
                st.warning(f"Plik zawiera {col_count} kolumn. Wykorzystamy tylko pierwsze dwie.")

            # Wybieramy tylko pierwsze dwie kolumny
            df = df.iloc[:, :2]
            df.columns = ["Czas/ID", "Wartość"]

            # Checkbox do włączania/wyłączania podglądu danych
            show_data = st.checkbox("Pokaż podgląd wczytanych danych", value=True)
            if show_data:
                st.subheader("Podgląd wczytanych danych (pierwsze 10 wierszy):")
                st.dataframe(df.head(10))

            # Konwersja kolumny "Czas/ID" na string (dla spójności)
            df["Czas/ID"] = df["Czas/ID"].astype(str)

            # Konwersja kolumny "Wartość" na numeryczne
            df["Wartość"] = pd.to_numeric(df["Wartość"], errors='coerce')
            df.dropna(subset=["Wartość"], inplace=True)

            if df.empty:
                st.error("Brak prawidłowych danych liczbowych w kolumnie 'Wartość'.")
                return

            # Tworzymy tablicę n x 1 (n = liczba pomiarów)
            data_array = df["Wartość"].to_numpy().reshape(-1, 1)

            # Tworzenie obiektu IMRControlChart
            chart = IMRControlChart(
                data=data_array,
                xlabel="Obserwacja",
                ylabel_top="I (Wartość indywidualna)",
                ylabel_bottom="MR (Ruchomy rozstęp)"
            )

            # Dodajemy limity i reguły
            chart.limits = True
            chart.append_rules([
                Rule01(), Rule02(), Rule03(), Rule04(),
                Rule05(), Rule06(), Rule07(), Rule08()
            ])

            # Sprawdzamy normalność danych (opcjonalnie)
            normally_distributed = chart.normally_distributed(
                data=chart.value_X, significance_level=0.05
            )
            st.write(f"Czy rozkład wartości I jest normalny (test α=0.05)? **{normally_distributed}**")

            # Rysujemy wykres I-MR
            chart.plot()  # zakładamy, że ta metoda rysuje oba wykresy
            fig = plt.gcf()
            st.pyplot(fig)

            # Dane wykresu I
            df_I = chart.data(0)
            st.write("**Dane wykresu I (wartości indywidualne)** (CL, UCL, LCL):")
            st.dataframe(df_I[["CL", "UCL", "LCL"]].reset_index(drop=True))

            # Dane wykresu MR
            df_MR = chart.data(1)
            st.write("**Dane wykresu MR (ruchomy rozstęp)** (CL, UCL, LCL):")
            st.dataframe(df_MR[["CL", "UCL", "LCL"]].reset_index(drop=True))

            st.write("---")
            st.write(f"Czy proces jest stabilny wg reguł? **{chart.stable()}**")

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
