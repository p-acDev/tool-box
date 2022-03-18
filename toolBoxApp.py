import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


st.set_page_config(
     page_title="Tool Box",
    #  page_icon="",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'About': "https://the-tool-box.readthedocs.io/en/latest/"
     }
 )

st.title("Tool box")

## interpolation app
chosen_app = st.sidebar.selectbox(
    "Selectionner l'app que vous voulez utiliser",
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

            df = pd.read_csv(data, sep=";")

            with st.expander("Clicker pour voir vos données"):
                st.dataframe(df)

            x, y = df['x'], df['y']

            # to be chosen by user
            x_new = np.arange(0, 360, 30)

            y_new = np.interp(x_new, x, y)

            # plt.plot(x, y, label="raw data")
            # plt.plot(x_new, y_new, label="interpolated")
            # plt.legend()
            # plt.xticks(x_new)
            # plt.grid()

            st.success("Voici votre interpolation")

            # st.pyplot(plt)

            df_interp = pd.DataFrame()
            df_interp["x"] = x_new
            df_interp["y"] = y_new

            st.dataframe(df_interp)
            st.download_button(
                label="Download data as csv",
                data=df_interp.to_csv(),
                file_name="interpolated_data.csv")
                