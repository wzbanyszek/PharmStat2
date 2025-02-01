import streamlit as st
import pandas as pd
from scipy.stats import shapiro, skew, kurtosis
from utils.data_processing import calculate_descriptive_stats

def show(language):
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

            # Podgląd danych z możliwością włączania i wyłączania
            show_data = st.checkbox("Pokaż podgląd danych", value=True)
            if show_data:
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

                # Dodanie wyników testu normalności, skośności i kurtozy jako wierszy
                additional_stats = {}
                for column in selected_columns:
                    data = df[column].dropna()
                    stat, p_value = shapiro(data)
                    skewness = skew(data)
                    kurt = kurtosis(data)

                    additional_stats.setdefault("Shapiro-Wilk p-wartość", []).append(round(p_value, 4))
                    additional_stats.setdefault("Skośność", []).append(round(skewness, 2))
                    additional_stats.setdefault("Kurtoza", []).append(round(kurt, 2))

                # Konwersja dodatkowych wyników do DataFrame
                additional_stats_df = pd.DataFrame(additional_stats, index=selected_columns).T

                # Łączenie statystyk opisowych z dodatkowymi statystykami
                full_stats = pd.concat([stats, additional_stats_df])

                st.dataframe(full_stats)

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
