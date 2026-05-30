import streamlit as st
import pandas as pd

# COMPONENT IMPORTS
from components.sidebar import render_sidebar
from components.overview import render_overview
from components.visualization import render_visualizations
from components.preprocessing import render_preprocessing
from components.landing import render_landing

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="AutoEDA",
    layout="wide"
)

# ============================================
# SIDEBAR
# ============================================

uploaded_file = render_sidebar()

# ============================================
# IF DATASET IS UPLOADED
# ============================================

if uploaded_file:

    # READ DATASET
    df = pd.read_csv(uploaded_file)

    # ============================================
    # INITIALIZE SESSION STATE
    # ============================================

    if "processed_df" not in st.session_state:

        st.session_state.processed_df = df.copy()

    # NUMERIC COLUMNS
    numeric_cols = df.select_dtypes(
        include=['number']
    ).columns

    # ============================================
    # UPDATE SIDEBAR WITH DATASET INFO
    # ============================================

    

    # ============================================
    # DOWNLOAD CLEANED DATASET
    # ============================================

    st.sidebar.markdown("---")

    st.sidebar.subheader("Download Dataset")

    csv = st.session_state.processed_df.to_csv(
        index=False
    )

    st.sidebar.download_button(
        label="Download Cleaned CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )

    # ============================================
    # MAIN TABS
    # ============================================

    overview_tab, viz_tab, preprocess_tab = st.tabs(
        [
            "Overview",
            "Visualizations",
            "Preprocessing"
        ]
    )

    # ============================================
    # OVERVIEW TAB
    # ============================================

    with overview_tab:

        render_overview(df)

    # ============================================
    # VISUALIZATION TAB
    # ============================================

    with viz_tab:

        render_visualizations(df, numeric_cols)

    # ============================================
    # PREPROCESSING TAB
    # ============================================

    with preprocess_tab:

        render_preprocessing(df)

# ============================================
# LANDING PAGE
# ============================================

else:

    render_landing()