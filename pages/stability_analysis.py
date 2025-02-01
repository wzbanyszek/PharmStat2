import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def show(language):
    st.header("Analiza danych ze stabilności")

    st.write("""
    **Instrukcje:**
    - Wczytaj plik Excel zawierający dane stabilności.
    - Na wykresie zostaną wyświetlone wybrane serie wraz z liniami regresji.
    - Pod wykresem znajdziesz tabelę z parametrami regresji dla wybranych serii.
    """)

    # Wczytywanie pliku
    uploaded_file = st.file_uploader("Wybierz plik Excel (xlsx lub xls):", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            
            # Pobranie nazwy parametru
            parameter_name = df.iloc[0, 0]

            # Pobranie danych
            time = df['Time']
            min_spec = df['Min'].iloc[0] if not pd.isna(df['Min'].iloc[0]) else None
            max_spec = df['Max'].iloc[0] if not pd.isna(df['Max'].iloc[0]) else None

            series_columns = df.columns[4:]

            # Podgląd danych z możliwością włączania i wyłączania
            show_data = st.checkbox("Pokaż podgląd danych", value=True)
            if show_data:
                st.write("**Podgląd danych (pierwsze 12 wierszy):**")
                st.dataframe(df.head(12))

            # Wybór serii do analizy
            selected_series = st.multiselect("Wybierz serie do analizy:", series_columns, default=series_columns)

            # Tworzenie wykresu
            fig, ax = plt.subplots(figsize=(12, 8))

            regression_results = []

            for col in selected_series:
                y = df[col].dropna()
                x = time[:len(y)]

                # Dopasowanie regresji liniowej
                slope, intercept, r_value, p_value, std_err = linregress(x, y)
                y_pred = slope * x + intercept

                # Rysowanie danych i linii regresji
                ax.scatter(x, y, label=f"{col} (dane)", alpha=0.7)
                ax.plot(x, y_pred, label=f"{col} (regresja)", linestyle='--')

                # Zapisywanie wyników regresji
                regression_results.append({
                    "Seria": col,
                    "Nachylenie\n(slope)": round(slope, 3),
                    "Wyraz wolny\n(intercept)": round(intercept, 3),
                    "Współczynnik\nkorelacji (r)": round(r_value, 3),
                    "Wartość p\n(p-value)": f"{p_value:.3e}",
                    "Odchylenie\nstandardowe": round(std_err, 3)
                })

            # Dodawanie linii specyfikacji
            if min_spec is not None:
                ax.axhline(min_spec, color='red', linestyle='-', label='Limit specyfikacji')
            if max_spec is not None:
                ax.axhline(max_spec, color='red', linestyle='-', label='Limit specyfikacji')

            ax.set_xlabel("Czas (miesiące)")
            ax.set_ylabel(parameter_name)
            ax.set_title(f"Analiza stabilności: {parameter_name}")
            ax.legend()
            st.pyplot(fig)

            # Wyświetlanie wyników regresji
            st.subheader("Wyniki analizy regresji dla wybranych serii")
            regression_df = pd.DataFrame(regression_results)
            st.dataframe(regression_df)

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
