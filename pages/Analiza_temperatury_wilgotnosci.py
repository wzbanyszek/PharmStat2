import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    """
    Podstrona aplikacji Streamlit do analizy temperatury i wilgotności
    na podstawie pliku Excel z kolumnami: time, temperature, humidity.
    Użytkownik może również samodzielnie ustawić limity temperatury i wilgotności
    (domyślnie 23–27°C, 55–65%).
    """
    st.header("Analiza temperatury i wilgotności")

    st.write("""
    Ta sekcja pozwala wgrać plik Excel zawierający co najmniej trzy kolumny:
    - **time** (datetime lub tekst dający się skonwertować do daty/czasu),
    - **temperature** (wartości temperatury, np. w °C),
    - **humidity** (wartości wilgotności, np. w %).

    Po wczytaniu pliku nastąpi:
    1. Sprawdzenie poprawności danych (parsowanie kolumny 'time').
    2. Obliczenie podstawowych statystyk (średnia, min, max, RSD).
    3. Zidentyfikowanie punktów przekraczających założone limity temperatury i wilgotności.
    4. Wyświetlenie wykresu temperatury i wilgotności wraz z liniami granicznymi.
    """)

    # Suwaki do ustawienia granic temperatury
    st.subheader("Ustaw granice temperatury (°C)")
    temp_lower = st.slider("Dolna granica temperatury", min_value=0, max_value=100, value=23)
    temp_upper = st.slider("Górna granica temperatury", min_value=0, max_value=100, value=27)

    # Suwaki do ustawienia granic wilgotności
    st.subheader("Ustaw granice wilgotności (%)")
    hum_lower = st.slider("Dolna granica wilgotności", min_value=0, max_value=100, value=55)
    hum_upper = st.slider("Górna granica wilgotności", min_value=0, max_value=100, value=65)

    # Uploader pliku
    uploaded_file = st.file_uploader(
        "Wybierz plik Excel (xlsx, xls):",
        type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            # Wczytujemy plik Excel do DataFrame
            # Jeśli plik ma nagłówek w pierwszym wierszu, usuń 'header=None, skiprows=1'
            # lub dostosuj do swojego formatu.
            df = pd.read_excel(uploaded_file, header=None, skiprows=1)
            df.columns = ['time', 'temperature', 'humidity']

            # Konwersja kolumny czasu na datetime
            df['time'] = pd.to_datetime(df['time'], errors='coerce')
            # Usuwamy wiersze z niepoprawną datą
            df.dropna(subset=['time'], inplace=True)

            st.subheader("Podgląd danych")
            st.dataframe(df.head(10))

            # Podstawowe statystyki: mean, min, max, RSD itp.
            st.subheader("Statystyki temperatury")
            mean_temp = df['temperature'].mean()
            min_temp = df['temperature'].min()
            max_temp = df['temperature'].max()
            std_temp = df['temperature'].std()
            rsd_temp = (std_temp / mean_temp * 100) if mean_temp != 0 else None

            st.write(f"- **Średnia (°C)**: {mean_temp:.2f}")
            st.write(f"- **Min (°C)**: {min_temp:.2f}")
            st.write(f"- **Max (°C)**: {max_temp:.2f}")
            st.write(f"- **RSD (%)**: {rsd_temp:.2f}")

            st.subheader("Statystyki wilgotności")
            mean_hum = df['humidity'].mean()
            min_hum = df['humidity'].min()
            max_hum = df['humidity'].max()
            std_hum = df['humidity'].std()
            rsd_hum = (std_hum / mean_hum * 100) if mean_hum != 0 else None

            st.write(f"- **Średnia (%)**: {mean_hum:.2f}")
            st.write(f"- **Min (%)**: {min_hum:.2f}")
            st.write(f"- **Max (%)**: {max_hum:.2f}")
            st.write(f"- **RSD (%)**: {rsd_hum:.2f}")

            # Wyszukiwanie momentów przekraczania limitów
            threshold_crossings = []
            for i in range(1, len(df)):
                prev_temp = df['temperature'].iloc[i-1]
                curr_temp = df['temperature'].iloc[i]
                prev_hum  = df['humidity'].iloc[i-1]
                curr_hum  = df['humidity'].iloc[i]

                # Logika przekroczeń / powrotu do normy
                if ((prev_temp < temp_lower and curr_temp >= temp_lower) or
                    (prev_temp >= temp_lower and curr_temp < temp_lower) or
                    (prev_temp < temp_upper and curr_temp >= temp_upper) or
                    (prev_temp > temp_upper and curr_temp <= temp_upper) or
                    (prev_hum < hum_lower and curr_hum >= hum_lower) or
                    (prev_hum >= hum_lower and curr_hum < hum_lower) or
                    (prev_hum < hum_upper and curr_hum >= hum_upper) or
                    (prev_hum > hum_upper and curr_hum <= hum_upper)):
                    threshold_crossings.append({
                        'time': df['time'].iloc[i],
                        'temperature': curr_temp,
                        'humidity': curr_hum
                    })

            # Wyświetlanie przekroczeń w tabeli (o ile istnieją)
            st.subheader("Przekroczenia limitów")
            if threshold_crossings:
                crossings_df = pd.DataFrame(threshold_crossings)
                st.dataframe(crossings_df)
            else:
                st.write("Brak przekroczeń granic temperatury / wilgotności.")

            # Wykres temperatury i wilgotności
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(df['time'], df['temperature'], label='Temperature', color='red')
            ax.plot(df['time'], df['humidity'], label='Humidity', color='blue')

            # Linie poziome limitów
            ax.axhline(y=temp_lower, color='red', linestyle='--', label='Temp Lower Limit')
            ax.axhline(y=temp_upper, color='red', linestyle='--', label='Temp Upper Limit')
            ax.axhline(y=hum_lower, color='blue', linestyle='--', label='Hum Lower Limit')
            ax.axhline(y=hum_upper, color='blue', linestyle='--', label='Hum Upper Limit')

            ax.set_xlabel('Czas')
            ax.set_ylabel('Wartość')
            ax.set_title('Temperatura i Wilgotność')
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Wystąpił błąd podczas analizy pliku: {e}")
    else:
        st.info("Nie wybrano pliku - proszę wgrać plik Excel powyżej.")
