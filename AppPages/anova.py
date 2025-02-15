import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from utils.translations import translations

def show(language):
    t = translations[language]["anova_module"]

    st.header(t["title"])

    show_instructions = st.checkbox(t["show_instructions"], value=True)
    if show_instructions:
        st.write(f"""
        **{t["instructions"]["header"]}:**
        - {t["instructions"]["prepare_file"]}
        - {t["instructions"]["upload_file"]}
        - {t["instructions"]["select_groups"]}
        - {t["instructions"]["perform_anova"]}
        #- {t["instructions"]["interpretation"]}
        """)

    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            if df.shape[1] < 2:
                st.error(t["file_handling"]["error_two_columns"])
                return

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(df.head(10))

            # Wybór grup do analizy
            selected_groups = st.multiselect(
                t["file_handling"]["select_groups"],
                df.columns,
                default=df.columns
            )

            if len(selected_groups) < 2:
                st.warning(t["warnings"]["need_two_groups"])
                return

            # Przygotowanie danych do ANOVA
            data = [df[group].dropna() for group in selected_groups]

            # Wykonanie testu ANOVA
            stat, p_value = f_oneway(*data)

            st.subheader(t["anova_results"]["header"])
            st.write(f"{t['anova_results']['statistic']}: **{stat:.4f}**")
            st.write(f"{t['anova_results']['p_value']}: **{p_value:.4e}**")

            if p_value < 0.05:
                st.success(t["anova_results"]["significant_result"])
            else:
                st.warning(t["anova_results"]["no_significant_result"])

            # Wykres pudełkowy (boxplot)
            st.subheader(t["subheaders"]["boxplot"])
            df_melted = df[selected_groups].melt(var_name=t["boxplot"]["x_label"], value_name=t["boxplot"]["y_label"])
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df_melted[t["boxplot"]["x_label"]], y=df_melted[t["boxplot"]["y_label"]])
            plt.xticks(rotation=45)
            plt.grid(True)
            st.pyplot(plt.gcf())

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
