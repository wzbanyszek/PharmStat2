import streamlit as st
import requests

#import requests
#hostname = socket.gethostname()
#IPAddr = socket.gethostbyname(hostname)
#st.write("Your Computer Name is:" + hostname)
#st.write("Your Computer IP Address is:" + IPAddr)

r = requests.get("https://httpbin.org/ip")
st.write(r.json())
