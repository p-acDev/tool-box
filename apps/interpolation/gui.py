import streamlit as st
from .main import do_interpolation

class Gui:

    def __init__(self, app__info):
        
        st.subheader(app__info["subheader"])
        st.info(app__info["info_desc"])

    def create(self):

        data = st.file_uploader("Upload raw data")

        if st.button("Interpoler") and data:

            df, df_interp = do_interpolation(data)

            with st.expander("Clicker pour voir vos données"):
                st.dataframe(df)

            st.success("Voici votre interpolation")

            st.dataframe(df_interp)
            st.download_button(
                label="Download data as csv",
                data=df_interp.to_csv(),
                file_name="interpolated_data.csv")

        return None