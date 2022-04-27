from numpy import histogram2d
import streamlit as st
from .utils import create_distibution, create_df
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

            direction_step = st.number_input("Taille d'incrément pour les directions",
            value=30.0)

            density = st.radio("Pour le téléchargement, voulez vous la distribution en densité",
            ("Non", "Oui"))

            if density == "Oui":
                density = True
            else:
                density = False

            if st.button("Créer distribution"):
                df = create_df(data, separator)
                histo = create_distibution(df, direction_step, density)
                

                fig = go.Figure(go.Histogram2d(
                    x=df[df.columns[1]],
                    y=df[df.columns[0]]
                ))
                fig.update_layout(
                    title_text=f'Distribution {data.name}',
                    xaxis_title=f'{df.columns[1]}',
                    yaxis_title=f'{df.columns[0]}',)
                st.plotly_chart(fig)

                with st.expander('Voir votre histogramme 2D'):
                    st.write(histo)
                st.download_button("Télécharger votre histogramme 2D",
                data=histo.to_csv())

        return None