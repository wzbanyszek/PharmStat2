import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

def show():
    st.header("Analiza zdolności procesowej (Process Capability Analysis)")

    st.write("""
    **Instrukcje:**
    - Wczytaj plik Excel zawierający dane pomiarowe.
    - Ustaw dolną (LSL) i górną (USL) granicę specyfikacji oraz wartość docelową (Target).
    - Otrzymasz wykres analizy zdolności procesowej oraz wskaźniki Cp i Cpk.
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

            # Ustawienie granic specyfikacji i wartości docelowej
            st.subheader("Ustawienia specyfikacji")
            target = st.number_input("Wartość docelowa (Target)", value=float(data.mean()))
            LSL = st.number_input("Dolna granica specyfikacji (LSL)", value=float(data.min()))
            USL = st.number_input("Górna granica specyfikacji (USL)", value=float(data.max()))

            # Generowanie wykresu
            x = np.linspace(min(data), max(data), 1000)
            y = norm.pdf(x, loc=target, scale=data.std())

            plt.figure(figsize=(15, 10))
            plt.hist(data, color="lightgrey", edgecolor="black", density=True, label="Histogram danych")
            sns.kdeplot(data, color="blue", label="Gęstość danych")
            plt.plot(x, y, linestyle="--", color="black", label="Teoretyczna gęstość (Normalna)")
            plt.axvline(LSL, linestyle="--", color="red", label="LSL")
            plt.axvline(USL, linestyle="--", color="orange", label="USL")
            plt.axvline(target, linestyle="--", color="green", label="Target")
            plt.title('Analiza zdolności procesowej')
            plt.xlabel("Wartości")
            plt.ylabel("")
            plt.yticks([])
            plt.legend()
            st.pyplot(plt.gcf())

            # Obliczenia wskaźników Cp i Cpk
            Cp = (USL - LSL) / (6 * np.std(data))
            Cpk = min((USL - data.mean()) / (3 * data.std()), (data.mean() - LSL) / (3 * data.std()))

            # Obliczenia dodatkowe
            num_samples = len(data)
            sample_mean = data.mean()
            sample_std = data.std()
            sample_max = data.max()
            sample_min = data.min()
            sample_median = np.median(data)

            pct_below_LSL = len(data[data < LSL]) / len(data) * 100
            pct_above_USL = len(data[data > USL]) / len(data) * 100

            # Wyświetlanie wyników
            st.subheader("Wyniki analizy")

            st.write(f"**Cp:** {round(Cp, 2)}")
            st.write(f"**Cpk:** {round(Cpk, 2)}")

            st.write("---")
            st.write(f"**Liczba próbek:** {num_samples}")
            st.write(f"**Średnia próbki:** {round(sample_mean, 2)}")
            st.write(f"**Odchylenie standardowe:** {round(sample_std, 2)}")
            st.write(f"**Maksimum:** {sample_max}")
            st.write(f"**Minimum:** {sample_min}")
            st.write(f"**Mediana:** {sample_median}")

            st.write(f"**Procent próbek poniżej LSL:** {round(pct_below_LSL, 2)}%")
            st.write(f"**Procent próbek powyżej USL:** {round(pct_above_USL, 2)}%")

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
