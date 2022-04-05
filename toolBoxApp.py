import streamlit as st
import json
import os
import importlib

with open("./info.json", "r", encoding="utf8") as f:
    info = json.load(f)


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

else :

    with open(f"./apps/{chosen_app.lower()}/info.json","r", encoding='utf8') as f: 
        app__info = json.load(f)

    with st.container():

        app_gui = importlib.import_module(f'.{chosen_app.lower()}.gui' ,'.apps').Gui(app__info)
        app_gui.create()


# custome css

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="www.pacourbet.net/" target="_blank">p-a.c</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)