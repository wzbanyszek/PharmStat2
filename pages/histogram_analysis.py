import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, shapiro, skew, kurtosis

def show(language):
    st.header("Analiza histogramów")

    st.write("""
    **Instrukcje:**
    - Wczytaj plik Excel zawierający dane pomiarowe.
    - Wybierz kolumnę do analizy, aby wygenerować histogram i wyświetlić statystyki opisowe.
    """)

    # Wczytywanie pliku
    uploaded_file = st.file_uploader("Wybierz plik Excel (xlsx lub xls):", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            columns = df.columns.tolist()

            # Wybór kolumny z danymi
            selected_column = st.selectbox("Wybierz kolumnę do analizy:", columns)

            data = df[selected_column].dropna()

            # Podgląd danych z możliwością włączania i wyłączania
            show_data = st.checkbox("Pokaż podgląd danych", value=True)
            if show_data:
                st.subheader("Podgląd danych (pierwsze 10 wierszy):")
                st.dataframe(data.head(10))

            # Generowanie histogramu
            plt.figure(figsize=(15, 10))
            plt.hist(data, color="lightgrey", edgecolor="black", bins=20, density=True, label="Histogram danych")
            sns.kdeplot(data, color="blue", label="Gęstość danych")
            plt.title('Histogram danych')
            plt.xlabel("Wartości")
            plt.ylabel("Częstość")
            plt.legend()
            st.pyplot(plt.gcf())

            # Statystyki opisowe
            st.subheader("Statystyki opisowe")
            st.write(f"**Liczba próbek:** {len(data)}")
            st.write(f"**Średnia:** {round(data.mean(), 2)}")
            st.write(f"**Odchylenie standardowe:** {round(data.std(), 2)}")
            st.write(f"**Maksimum:** {data.max()}")
            st.write(f"**Minimum:** {data.min()}")
            st.write(f"**Mediana:** {np.median(data)}")
            st.write(f"**Współczynnik zmienności (RSD %):** {round((data.std() / data.mean()) * 100, 2)}%")

            # Ocena normalności rozkładu (test Shapiro-Wilka)
            st.subheader("Ocena normalności rozkładu")
            stat, p_value = shapiro(data)
            st.write(f"**Test Shapiro-Wilka:** statystyka = {round(stat, 4)}, p-wartość = {round(p_value, 4)}")
            if p_value > 0.05:
                st.success("Brak podstaw do odrzucenia hipotezy o normalności rozkładu.")
            else:
                st.error("Dane nie pochodzą z rozkładu normalnego.")

            # Skośność i kurtoza
            st.subheader("Skośność i kurtoza")
            skewness = skew(data)
            kurt = kurtosis(data)
            st.write(f"**Skośność:** {round(skewness, 2)}")
            st.write(f"**Kurtoza:** {round(kurt, 2)}")

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
