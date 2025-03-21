import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
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

            parameter_name = df.iloc[0, 0]
            time = df['Time']
            min_spec = df['Min'].iloc[0] if not pd.isna(df['Min'].iloc[0]) else None
            max_spec = df['Max'].iloc[0] if not pd.isna(df['Max'].iloc[0]) else None
            series_columns = df.columns[4:]

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(df.head(12))

            selected_series = st.multiselect(t["file_handling"]["select_series"], series_columns, default=series_columns)

            show_confidence_interval = st.checkbox(t["plot"]["show_confidence_interval"], value=True)

            fig, ax = plt.subplots(figsize=(12, 8))
            regression_results = []

            colors = plt.cm.get_cmap("tab10", len(selected_series))

            for i, col in enumerate(selected_series):
                y = df[col]
                valid_indices = y.dropna().index
                x = time.loc[valid_indices]
                y = y.loc[valid_indices]

                if len(x) > 1:
                    slope, intercept, r_value, p_value, std_err = linregress(x, y)
                    y_pred = intercept + slope * x

                    residuals = y - y_pred
                    std_resid = np.std(residuals, ddof=2)
                    n = len(x)
                    mean_x = np.mean(x)

                    x_line = np.linspace(min(x), max(x), 100)
                    y_line = intercept + slope * x_line

                    conf_interval = 1.96 * std_resid * np.sqrt(1/n + (x_line - mean_x)**2 / np.sum((x - mean_x)**2))
                    y_upper = y_line + conf_interval
                    y_lower = y_line - conf_interval

                    color = colors(i)

                    ax.scatter(x, y, label=f"{col} ({t['plot']['data']})", color=color, alpha=0.7)
                    ax.plot(x_line, y_line, '-', label=f"{col} ({t['plot']['regression']})", color=color)

                    if show_confidence_interval:
                        ax.fill_between(x_line, y_lower, y_upper, color='gray', alpha=0.3, label='95% Przedział ufności' if i == 0 else "")

                    # Obliczanie przewidywanego okresu ważności
                    if max_spec is not None:
                        predicted_time = (max_spec - intercept) / slope
                        predicted_time_lower = (max_spec - intercept - conf_interval[-1]) / slope
                        predicted_time_upper = (max_spec - intercept + conf_interval[-1]) / slope
                    else:
                        predicted_time, predicted_time_lower, predicted_time_upper = None, None, None

                    regression_results.append({
                        t["regression_results"]["series"]: col,
                        t["regression_results"]["slope"]: round(slope, 3),
                        t["regression_results"]["intercept"]: round(intercept, 3),
                        t["regression_results"]["r_value"]: round(r_value, 3),
                        t["regression_results"]["p_value"]: f"{p_value:.3e}",
                        t["regression_results"]["std_err"]: round(std_err, 3),
                        t["regression_results"]["predicted_time"]: f"{predicted_time:.1f} miesięcy" if predicted_time else "N/A",
                        t["regression_results"]["predicted_time_range"]: f"{predicted_time_lower:.1f} - {predicted_time_upper:.1f} miesięcy" if predicted_time else "N/A"
                    })

            if min_spec is not None:
                ax.axhline(min_spec, color='green', linestyle='--', label=t['plot']['spec_limit'])
            if max_spec is not None:
                ax.axhline(max_spec, color='green', linestyle='--', label=t['plot']['spec_limit'])

            ax.set_xlabel(t["plot"]["x_label"])
            ax.set_ylabel(parameter_name)
            ax.set_title(f"{t['plot']['title']}: {parameter_name}")
            ax.legend()
            ax.set_xticks(np.arange(min(time), max(time) + 1, 3))

            plt.grid(True)
            st.pyplot(fig)

            st.subheader(t["regression_results"]["header"])
            regression_df = pd.DataFrame(regression_results)
            st.dataframe(regression_df)

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
