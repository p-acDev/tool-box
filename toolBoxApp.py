import streamlit as st
import pandas as pd
import numpy as np
from app__interpolation import app__interpolation


st.set_page_config(
     page_title="Tool Box",
     page_icon=":hammer_and_wrench:",
     initial_sidebar_state="expanded",
     menu_items={
         'About': """## Documentation de l'app
         https://the-tool-box.readthedocs.io/en/latest/ 
          ## Développée par:
          pacourbet -> https://pierre-andre-courbet.gitbook.io/pac/informations/about"""
     }
 )

st.title(":hammer_and_wrench:Tool box")

## interpolation app
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

    with st.container():
        st.subheader("Interpolation")
        # to be chosen by user
        st.info("Application pour interpoler un jeu de donnéess")
        data = st.file_uploader("Upload raw data")

        if st.button("Interpoler") and data:

            df, df_interp = app__interpolation.do_interpolation(data)

            with st.expander("Clicker pour voir vos données"):
                st.dataframe(df)

            st.success("Voici votre interpolation")

            st.dataframe(df_interp)
            st.download_button(
                label="Download data as csv",
                data=df_interp.to_csv(),
                file_name="interpolated_data.csv")
                
