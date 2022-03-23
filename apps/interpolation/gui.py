import streamlit as st
from .utils import do_interpolation

class Gui:

    def __init__(self, app__info):
        
        st.subheader(app__info["subheader"])
        st.info(app__info["info_desc"])

    def create(self):

        data = st.file_uploader("Upload raw data")

        if data is not None:

            separator = st.radio(
                "Sélectionner le séparateur (';' par défaut)",
                (';', ',', 'autre'))
            
            if separator == 'autre':
                separator = st.text_input('Séparateur:')


            if st.button("Interpoler"):

                df, df_interp = do_interpolation(data, separator)

                with st.expander("Clicker pour voir vos données"):
                    st.dataframe(df)

                st.success("Voici votre interpolation")

                st.dataframe(df_interp)
                st.download_button(
                    label="Download data as csv",
                    data=df_interp.to_csv(),
                    file_name="interpolated_data.csv")

        return None