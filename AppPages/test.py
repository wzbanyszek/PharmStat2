import streamlit as st
import requests

#import requests
#hostname = socket.gethostname()
#IPAddr = socket.gethostbyname(hostname)
#st.write("Your Computer Name is:" + hostname)
#st.write("Your Computer IP Address is:" + IPAddr)


def show(language):
  #URL = "https://httpbin.org/ip"
  
  #https://www.ipify.org/
  URL = "https://api.ipify.org?format=json"

  if st.button("Pobierz dane"):
    r = requests.get(URL)
    st.write(r)
    st.write(r.json())
