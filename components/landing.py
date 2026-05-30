import streamlit as st

def render_landing():

    st.title("Welcome to AutoEDA")

    st.write(
        """
        Upload your CSV dataset and perform automated
        exploratory data analysis with interactive visualizations.
        """
    )

    st.markdown("---")

    # ============================================
    # KEY FEATURES
    # ============================================

    st.header("Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 📊 Interactive Exploration

        Explore datasets with:
        - Automated insights
        - Dataset previews
        - Statistical summaries
        """)

    with col2:
        st.markdown("""
        ### 📈 Stunning Visualizations

        Generate:
        - Heatmaps
        - Histograms
        - Boxplots
        - Correlation analysis
        """)

    with col3:
        st.markdown("""
        ### 🛠️ Effortless Processing

        Simplify:
        - Data understanding
        - Exploratory analysis
        - Dataset inspection
        """)

    st.markdown("---")

    # ============================================
    # WHO CAN USE
    # ============================================

    st.header("Who Can Use AutoEDA?")

    user_col1, user_col2 = st.columns(2)

    with user_col1:
        st.success("📊 Data Analysts")
        st.success("🔎 Data Scientists")

    with user_col2:
        st.success("🧐 Business Professionals")
        st.success("📈 Students & Educators")

    st.markdown("---")

    st.info(
        "Upload a CSV dataset from the sidebar to begin."
    )