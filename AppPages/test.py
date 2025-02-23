import socket
import streamlit as st
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

st.write("Your Computer Name is:" + hostname)
st.write("Your Computer IP Address is:" + IPAddr)
