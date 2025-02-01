import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils.translations import translations

# Import klasy ImRControlChart i reguł z biblioteki SPC
from SPC import ImRControlChart, Rule01, Rule02, Rule03, Rule04, Rule05, Rule06, Rule07, Rule08

def show(language):
    t = translations[language]

    st.header(t["control_charts"])

    st.write(f"""
    **{t["how_to_use"]}:**
    - {t["upload_data"]}
      1. **{t["time_series"]}** (e.g., dates, sample IDs),
      2. **{t["values"]}** (numerical data).
    - {t["extra_columns"]}
    - **ImR Chart** ({t["individual_values"]}, {t["moving_range"]}).
    """)

    uploaded_file = st.file_uploader(
        t["choose_file"],
        type=["xlsx", "xls"]
    )

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            col_count = df.shape[1]
            if col_count < 2:
                st.error(t["error_two_columns"])
                return

            if col_count > 2:
                st.warning(f"{t["warning_extra_columns"]} {col_count}. {t["using_first_two"]}")

            df = df.iloc[:, :2]
            df.columns = [t["time_series"], t["values"]]

            show_data = st.checkbox(t["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["data_preview"])
                st.dataframe(df.head(10))

            df[t["time_series"]] = df[t["time_series"]].astype(str)
            df[t["values"]] = pd.to_numeric(df[t["values"]], errors='coerce')
            df.dropna(subset=[t["values"]], inplace=True)

            if df.empty:
                st.error(t["error_no_numeric_data"])
                return

            data_array = df[t["values"]].to_numpy().reshape(-1, 1)

            chart = ImRControlChart(
                data=data_array,
                xlabel=t["observation"],
                ylabel_top=t["individual_values"],
                ylabel_bottom=t["moving_range"]
            )

            chart.limits = True
            chart.append_rules([
                Rule01(), Rule02(), Rule03(), Rule04(),
                Rule05(), Rule06(), Rule07(), Rule08()
            ])

            normally_distributed = chart.normally_distributed(
                data=chart.value_I, significance_level=0.05
            )
            st.write(f"{t["normal_distribution_check"]} **{normally_distributed}**")

            chart.plot()
            fig = plt.gcf()
            st.pyplot(fig)

            show_I_data = st.checkbox(t["show_I_chart"], value=True)
            show_MR_data = st.checkbox(t["show_MR_chart"], value=True)

            if show_I_data:
                df_I = chart.data(0)
                st.write(f"**{t["I_chart_data"]}** (CL, UCL, LCL):")
                st.dataframe(df_I[["CL", "UCL", "LCL"]].reset_index(drop=True))

            if show_MR_data:
                df_MR = chart.data(1)
                st.write(f"**{t["MR_chart_data"]}** (CL, UCL, LCL):")
                st.dataframe(df_MR[["CL", "UCL", "LCL"]].reset_index(drop=True))

            st.write("---")
            st.write(f"{t["process_stable"]} **{chart.stable()}**")

        except Exception as e:
            st.error(f"{t["error_processing_file"]}: {e}")
    else:
        st.info(t["no_file_uploaded"])
