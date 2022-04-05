import streamlit as st
import json
import os
import importlib

with open("./info.json", "r", encoding="utf8") as f:
    info = json.load(f)


st.set_page_config(menu_items = {
    "About": "Documentation de l'app https://the-tool-box.readthedocs.io/en/latest/ Développée par pacourbet https://www.pacourbet.net/"
     },
     )

st.title(info["header"])

chosen_app = st.sidebar.selectbox(
    "Selectionner l'app que vous voulez utiliser.",
    tuple(info["apps"])
)


if chosen_app == "-":
    ## Introduction
    with st.container():

        st.info("""
        Tool Box, une web app qui rassemble
        plusieurs outils comme l'interpolation, des fits de courbes,
        des distributions ...""")

else :

    with open(f"./apps/{chosen_app.lower()}/info.json","r", encoding='utf8') as f: 
        app__info = json.load(f)

    with st.container():

        app_gui = importlib.import_module(f'.{chosen_app.lower()}.gui' ,'.apps').Gui(app__info)
        app_gui.create()