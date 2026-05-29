# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# st.title("AutoEDA Platform")
# 
# uploaded_file = st.file_uploader(
#     "Upload CSV File",
#     type=["csv"]
# )
# 
# if uploaded_file:
# 
#     df = pd.read_csv(uploaded_file)
# 
#     st.subheader("Dataset Preview")
#     st.dataframe(df.head())
# 
#     st.subheader("Dataset Overview")
# 
#     st.write("Rows:", df.shape[0])
#     st.write("Columns:", df.shape[1])
# 
#     st.subheader("Missing Values")
# 
#     st.write(df.isnull().sum())
# 
#     st.subheader("Statistical Summary")
# 
#     st.dataframe(df.describe())
# 
#     st.subheader("Correlation Heatmap")
# 
#     numeric_df = df.select_dtypes(include=['number'])
# 
#     fig, ax = plt.subplots(figsize=(10,6))
# 
#     sns.heatmap(
#         numeric_df.corr(),
#         annot=True,
#         cmap="coolwarm",
#         ax=ax
#     )
# 
#     st.pyplot(fig)
# 
#     st.subheader("Generating Profile Report")
# 


!streamlit run app.py &>/dev/null&

from pyngrok import ngrok

ngrok.set_auth_token("3EPTnJA6pN3gZ9HCoLaDnigFSLR_QoLwZkpYNDHG84dF16ae")

!streamlit run app.py &>/dev/null&

from pyngrok import ngrok

public_url = ngrok.connect(8501)

print(public_url)
