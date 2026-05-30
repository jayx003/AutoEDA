import streamlit as st
import pandas as pd

def render_overview(df):

    st.title("Dataset Overview")

    # ============================================
    # DATASET PREVIEW
    # ============================================

    st.markdown("## 1. Dataset Preview")

    st.write(
        """
        This section provides an overview of your dataset.
        You can select the number of rows to display and
        inspect the dataset structure.
        """
    )

    # ROW SLIDER
    num_rows = st.slider(
        "Display Rows",
        min_value=1,
        max_value=len(df),
        value=5,
        step=1
    )

    # DISPLAY DATAFRAME
    st.dataframe(
        df.head(num_rows),
        use_container_width=True,
        height=350
    )

    st.markdown("---")

    # ============================================
    # DATASET METRICS
    # ============================================

    st.markdown("## 2. Dataset Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    st.markdown("---")

    # ============================================
    # MISSING VALUES
    # ============================================

    st.markdown("## 3. Missing Value Analysis")

    missing_df = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values
        }
    )

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    st.markdown("---")

    # ============================================
    # STATISTICAL SUMMARY
    # ============================================

    st.markdown("## 4. Statistical Summary")

    st.dataframe(
        df.describe(),
        use_container_width=True
    )