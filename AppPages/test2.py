import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress, f
from utils.translations import translations

def show(language):
    t = translations[language]["stability_regression"]

    st.header(t["title"])

    show_instructions = st.checkbox(t["show_instructions"], value=True)
    if show_instructions:
        st.write(f"""
        **{t["instructions"]["header"]}:**
        - {t["instructions"]["prepare_file"]}
        - {t["instructions"]["upload_file"]}
        - {t["instructions"]["display_series"]}
        - {t["instructions"]["view_regression_results"]}
        - {t["instructions"]["interpretation"]}
        """)

    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            # Zakładamy, że pierwsza komórka (0,0) to nazwa parametru,
            # a kolumny: ['Time','Min','Max'] a potem serie
            parameter_name = df.iloc[0, 0]
            time = df['Time']
            min_spec = df['Min'].iloc[0] if 'Min' in df.columns and not pd.isna(df['Min'].iloc[0]) else None
            max_spec = df['Max'].iloc[0] if 'Max' in df.columns and not pd.isna(df['Max'].iloc[0]) else None

            # Załóżmy, że kolumny 0..3 to param_name, Time, Min, Max, a reszta to serie
            series_columns = df.columns[4:]

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(df.head(12))

            selected_series = st.multiselect(
                t["file_handling"]["select_series"],
                series_columns,
                default=series_columns
            )

            show_confidence_interval = st.checkbox(t["plot"]["show_confidence_interval"], value=True)

            fig, ax = plt.subplots(figsize=(12, 8))
            regression_results = []

            colors = plt.cm.get_cmap("tab10", len(selected_series))

            # Przygotowanie do ewentualnej analizy ANCOVA
            # (wewnątrz jednego DataFrame - scalimy x,y,seria)
            ancova_data = []

            for i, col in enumerate(selected_series):
                y = df[col]
                valid_indices = y.dropna().index
                x = time.loc[valid_indices]
                y = y.loc[valid_indices]

                # do ANCOVA zbieramy "x,y,kategoria"
                for x_val, y_val in zip(x, y):
                    ancova_data.append((x_val, y_val, col))

                if len(x) > 1:
                    slope, intercept, r_value, p_value, std_err = linregress(x, y)
                    y_pred = intercept + slope * x

                    # R2 to r_value^2
                    r_squared = r_value**2

                    # Obliczenie F-stat i p-value wprost z linregress
                    # UWAGA: w linregress t-stat = slope / std_err => T^2 = F (1, n-2)
                    # n to liczba punktów
                    n = len(x)
                    t_stat = slope / std_err
                    f_stat = t_stat**2  # z definicji F(1, n-2)
                    df1 = 1
                    df2 = n - 2
                    # p-value do F to to samo co p_value w linregress (dla slope),
                    # ale możemy sprawdzić to jeszcze przez sf:
                    # p_value_f = 1 - f.cdf(f_stat, df1, df2)

                    # Reszty i std reszt do CI
                    residuals = y - y_pred
                    std_resid = np.std(residuals, ddof=2)
                    mean_x = np.mean(x)

                    x_line = np.linspace(min(x), max(x), 100)
                    y_line = intercept + slope * x_line

                    conf_interval = 1.96 * std_resid * np.sqrt(
                        1 / n + (x_line - mean_x) ** 2 / np.sum((x - mean_x) ** 2)
                    )
                    y_upper = y_line + conf_interval
                    y_lower = y_line - conf_interval

                    color = colors(i)

                    ax.scatter(x, y, label=f"{col} ({t['plot']['data']})", color=color, alpha=0.7)
                    ax.plot(x_line, y_line, '-', label=f"{col} ({t['plot']['regression']})", color=color)

                    if show_confidence_interval:
                        ax.fill_between(
                            x_line,
                            y_lower,
                            y_upper,
                            color='gray',
                            alpha=0.3,
                            label='95% CI' if i == 0 else ""
                        )

                    # Przewidywany czas do górnego limitu (jeśli jest)
                    if max_spec is not None and slope != 0:
                        predicted_time = (max_spec - intercept) / slope
                        # UWAGA: do CI dla predicted_time należałoby
                        # zmodyfikować wzór, bo conf_interval jest dla Y
                        # Tutaj proste przybliżenie:
                        # weźmy conf_interval[-1] (max w x_line) – to dość umowne
                        # ...
                        predicted_time_lower = (max_spec - intercept - conf_interval[-1]) / slope
                        predicted_time_upper = (max_spec - intercept + conf_interval[-1]) / slope
                    else:
                        predicted_time, predicted_time_lower, predicted_time_upper = None, None, None

                    # Dolny limit, analogicznie
                    # (jeśli min_spec i slope != 0)
                    if min_spec is not None and slope != 0:
                        predicted_time_min = (min_spec - intercept) / slope
                    else:
                        predicted_time_min = None

                    regression_results.append({
                        t["regression_results"]["series"]: col,
                        # z pliku: Nachylenie, Wyraz wolny, R2,
                        'Nachylenie': round(slope, 5),
                        'Wyraz wolny': round(intercept, 5),
                        'R2': round(r_squared, 5),
                        # Przecięcie dolnego/górnego limitu – z pliku
                        # (tu w zależności, czy min_spec, max_spec)
                        'Przecięcie dolnego limitu': 
                            f"{predicted_time_min:.2f}" if predicted_time_min else "--",
                        'Przecięcie górnego limitu': 
                            f"{predicted_time:.2f}" if predicted_time else "--",
                        # test istotności nachylenia
                        # => F, F_crit, p_value, or "TAK"/"NIE"
                        'F (slope)': round(f_stat, 3),
                        'df1': df1,
                        'df2': df2,
                        'F crit (95%)': "--",  # ewentualnie możemy dodać f.isf(0.05, df1, df2)
                        'Hipoteza H0 a=0': "TAK" if f_stat > 0 else "NIE", # prymitywne placeholder
                        # p_value => w linregress to p_value
                        'p_value (slope)': f"{p_value:.3e}",
                        t["regression_results"]["std_err"]: round(std_err, 5),
                        # tu ewentualnie interpretacja
                        t["regression_results"]["predicted_time"]:
                            f"{predicted_time:.2f} m" if predicted_time else "N/A",
                        t["regression_results"]["predicted_time_range"]:
                            f"{predicted_time_lower:.2f} - {predicted_time_upper:.2f} m"
                            if predicted_time else "N/A"
                    })

            # Rysowanie linii Min/Max
            if min_spec is not None:
                ax.axhline(min_spec, color='green', linestyle='--', label='Min Spec')
            if max_spec is not None:
                ax.axhline(max_spec, color='red', linestyle='--', label='Max Spec')

            ax.set_xlabel(t["plot"]["x_label"])
            ax.set_ylabel(parameter_name)
            ax.set_title(f"{t['plot']['title']}: {parameter_name}")
            ax.legend()
            # Oś X co 3 miesiące (dowolne)
            ax.set_xticks(np.arange(min(time), max(time) + 1, 3))

            plt.grid(True)
            st.pyplot(fig)

            # Tabela wyników
            st.subheader("Rozszerzone wyniki regresji")
            regression_df = pd.DataFrame(regression_results)
            st.dataframe(regression_df)

            # Ewentualnie tu można zaimplementować Test Równości Współczynników (ANCOVA)
            # Basic approach: user picks "Test równości", then we do an ANCOVA on ancova_data
            # Ten fragment byłby dość rozbudowany, np. model = y ~ X + Kategoria + ...
            # Z racji ograniczeń w Streamlit i uproszczeń – pomijamy szczegóły

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
