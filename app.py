import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Medical Data Visualizer", layout="wide")

st.title("🩺 Medical Data Visualizer")

# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader("📂 Upload Medical Dataset (CSV)", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(df.head())

    # -------- BMI --------
    df['overweight'] = (df['weight'] / (df['height']/100)**2) > 25

    # -------- NORMALIZATION --------
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
    df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

    # -------- HEATMAP --------
    st.subheader("🔥 Correlation Heatmap")

    corr = df.corr()

    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm", ax=ax)

    st.pyplot(fig)

    # -------- CATPLOT --------
    st.subheader("📊 Categorical Plot")

    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    fig2 = sns.catplot(
        x="variable",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="count"
    )

    st.pyplot(fig2)

else:
    st.info("👆 Upload a CSV file to start")
