import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from scipy.stats import ttest_ind
from utils.translations import translations

def calculate_f2(reference, test):
    """
    Oblicza współczynnik podobieństwa f2.
    """
    n = len(reference)
    sum_sq_diff = np.sum((reference - test) ** 2)
    #f2 = 50 * np.log10(1 + (1/n) * sum_sq_diff) * (-0.5)
    f2 = 50 * np.log10(100*((1 + (1/n) * sum_sq_diff) ** (-0.5)))
    f2 = abs(f2)
    return f2

def calculate_f1(reference, test):
    """
    Oblicza współczynnik różnicy f1.
    """
    abs_diff = np.abs(reference - test)
    f1 = (np.sum(abs_diff) / np.sum(reference)) * 100
    return f1

def show(language):
    t = translations[language]["dissolution_testing"]

    st.header(t["title"])

    st.write(f"""
    **{t["instructions"]["header"]}:**
    - {t["instructions"]["upload_file"]}
    - {t["instructions"]["select_groups"]}
    - {t["instructions"]["perform_analysis"]}
    - {t["instructions"]["view_results"]}
    """)

    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            if df.shape[1] < 3:
                st.error(t["file_handling"]["error_processing_file"])
                return

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(df.head(10))

            # Wybór kolumn do analizy
            reference_column = st.selectbox(t["file_handling"]["select_groups"], df.columns[1:], index=0)
            test_columns = st.multiselect(t["file_handling"]["select_groups"], df.columns[2:], default=df.columns[2:])

            if not test_columns:
                st.warning(t["warnings"]["need_two_groups"])
                return

            time = df.iloc[:, 0]
            reference = df[reference_column].dropna().to_numpy()

            f1_results = []
            f2_results = []

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(time, reference, marker='o', linestyle='-', label=f"{reference_column} (Ref)", color='black')

            for test_col in test_columns:
                test = df[test_col].dropna().to_numpy()
                f1_value = calculate_f1(reference, test)
                f2_value = calculate_f2(reference, test)

                f1_results.append((test_col, f1_value))
                f2_results.append((test_col, f2_value))

                ax.plot(time[:len(test)], test, marker='o', linestyle='--', label=f"{test_col} (Test)")

            ax.set_xlabel(t["plot"]["x_label"])
            ax.set_ylabel(t["plot"]["y_label"])
            ax.set_title(t["plot"]["title"])
            ax.legend()
            plt.grid(True)
            st.pyplot(fig)

            st.subheader(t["analysis_results"]["header"])
            results_df = pd.DataFrame({
                "Seria": [res[0] for res in f1_results],
                t["analysis_results"]["f1"]: [res[1] for res in f1_results],
                t["analysis_results"]["f2"]: [res[1] for res in f2_results]
            })

            st.dataframe(results_df)

            # Interpretacja wyników
            for _, row in results_df.iterrows():
                f2_value = row[t["analysis_results"]["f2"]]
                if f2_value >= 50:
                    st.success(f"{row['Seria']}: {t['analysis_results']['significant_result']}")
                else:
                    st.warning(f"{row['Seria']}: {t['analysis_results']['no_significant_result']}")

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
