import streamlit as st
import pandas as pd
from utils.data_processing import calculate_descriptive_stats

def show():
    st.header("Statystyki opisowe")

    st.write("""
    **Instrukcje:**
    - Wczytaj plik Excel zawierający dane pomiarowe.
    - Wybierz kolumny, dla których chcesz obliczyć statystyki opisowe.
    - Otrzymasz zestawienie najważniejszych statystyk, takich jak Średnia, mediana, odchylenie standardowe i inne.
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

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
