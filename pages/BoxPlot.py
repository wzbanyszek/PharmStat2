import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_processing import calculate_descriptive_stats

def show(language):
    st.header("Wykresy BoxPlot")
    st.write("""
    Ta sekcja pozwala wczytać plik Excel i wygenerować wykresy BoxPlot dla poszczególnych kolumn.
    """)

    uploaded_file = st.file_uploader(
        "Wybierz plik Excel (xlsx, xls):",
        type=["xlsx", "xls"]
    )

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
                # Generuj wykres BoxPlot
                st.subheader("Wykresy BoxPlot")
                fig, ax = plt.subplots(figsize=(10, 6))
                df[selected_columns].boxplot(ax=ax)
                ax.set_title("Wykresy BoxPlot dla wybranych kolumn")
                ax.set_ylabel("Wartości")
                ax.grid(True)
                st.pyplot(fig)

                # Statystyki opisowe
                st.subheader("Statystyki opisowe")
                stats = calculate_descriptive_stats(df[selected_columns])
                st.dataframe(stats)

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
