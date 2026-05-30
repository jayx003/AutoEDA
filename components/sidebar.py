import streamlit as st

def render_sidebar(df=None):

    st.sidebar.title(
        "AutoEDA: Automated Exploratory Data Analysis"
    )

    uploaded_file = st.sidebar.file_uploader(
        "Upload Your CSV File Here",
        type=["csv"]
    )

    if df is not None:

        st.sidebar.success("Dataset Uploaded")

        st.sidebar.write(f"Rows: {df.shape[0]}")
        st.sidebar.write(f"Columns: {df.shape[1]}")

    return uploaded_file