import streamlit as st
import requests

import pandas as pd
from io import BytesIO

#import requests
#hostname = socket.gethostname()
#IPAddr = socket.gethostbyname(hostname)
#st.write("Your Computer Name is:" + hostname)
#st.write("Your Computer IP Address is:" + IPAddr)


# Funkcja do konwersji DataFrame do pliku Excel
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def show(language):
  #URL = "https://httpbin.org/ip"
  
  #https://www.ipify.org/
  URL = "https://api.ipify.org?format=json"

  if st.button("Pobierz dane"):
    r = requests.get(URL)
    st.write(r)
    st.write(r.json())
    st.write(st.secrets["some_key"])


  # Wczytywanie pliku
  uploaded_file = st.file_uploader("Wybierz plik Excel", type=['xlsx', 'xls'])
  if uploaded_file:
      df = pd.read_excel(uploaded_file)
      st.write("Podgląd danych:")
      edited_df = st.data_editor(df)
  
      # Przycisk do pobrania zmodyfikowanego pliku
      df_xlsx = to_excel(edited_df)
      st.download_button(label='Pobierz zmodyfikowany plik Excel',
                         data=df_xlsx,
                         file_name='zmodyfikowany_plik.xlsx')
