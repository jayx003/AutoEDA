import streamlit as st

def render_preprocessing(df):

    st.title("Data Preprocessing")

    # ============================================
    # REMOVE MISSING VALUES
    # ============================================

    st.markdown("## 1. Remove Missing Values")

    if st.button("Drop Missing Values"):

        st.session_state.processed_df = (
            st.session_state.processed_df.dropna()
        )

        st.success(
            f"""
            Missing values removed successfully.
            New shape:
            {st.session_state.processed_df.shape}
            """
        )

        st.dataframe(
            st.session_state.processed_df.head(),
            use_container_width=True
        )

    st.markdown("---")

    # ============================================
    # REMOVE DUPLICATES
    # ============================================

    st.markdown("## 2. Remove Duplicate Rows")

    if st.button("Remove Duplicates"):

        st.session_state.processed_df = (
            st.session_state.processed_df.drop_duplicates()
        )

        st.success(
            f"""
            Duplicates removed successfully.
            New shape:
            {st.session_state.processed_df.shape}
            """
        )

        st.dataframe(
            st.session_state.processed_df.head(),
            use_container_width=True
        )

    st.markdown("---")

    # ============================================
    # FILL MISSING VALUES
    # ============================================

    st.markdown("## 3. Fill Missing Values")

    fill_method = st.selectbox(
        "Select Fill Method",
        [
            "Mean",
            "Median",
            "Mode"
        ]
    )

    if st.button("Apply Fill Method"):

        filled_df = (
            st.session_state.processed_df.copy()
        )

        numeric_cols = filled_df.select_dtypes(
            include=['number']
        ).columns

        if fill_method == "Mean":

            filled_df[numeric_cols] = (
                filled_df[numeric_cols].fillna(
                    filled_df[numeric_cols].mean()
                )
            )

        elif fill_method == "Median":

            filled_df[numeric_cols] = (
                filled_df[numeric_cols].fillna(
                    filled_df[numeric_cols].median()
                )
            )

        elif fill_method == "Mode":

            filled_df = filled_df.fillna(
                filled_df.mode().iloc[0]
            )

        st.session_state.processed_df = filled_df

        st.success(
            f"Missing values filled using {fill_method}."
        )

        st.dataframe(
            st.session_state.processed_df.head(),
            use_container_width=True
        )