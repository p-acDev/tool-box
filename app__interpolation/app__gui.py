import streamlit as st
from app__interpolation import app__interpolation

def create_gui():

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

    return None