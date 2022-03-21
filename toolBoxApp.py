from base64 import decode
import streamlit as st
import pandas as pd
import numpy as np
import json
from app__interpolation import app__interpolation, app__gui


st.set_page_config(
     page_title="Tool Box",
     page_icon=":hammer_and_wrench:",
     initial_sidebar_state="expanded",
     menu_items={
         'About': """Documentation de l'app
         https://the-tool-box.readthedocs.io/en/latest/ Développée par pacourbet https://pierre-andre-courbet.gitbook.io/pac/informations/about"""
     }
 )

st.title(":hammer_and_wrench:Tool box")

chosen_app = st.sidebar.selectbox(
    "Selectionner l'app que vous voulez utiliser.",
    ("-", "Interpolation", "Other")
)

if chosen_app == "-":
    ## Introduction
    with st.container():

        st.info("""
        Tool Box, une web app qui rassemble
        plusieurs outils comme l'interpolation, des fits de courbes,
        des distributions ...""")

elif chosen_app == "Interpolation":

    with open("./app__interpolation/app__info.json","r", encoding='utf8') as f: 
        app__info = json.load(f)

    with st.container():
        st.subheader(app__info["subheader"])
        # to be chosen by user
        st.info(app__info["info_desc"])
        
        app__gui.create_gui()
                
