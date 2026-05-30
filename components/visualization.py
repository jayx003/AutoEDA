import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_visualizations(df, numeric_cols):

    st.title("Data Visualizations")

    # ============================================
    # HEATMAP
    # ============================================

    st.markdown("## 1. Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap='coolwarm',
        linewidths=0.5,
        ax=ax
    )

    st.pyplot(fig)

    st.markdown("---")

    # ============================================
    # HISTOGRAM
    # ============================================

    st.markdown("## 2. Histogram")

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    fig2, ax2 = plt.subplots(figsize=(10, 5))

    sns.histplot(
        df[selected_col],
        kde=True,
        ax=ax2
    )

    ax2.set_title(f"Histogram of {selected_col}")

    st.pyplot(fig2)

    st.markdown("---")

    # ============================================
    # BOXPLOT
    # ============================================

    st.markdown("## 3. Boxplot")

    fig3, ax3 = plt.subplots(figsize=(10, 5))

    sns.boxplot(
        y=df[selected_col],
        ax=ax3
    )

    ax3.set_title(f"Boxplot of {selected_col}")

    st.pyplot(fig3)