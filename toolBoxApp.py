import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import os
from apps.interpolation import gui as interp_gui
from apps.template import gui as temp_gui

with open("./info.json", "r", encoding="utf8") as f:
    info = json.load(f)

for f in os.listdir('.'):
    if os.path.isdir(f) and f.startswith('app__'):
        sys.path.append("./" + f)

st.set_page_config(menu_items = {
    "About": "Documentation de l'app https://the-tool-box.readthedocs.io/en/latest/ Développée par pacourbet https://pierre-andre-courbet.gitbook.io/pac/informations/about"
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

# TODO: use the importlib instead to import module by name
elif chosen_app == "Interpolation":

    with open(f"./apps/{chosen_app.lower()}/info.json","r", encoding='utf8') as f: 
        app__info = json.load(f)

    with st.container():

        app_gui = interp_gui.Gui(app__info)
        app_gui.create()

elif chosen_app == "Template":

    with open(f"./apps/{chosen_app.lower()}/info.json","r", encoding='utf8') as f: 
        app__info = json.load(f)

    with st.container():

        app_gui = temp_gui.Gui(app__info)
        app_gui.create()