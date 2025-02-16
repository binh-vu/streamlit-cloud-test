import streamlit as st
from st_bridge import bridge, html

st.set_page_config(page_title="Python Chess Explorer", layout="wide")

data = bridge("my-bridge", default="")

st.markdown(
    """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">""",
    unsafe_allow_html=True,
)

html(
    """
 <button type="button" class="btn btn-primary" onClick="stBridges.send('my-bridge', 
 'prev')"> Prev </button>
 <button type="button" class="btn btn-primary" onClick="stBridges.send('my-bridge', 
 'next')">Next  </button>

"""
)

if data:
    st.text(data)
