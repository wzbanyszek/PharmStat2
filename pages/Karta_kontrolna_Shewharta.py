import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importujemy klasy i reguły z SPC:
from SPC import XbarRControlChart, Rule01, Rule02, Rule03, Rule04, Rule05, Rule06, Rule07, Rule08

def show():
    """
    Strona prezentująca możliwość wczytania pliku Excel
    (pierwsza kolumna: daty/serie, druga kolumna: wartości),
    a następnie stworzenie karty kontrolnej Shewharta (X-bar / R).
    Zakładamy podgrupy o domyślnej wielkości 4.
    """
    st.header("Karta kontrolna Shewharta (X-bar / R)")

    st.write("""
    **Instrukcje**:
    - Plik Excel musi mieć co najmniej 2 kolumny:
      1. **Czas / ID serii** (np. daty, numer próbki),
      2. **Wartości** (pomiar procesu).
    - Jeśli plik zawiera więcej kolumn, zostaną pominięte.
    - Dane w drugiej kolumnie zostaną grupowane w podgrupy (domyślnie po 4 wiersze na grupę).
    """)

    # Parametr: rozmiar podgrupy (X-bar / R wymaga wielkości > 1)
    subgroup_size = st.number_input(
        "Rozmiar podgrupy (liczba pomiarów w jednej grupie)",
        min_value=2, max_value=50, value=4
    )

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
                st.error("Plik musi zawierać co najmniej 2 kolumny (czas/ID, wartość).")
                return
            
            # Jeżeli jest więcej kolumn, poinformuj użytkownika
            if col_count > 2:
                st.warning(f"Plik zawiera {col_count} kolumn. Wykorzystam tylko pierwsze 2.")

            # Wybieramy tylko pierwsze dwie kolumny
            df = df.iloc[:, :2]
            df.columns = ["Serie/Czas", "Wartość"]

            # Wyświetlamy podgląd danych
            st.subheader("Podgląd wczytanych danych (pierwszych 10 wierszy):")
            st.dataframe(df.head(10))

            # Konwersja pierwszej kolumny na string (jeśli to daty/serie, 
            # to i tak w XbarR potrzebujemy głównie do wyświetlenia w legendzie/daty)
            df["Serie/Czas"] = df["Serie/Czas"].astype(str)

            # Druga kolumna to wartości
            data_array = df["Wartość"].to_numpy()

            # Podział na podgrupy
            # Np. jeśli subgroup_size=4, to co 4 wartości staje się jedną grupą.
            # Obetniemy ewentualne nadwyżkowe wiersze, których nie da się dopasować do pełnych grup.
            total_points = len(data_array)
            full_groups_count = total_points // subgroup_size  # ile pełnych grup

            if full_groups_count < 1:
                st.error("Za mało danych, aby utworzyć choć jedną pełną podgrupę.")
                return

            # Przycinamy do pełnych podgrup
            data_array = data_array[: full_groups_count * subgroup_size]

            # Tworzymy macierz (liczba_podgrup) x (rozmiar_podgrupy)
            reshaped_data = data_array.reshape(full_groups_count, subgroup_size)

            st.write(f"Liczba pełnych podgrup: **{full_groups_count}** (po {subgroup_size} pomiarów w każdej).")

            # Tworzymy obiekt XbarRControlChart
            chart = XbarRControlChart(
                data=reshaped_data, 
                xlabel="Podgrupa",
                ylabel_top="X-bar (Średnia)",
                ylabel_bottom="R (Rozstęp)"
            )
            # Dodajemy limity i reguły
            chart.limits = True
            chart.append_rules([Rule01(), Rule02(), Rule03(), Rule04(), Rule05(), Rule06(), Rule07(), Rule08()])

            # Sprawdzamy normalność (opcjonalnie)
            normally_distributed = chart.normally_distributed(
                data=chart.value_X, significance_level=0.05
            )
            st.write(f"Czy rozkład wartości X jest normalny (test α=0.05)? **{normally_distributed}**")

            # Rysujemy wykres (X-bar / R)
            chart.plot()  # to prawdopodobnie wywołuje plt.show() wewnętrznie
            fig = plt.gcf()
            st.pyplot(fig)

            # Dane wykresu X-bar
            df_xbar = chart.data(0)
            st.write("**Dane wykresu X-bar** (CL, UCL, LCL):")
            st.dataframe(df_xbar[["CL", "UCL", "LCL"]].reset_index(drop=True))

            # Dane wykresu R
            df_range = chart.data(1)
            st.write("**Dane wykresu R** (CL, UCL, LCL):")
            st.dataframe(df_range[["CL", "UCL", "LCL"]].reset_index(drop=True))

            st.write("---")
            st.write(f"Czy wykres jest stabilny wg reguł? **{chart.stable()}**")

            # Informacja o ewentualnie pominiętych wierszach
            leftover = len(df) - (full_groups_count * subgroup_size)
            if leftover > 0:
                st.info(f"Pominięto ostatnich {leftover} wierszy, aby zachować pełne podgrupy.")

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
