import streamlit as st

st.set_page_config(
    page_title="Deep Learning Training Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Multi-Page Navigation for Streamlit
pages = [
    st.Page("app2.py", title="DeepVision AI (CNN & XAI)", icon="🧠", default=True),
    st.Page("streamlittut.py", title="Streamlit Interactive Demo", icon="📊"),
]

pg = st.navigation(pages)
pg.run()
