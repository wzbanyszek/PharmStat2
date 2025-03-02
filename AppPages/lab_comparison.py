import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, ttest_rel, levene, bartlett, wilcoxon, pearsonr, spearmanr
from utils.translations import translations

def show(language):
    t = translations[language]["lab_comparison"]

    st.header(t["title"])

    show_instructions = st.checkbox(t["show_instructions"], value=True)
    if show_instructions:
        st.write(f"""
        **{t["instructions"]["header"]}:**
        - {t["instructions"]["prepare_file"]}
        - {t["instructions"]["upload_file"]}
        - {t["instructions"]["select_columns"]}
        - {t["instructions"]["perform_tests"]}
        - {t["instructions"]["interpretation"]}
        """)

    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            if df.shape[1] != 2:
                st.error(t["file_handling"]["error_two_columns"])
                return

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(df.head(10))

            lab1, lab2 = df.columns

            # Test F-Snedecora (sprawdzenie równości wariancji)
            f_stat, f_p = bartlett(df[lab1].dropna(), df[lab2].dropna())  # lub levene()

            # Test t-Studenta dla próbek sparowanych (dokładność)
            t_stat, t_p = ttest_rel(df[lab1].dropna(), df[lab2].dropna())

            # Test Wilcoxona (dla danych nie spełniających normalności)
            wil_stat, wil_p = wilcoxon(df[lab1].dropna(), df[lab2].dropna())

            # Korelacja między wynikami
            pearson_corr, pearson_p = pearsonr(df[lab1].dropna(), df[lab2].dropna())
            spearman_corr, spearman_p = spearmanr(df[lab1].dropna(), df[lab2].dropna())

            # Wyświetlanie wyników testów statystycznych
            st.subheader(t["results"]["header"])
            st.write(f"{t['results']['f_test_stat']}: **{f_stat:.4f}**, p = **{f_p:.4e}**")
            st.write(f"{t['results']['t_test_stat']}: **{t_stat:.4f}**, p = **{t_p:.4e}**")
            st.write(f"{t['results']['wilcoxon_stat']}: **{wil_stat:.4f}**, p = **{wil_p:.4e}**")
            st.write(f"{t['results']['pearson_corr']}: **{pearson_corr:.4f}**, p = **{pearson_p:.4e}**")
            st.write(f"{t['results']['spearman_corr']}: **{spearman_corr:.4f}**, p = **{spearman_p:.4e}**")

            # Wizualizacja – Boxplot
            st.subheader(t["subheaders"]["boxplot"])
            df_melted = df.melt(var_name=t["boxplot"]["x_label"], value_name=t["boxplot"]["y_label"])
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df_melted[t["boxplot"]["x_label"]], y=df_melted[t["boxplot"]["y_label"]])
            plt.xticks(rotation=45)
            plt.grid(True)
            st.pyplot(plt.gcf())

            # Wizualizacja – Wykres porównujący wartości
            st.subheader(t["subheaders"]["scatter"])
            plt.figure(figsize=(8, 6))
            plt.scatter(df[lab1], df[lab2], alpha=0.7)
            plt.xlabel(lab1)
            plt.ylabel(lab2)
            plt.title(t["scatter"]["title"])
            plt.grid(True)
            st.pyplot(plt.gcf())

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
