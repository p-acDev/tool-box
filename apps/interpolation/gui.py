from turtle import color
import streamlit as st
from .utils import do_interpolation
import plotly.graph_objects as go

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

                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=df['x'],
                        y=df['y'],
                        mode="markers+lines",
                        name="raw data",
                        line=dict(color="#4298f5")
                    )
                )

                fig.add_trace(
                    go.Scatter(
                        x=df_interp['x'],
                        y=df_interp['y'],
                        mode="markers+lines",
                        name="interpolated data",
                        line=dict(color="#f59342")
                    )
                )

                st.plotly_chart(fig)

                with st.expander("Clicker pour voir vos données interpolées"):
                    st.dataframe(df_interp)

                st.download_button(
                    label="Download data as csv",
                    data=df_interp.to_csv(),
                    file_name="interpolated_data.csv")

        return None