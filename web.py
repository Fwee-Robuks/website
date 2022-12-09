import streamlit as st
import requests
from streamlit_lottie import st_lottie
import os
from win10toast import ToastNotifier

st.set_page_config(page_title="", page_icon=":key:", layout="wide")

st.title("High Orbit Troll Cannon")

st.button("Break", on_click=print('Break'))

command = st.text_input("Command Prompt")

if command == "delete":
    toaster = ToastNotifier()
    toaster.show_toast("Critical Error!",
                   "We accidentally deleted system32, whoops!",
                   duration=10)
else:
    print("incorrect password!")

if command == "stop":
    os.system('taskkill /f /im python.exe')
