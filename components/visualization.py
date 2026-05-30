import streamlit as st
import plotly.express as px

def render_visualizations(df, numeric_cols):

    st.title("Interactive Data Visualizations")

    # ============================================
    # HEATMAP
    # ============================================

    st.markdown("## 1. Correlation Heatmap")

    corr_matrix = df[numeric_cols].corr()

    heatmap_fig = px.imshow(
        corr_matrix,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r"
    )

    st.plotly_chart(
        heatmap_fig,
        use_container_width=True
    )

    st.markdown("---")

    # ============================================
    # HISTOGRAM
    # ============================================

    st.markdown("## 2. Interactive Histogram")

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    hist_fig = px.histogram(
        df,
        x=selected_col,
        nbins=30,
        title=f"Distribution of {selected_col}"
    )

    st.plotly_chart(
        hist_fig,
        use_container_width=True
    )

    st.markdown("---")

    # ============================================
    # BOXPLOT
    # ============================================

    st.markdown("## 3. Interactive Boxplot")

    box_fig = px.box(
        df,
        y=selected_col,
        title=f"Boxplot of {selected_col}"
    )

    st.plotly_chart(
        box_fig,
        use_container_width=True
    )

    st.markdown("---")

    # ============================================
    # SCATTER PLOT
    # ============================================

    st.markdown("## 4. Interactive Scatter Plot")

    x_axis = st.selectbox(
        "Select X-Axis",
        numeric_cols,
        key="x_axis"
    )

    y_axis = st.selectbox(
        "Select Y-Axis",
        numeric_cols,
        key="y_axis"
    )

    scatter_fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        hover_data=df.columns,
        title=f"{x_axis} vs {y_axis}"
    )

    scatter_fig.update_layout(
        height=600
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )
