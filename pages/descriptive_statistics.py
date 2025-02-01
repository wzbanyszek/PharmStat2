import streamlit as st
import pandas as pd
from scipy.stats import shapiro, skew, kurtosis
from utils.data_processing import calculate_descriptive_stats

def show():
    st.header("Statystyki opisowe")

    st.write("""
    **Instrukcje:**
    - Wczytaj plik Excel zawierający dane pomiarowe.
    - Wybierz kolumny, dla których chcesz obliczyć statystyki opisowe.
    - Otrzymasz zestawienie najważniejszych statystyk, takich jak Średnia, mediana, odchylenie standardowe i inne.
    - Dodatkowo ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie.
    """)

    # Wczytywanie pliku
    uploaded_file = st.file_uploader("Wybierz plik Excel (xlsx lub xls):", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.write("**Podgląd danych (pierwsze 5 wierszy):**")
            st.dataframe(df.head())

            columns = df.columns.tolist()
            selected_columns = st.multiselect(
                "Wybierz kolumny do analizy:",
                columns,
                default=columns
            )

            if selected_columns:
                st.subheader("Statystyki opisowe")
                stats = calculate_descriptive_stats(df[selected_columns])
                st.dataframe(stats)

                # Ocena normalności rozkładu, skośność i kurtoza dla każdej kolumny
                for column in selected_columns:
                    st.write(f"---")
                    st.write(f"**Analiza kolumny:** {column}")
                    data = df[column].dropna()

                    # Ocena normalności rozkładu (test Shapiro-Wilka)
                    stat, p_value = shapiro(data)
                    st.write(f"**Test Shapiro-Wilka:** statystyka = {round(stat, 4)}, p-wartość = {round(p_value, 4)}")
                    if p_value > 0.05:
                        st.success("Brak podstaw do odrzucenia hipotezy o normalności rozkładu.")
                    else:
                        st.error("Dane nie pochodzą z rozkładu normalnego.")

                    # Skośność i kurtoza
                    skewness = skew(data)
                    kurt = kurtosis(data)
                    st.write(f"**Skośność:** {round(skewness, 2)}")
                    st.write(f"**Kurtoza:** {round(kurt, 2)}")

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
