import streamlit as st
from . import main


class Gui:

    def __init__(self, app__info):
        
        st.subheader(app__info["subheader"])
        st.info(app__info["info_desc"])

    def create(self):

        

        return None