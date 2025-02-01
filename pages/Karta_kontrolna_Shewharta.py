import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import klasy ImRControlChart i reguł z biblioteki SPC
from SPC import ImRControlChart, Rule01, Rule02, Rule03, Rule04, Rule05, Rule06, Rule07, Rule08

def show():
    st.header("Karta kontrolna ImR (Individual – Moving Range)")

    st.write("""
    **Instrukcje**:
    - Wczytaj plik Excel zawierający **co najmniej 2 kolumny**:
      1. **Czas / ID serii** (np. daty, numery próbki),
      2. **Wartości** (liczby).
    - Jeśli plik zawiera więcej niż 2 kolumny, zostaną one pominięte.
    - Wykres **ImR** (Individual – Moving Range) pokazuje:
      - Wartości indywidualne (I-chart),
      - Ruchomy rozstęp między kolejnymi pomiarami (MR-chart).
    """)

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

            # Checkbox do podglądu danych
            show_data = st.checkbox("Pokaż podgląd wczytanych danych", value=True)
            if show_data:
                st.subheader("Podgląd wczytanych danych (pierwsze 10 wierszy):")
                st.dataframe(df.head(10))

            # Konwersja kolumn
            df["Czas/ID"] = df["Czas/ID"].astype(str)
            df["Wartość"] = pd.to_numeric(df["Wartość"], errors='coerce')
            df.dropna(subset=["Wartość"], inplace=True)

            if df.empty:
                st.error("Brak prawidłowych danych liczbowych w kolumnie 'Wartość'.")
                return

            # Tworzenie tablicy n x 1 (n = liczba pomiarów)
            data_array = df["Wartość"].to_numpy().reshape(-1, 1)

            # Tworzenie wykresu ImR
            chart = ImRControlChart(
                data=data_array,
                xlabel="Obserwacja",
                ylabel_top="I (Wartość indywidualna)",
                ylabel_bottom="MR (Ruchomy rozstęp)"
            )

            # Dodawanie reguł
            chart.limits = True
            chart.append_rules([
                Rule01(), Rule02(), Rule03(), Rule04(),
                Rule05(), Rule06(), Rule07(), Rule08()
            ])

            # Sprawdzanie normalności danych (użycie value_I)
            normally_distributed = chart.normally_distributed(
                data=chart.value_I, significance_level=0.05
            )
            st.write(f"Czy rozkład wartości I jest normalny (test α=0.05)? **{normally_distributed}**")

            # Rysowanie wykresu
            chart.plot()
            fig = plt.gcf()
            st.pyplot(fig)

            # Checkboxy do ukrywania/wyświetlania tabel z danymi
            show_I_data = st.checkbox("Pokaż dane wykresu I (wartości indywidualne)", value=True)
            show_MR_data = st.checkbox("Pokaż dane wykresu MR (ruchomy rozstęp)", value=True)

            # Dane wykresu I
            if show_I_data:
                df_I = chart.data(0)
                st.write("**Dane wykresu I (wartości indywidualne)** (CL, UCL, LCL):")
                st.dataframe(df_I[["CL", "UCL", "LCL"]].reset_index(drop=True))

            # Dane wykresu MR
            if show_MR_data:
                df_MR = chart.data(1)
                st.write("**Dane wykresu MR (ruchomy rozstęp)** (CL, UCL, LCL):")
                st.dataframe(df_MR[["CL", "UCL", "LCL"]].reset_index(drop=True))

            st.write("---")
            st.write(f"Czy proces jest stabilny wg reguł? **{chart.stable()}**")

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
