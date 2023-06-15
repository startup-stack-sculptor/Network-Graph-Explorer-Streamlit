import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import plotly.graph_objs as go
from PIL import Image


# provide some info about the app
info = """
A web-based network graph explorer built with Streamlit to visualize and explore network graphs, enabling analysis and understanding of social connections, similar to platforms like LinkedIn or Facebook.
"""

with st.sidebar.expander("About this app"):
    st.write(info)

# Add a file uploader to the sidebar
uploaded_file = st.sidebar.file_uploader('', type=['csv'])

st.markdown(
    """
    <style>
    .font {
      font-size: 30px;
      font-family: 'Copper Black';
      color: #FF9633;
    }
    </style>
    """,
    unsafe_allow_html=True)

st.markdown('<p class="font">Upload your data and generate an interactive network graph instantly...</p>', unsafe_allow_html=True)
