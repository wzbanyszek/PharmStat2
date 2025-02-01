import streamlit as st
import pandas as pd
from scipy.stats import shapiro, skew, kurtosis
from utils.data_processing import calculate_descriptive_stats
from utils.translations import translations

def show(language):
    t = translations[language]

    st.header(t["descriptive_stats"])

    st.write(f"""
    **{t["instructions"]}:**
    - {t["upload_file_instruction"]}
    - {t["select_columns_instruction"]}
    - {t["stats_summary_instruction"]}
    - {t["normality_skew_kurtosis_instruction"]}
    """)

    # Wczytywanie pliku
    uploaded_file = st.file_uploader(t["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            # Podgląd danych z możliwością włączania i wyłączania
            show_data = st.checkbox(t["show_data_preview"], value=True)
            if show_data:
                st.write(f"**{t['data_preview']}**")
                st.dataframe(df.head())

            columns = df.columns.tolist()
            selected_columns = st.multiselect(
                t["select_columns"],
                columns,
                default=columns
            )

            if selected_columns:
                st.subheader(t["descriptive_stats"])
                stats = calculate_descriptive_stats(df[selected_columns])

                # Dodanie wyników testu normalności, skośności i kurtozy jako wierszy
                additional_stats = {}
                for column in selected_columns:
                    data = df[column].dropna()
                    stat, p_value = shapiro(data)
                    skewness = skew(data)
                    kurt = kurtosis(data)

                    additional_stats.setdefault(t["shapiro_p_value"], []).append(round(p_value, 4))
                    additional_stats.setdefault(t["skewness"], []).append(round(skewness, 2))
                    additional_stats.setdefault(t["kurtosis"], []).append(round(kurt, 2))

                # Konwersja dodatkowych wyników do DataFrame
                additional_stats_df = pd.DataFrame(additional_stats, index=selected_columns).T

                # Łączenie statystyk opisowych z dodatkowymi statystykami
                full_stats = pd.concat([stats, additional_stats_df])

                st.dataframe(full_stats)

        except Exception as e:
            st.error(f"{t['error_processing_file']}: {e}")
    else:
        st.info(t["no_file_uploaded"])
