import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Zakładamy, że w bibliotece SPC masz te klasy i reguły:
from SPC import XbarRControlChart, Rule01, Rule02, Rule03, Rule04, Rule05, Rule06, Rule07, Rule08

def show():
    """
    Strona prezentująca możliwość wczytania pliku Excel (XLS, XLSX),
    zawierającego co najmniej 2 kolumny:
    1) Daty / ID serii (dowolny tekst lub datetime),
    2) Wartości (liczby, np. pomiar procesu).
    
    Jeśli w pliku jest więcej kolumn, pomijamy je i informujemy użytkownika.
    
    Po wczytaniu:
    - Brak podziału na subgrupy (pomijamy grupowanie),
      co oznacza, że XbarRControlChart będzie otrzymywał tablicę (n x 1).
    - Rysujemy wykres X-bar / R (choć w sensie statystycznym jest to osobliwe,
      bo typowe X-bar / R zakłada >1 pomiar na subgrupę).
    """

    st.header("Karta kontrolna Shewharta (X-bar / R) bez grupowania danych")

    st.write("""
    **Instrukcje**:
    - Plik Excel musi mieć co najmniej 2 kolumny:
      1. **Czas / ID serii** (np. daty, numery próbki, wczytamy jako tekst).
      2. **Wartości** (liczby).
    - Jeśli w pliku jest więcej kolumn, zostaną pominięte.
    - Każda wartość traktowana jest jako osobna „subgrupa” wielkości 1. 
      Dla klasycznego X-bar / R to nietypowa sytuacja (lepszy byłby wykres I–MR),
      jednak to kod zgodny z Twoimi wytycznymi, aby „pominąć grupowanie”.
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
            
            # Komunikat, jeśli jest więcej niż 2 kolumny
            if col_count > 2:
                st.warning(f"Plik zawiera {col_count} kolumn. Wykorzystamy tylko pierwsze dwie.")

            # Wybieramy tylko pierwsze dwie kolumny
            df = df.iloc[:, :2]
            df.columns = ["Czas/ID", "Wartość"]

            # Checkbox do włączania/wyłączania podglądu danych
            show_data = st.checkbox("Pokaż podgląd wczytanych danych", value=True)
            if show_data:
                st.subheader("Podgląd wczytanych danych (pierwszych 10 wierszy):")
                st.dataframe(df.head(10))

            # Konwersja pierwszej kolumny do string (na wszelki wypadek)
            df["Czas/ID"] = df["Czas/ID"].astype(str)

            # Druga kolumna to wartości liczbowe
            # (jeśli ktoś wgra teksty tam, mogą być NaN)
            df["Wartość"] = pd.to_numeric(df["Wartość"], errors='coerce')
            df.dropna(subset=["Wartość"], inplace=True)

            # Tworzymy tablicę n x 1 (n = liczba wierszy)
            data_array = df["Wartość"].to_numpy().reshape(-1, 1)

            # Tworzymy obiekt XbarRControlChart
            chart = XbarRControlChart(
                data=data_array,
                xlabel="Obserwacja",
                ylabel_top="X-bar (Średnia)",
                ylabel_bottom="R (Rozstęp)"
            )

            # Dodajemy limity i reguły
            chart.limits = True
            chart.append_rules([
                Rule01(), Rule02(), Rule03(), Rule04(),
                Rule05(), Rule06(), Rule07(), Rule08()
            ])

            # Sprawdzamy normalność (opcjonalnie)
            normally_distributed = chart.normally_distributed(
                data=chart.value_X, significance_level=0.05
            )
            st.write(f"Czy rozkład wartości X jest normalny (test α=0.05)? **{normally_distributed}**")

            # Rysujemy wykres (X-bar / R)
            chart.plot()  # to wywołuje plt.show() wewnętrznie
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

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
