import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import io

# ---------------------------------------------------------
# Ustawienia matplotlib (opcjonalne)
# ---------------------------------------------------------
plt.style.use("seaborn")

# ---------------------------------------------------------
# Funkcje i limity dla temperatury i wilgotności
# ---------------------------------------------------------
temperature_limit = (23, 27)  # 23 - 27 °C
humidity_limit = (55, 65)     # 55% - 65%

def generate_report_streamlit(file_content):
    """
    Generuje raport z pliku Excel (pomiary temperatury i wilgotności),
    wyświetla wyniki w Streamlit (zamiast print/plt.show).
    """

    try:
        # Wczytujemy plik Excel do DataFrame
        df = pd.read_excel(io.BytesIO(file_content), header=None, skiprows=1)
        df.columns = ['time', 'temperature', 'humidity']

        # Konwersja kolumny daty na format datetime
        df['time'] = pd.to_datetime(df['time'], format='%m/%d/%y %H:%M', errors='coerce')
        # Usunięcie wierszy z błędną datą
        df = df.dropna(subset=['time'])

        # Wyszukiwanie przekroczeń progów (threshold crossing)
        threshold_crossings = []
        for i in range(1, len(df)):
            prev_temp = df['temperature'].iloc[i-1]
            curr_temp = df['temperature'].iloc[i]
            prev_hum  = df['humidity'].iloc[i-1]
            curr_hum  = df['humidity'].iloc[i]

            if ((prev_temp < 23 and curr_temp >= 23) or
                (prev_temp >= 23 and curr_temp < 23) or
                (prev_temp < 27 and curr_temp >= 27) or
                (prev_temp > 27 and curr_temp <= 27) or
                (prev_hum < 55 and curr_hum >= 55) or
                (prev_hum >= 55 and curr_hum < 55) or
                (prev_hum < 65 and curr_hum >= 65) or
                (prev_hum > 65 and curr_hum <= 65)):
                threshold_crossings.append({
                    'time': df['time'].iloc[i],
                    'temperature': curr_temp,
                    'humidity': curr_hum
                })

        crossings_df = pd.DataFrame(threshold_crossings)

        # Wyświetlamy krótką tabelkę przekroczeń
        st.subheader("Przekroczenia progów temperatury / wilgotności")
        if not crossings_df.empty:
            st.dataframe(crossings_df)
        else:
            st.write("Brak przekroczeń granic.")

        st.write("---")
        st.subheader("Statystyki temperatury")
        avg_temp = df["temperature"].mean()
        min_temp = df["temperature"].min()
        max_temp = df["temperature"].max()
        rsd_temp = (df["temperature"].std() / avg_temp * 100) if avg_temp != 0 else None
        st.write(f"- **Średnia:** {avg_temp:.2f}")
        st.write(f"- **Minimum:** {min_temp:.2f}")
        st.write(f"- **Maksimum:** {max_temp:.2f}")
        st.write(f"- **RSD:** {rsd_temp:.2f}%")
        st.write(f"- **Liczba pomiarów:** {len(df['temperature'])}")

        st.subheader("Statystyki wilgotności")
        avg_hum = df["humidity"].mean()
        min_hum = df["humidity"].min()
        max_hum = df["humidity"].max()
        rsd_hum = (df["humidity"].std() / avg_hum * 100) if avg_hum != 0 else None
        st.write(f"- **Średnia:** {avg_hum:.2f}")
        st.write(f"- **Minimum:** {min_hum:.2f}")
        st.write(f"- **Maksimum:** {max_hum:.2f}")
        st.write(f"- **RSD:** {rsd_hum:.2f}%")
        st.write(f"- **Liczba pomiarów:** {len(df['humidity'])}")

        # Rysujemy wykres temperatury i wilgotności + linie limitów
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['time'], df['temperature'], label='Temperature')
        ax.plot(df['time'], df['humidity'], label='Humidity')
        ax.axhline(y=temperature_limit[0], color='blue', linestyle='--', label='Temp Lower Limit')
        ax.axhline(y=temperature_limit[1], color='blue', linestyle='--', label='Temp Upper Limit')
        ax.axhline(y=humidity_limit[0], color='green', linestyle='--', label='Humidity Lower Limit')
        ax.axhline(y=humidity_limit[1], color='green', linestyle='--', label='Humidity Upper Limit')

        ax.set_xlabel('Datetime')
        ax.set_ylabel('Value')
        ax.set_title('Temperature and Humidity Monitoring')
        ax.grid(True)
        ax.legend()
        fig.tight_layout()

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Wystąpił błąd podczas analizy pliku: {e}")

# ---------------------------------------------------------
# Strony istniejącej aplikacji
# ---------------------------------------------------------
def show_intro():
    st.header("Wprowadzenie")
    st.write("""
    **Witaj w przykładowej aplikacji Streamlit!**  
    ...
    (Treść wprowadzenia)
    """)

def show_scatter_line():
    st.header("Wykres punktowy i liniowy")
    num_rows = st.slider("Ile punktów losowych wygenerować?", 5, 300, 50)
    X = np.linspace(0, 10, num_rows)
    noise = np.random.randn(num_rows) * 3
    Y = 2.5 * X + noise
    df = pd.DataFrame({"X": X, "Y": Y})
    st.write("**Podgląd danych (pierwsze 5 wierszy):**")
    st.dataframe(df.head())
    
    chart_type = st.selectbox("Wybierz rodzaj wykresu:", ["Punktowy (scatter)", "Liniowy (line)"])
    
    if st.button("Rysuj wykres"):
        fig, ax = plt.subplots()
        if chart_type == "Punktowy (scatter)":
            ax.scatter(df["X"], df["Y"], color="blue", alpha=0.7)
            ax.set_title("Wykres punktowy")
        else:
            ax.plot(df["X"], df["Y"], color="red")
            ax.set_title("Wykres liniowy")

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        st.pyplot(fig)

def show_linreg_scipy():
    st.header("Regresja Liniowa (SciPy)")
    st.write("... opis ...")
    num_points = st.slider("Liczba punktów danych:", 10, 300, 50)
    X = np.linspace(0, 10, num_points)
    true_a = 3.0
    true_b = 2.0
    noise = np.random.randn(num_points) * 3
    Y = true_a * X + true_b + noise
    df_reg = pd.DataFrame({"X": X, "Y": Y})
    st.dataframe(df_reg.head())

    if st.button("Dopasuj regresję i narysuj wykres"):
        slope, intercept, r_value, p_value, std_err = linregress(X, Y)
        Y_pred = slope * X + intercept

        fig, ax = plt.subplots()
        ax.scatter(X, Y, label="Dane (punkty)", alpha=0.7)
        ax.plot(X, Y_pred, color="red", label="Linia regresji")
        ax.set_title("Regresja Liniowa: Y = aX + b")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        st.pyplot(fig)

        st.write(f"**Nachylenie (slope)** = {slope:.3f}")
        st.write(f"**Wyraz wolny (intercept)** = {intercept:.3f}")
        st.write(f"**Współczynnik korelacji (r)** = {r_value:.3f}")
        st.write(f"**Wartość p (p-value)** = {p_value:.3e}")
        st.write(f"**Odchylenie standardowe (std_err)** = {std_err:.3f}")

def show_spc():
    st.header("Analiza SPC (Shewhart & Cpk)")
    st.write("... opis ...")
    n_measurements = st.slider("Ile pomiarów chcesz wygenerować?", 10, 300, 50)
    mean_process = st.number_input("Średnia procesu (np. 50.0)", value=50.0)
    std_process = st.number_input("Odchylenie standardowe procesu (np. 2.0)", value=2.0, min_value=0.0, step=0.1)
    lsl = st.number_input("LSL (Lower Spec Limit)", value=45.0)
    usl = st.number_input("USL (Upper Spec Limit)", value=55.0)

    if st.button("Analizuj proces"):
        data = mean_process + std_process * np.random.randn(n_measurements)
        x_mean = np.mean(data)
        x_std = np.std(data, ddof=1)
        st.write(f"**Średnia z próby =** {x_mean:.3f}")
        st.write(f"**Odchylenie standardowe z próby =** {x_std:.3f}")

        ucl = x_mean + 3 * x_std
        lcl = x_mean - 3 * x_std

        fig, ax = plt.subplots()
        ax.plot(data, marker='o', label='Pomiary')
        ax.axhline(x_mean, color='green', linestyle='--', label='CL (Center Line)')
        ax.axhline(ucl, color='red', linestyle='--', label='UCL (+3σ)')
        ax.axhline(lcl, color='red', linestyle='--', label='LCL (–3σ)')
        ax.set_title("Wykres Shewharta (X-chart)")
        ax.set_xlabel("Nr pomiaru")
        ax.set_ylabel("Wartość pomiaru")
        ax.legend()
        st.pyplot(fig)

        if x_std > 0:
            cpk_lower = (x_mean - lsl) / (3 * x_std)
            cpk_upper = (usl - x_mean) / (3 * x_std)
            cpk_value = min(cpk_lower, cpk_upper)
        else:
            cpk_value = np.nan

        st.write(f"**Cpk** = {cpk_value:.3f}")
        st.warning("""
        Interpretacja Cpk:
        - Cpk > 1.33 -> proces uznawany za zdolny,
        - 1.0 < Cpk < 1.33 -> może wymagać usprawnień,
        - Cpk < 1.0 -> proces nie spełnia wymagań.
        """)
        if lsl >= usl:
            st.error("Uwaga: LSL >= USL! Sprawdź poprawność granic specyfikacji.")

def show_excel_upload():
    st.header("Wczytywanie pliku Excel")
    st.write("""
    Ta część aplikacji pozwala wgrać własny plik Excel (format `.xlsx` lub `.xls`) 
    i wyświetlić jego zawartość w postaci tabeli, wraz z przykładowymi statystykami.
    """)
    uploaded_file = st.file_uploader(
        "Wybierz plik Excel (xlsx, xls):",
        type=["xlsx", "xls"]
    )
    if uploaded_file is not None:
        try:
            df_excel = pd.read_excel(uploaded_file)
            st.success("Plik wczytany poprawnie. Oto podgląd danych:")
            st.dataframe(df_excel.head(20))

            st.subheader("Podstawowe statystyki")
            st.write(df_excel.describe())
        except Exception as e:
            st.error(f"Błąd odczytu pliku: {e}")
    else:
        st.info("Najpierw wybierz plik w polu powyżej.")

def show_temp_hum_analysis():
    st.header("Analiza temperatury i wilgotności z pliku Excel")
    st.write("""
    Tu możesz przesłać plik z danymi (kolumny: `time`, `temperature`, `humidity`).  
    Zostaną obliczone statystyki, przekroczenia limitów (23-27°C, 55-65%) 
    oraz wygenerowany wykres.
    """)

    uploaded_file = st.file_uploader(
        "Wybierz plik Excel (xlsx, xls):",
        type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        st.write(f"Analiza pliku: **{uploaded_file.name}**")
        file_bytes = uploaded_file.read()
        # Wywołujemy zmodyfikowaną funkcję generowania raportu
        generate_report_streamlit(file_bytes)
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")


# ---------------------------------------------------------
# GŁÓWNA CZĘŚĆ APLIKACJI – MENU
# ---------------------------------------------------------
st.title("Aplikacja wielostronicowa w Streamlit")

page = st.sidebar.radio(
    "Wybierz podstronę:",
    [
        "Wprowadzenie",
        "Wykres punktowy i liniowy",
        "Regresja liniowa (SciPy)",
        "Analiza SPC (Shewhart & Cpk)",
        "Wczytanie pliku Excel",
        "Analiza temperatury i wilgotności"
    ]
)

if page == "Wprowadzenie":
    show_intro()

elif page == "Wykres punktowy i liniowy":
    show_scatter_line()

elif page == "Regresja liniowa (SciPy)":
    show_linreg_scipy()

elif page == "Analiza SPC (Shewhart & Cpk)":
    show_spc()

elif page == "Wczytanie pliku Excel":
    show_excel_upload()

elif page == "Analiza temperatury i wilgotności":
    show_temp_hum_analysis()
