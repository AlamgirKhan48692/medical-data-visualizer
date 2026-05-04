import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Medical Data Visualizer", layout="wide")

st.title("🩺 Medical Data Visualizer")

# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader("📂 Upload Medical Dataset (CSV)", type="csv")

if uploaded_file is not None:

    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Dataset Preview")
        st.dataframe(df.head())

        # -------- REQUIRED COLUMNS --------
        required_cols = [
            'age', 'height', 'weight', 'gender',
            'ap_hi', 'ap_lo', 'cholesterol', 'gluc',
            'smoke', 'alco', 'active', 'cardio'
        ]

        for col in required_cols:
            if col not in df.columns:
                st.error(f"❌ Missing column: {col}")
                st.stop()

        # -------- FORCE NUMERIC (FIX FOR PYARROW ERROR) --------
        for col in required_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        df = df.dropna()

        # -------- BMI --------
        df['overweight'] = (
            (df['weight'] / (df['height'] / 100) ** 2) > 25
        ).astype(int)

        # -------- NORMALIZATION --------
        df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0).astype(int)
        df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0).astype(int)

        # -------- HEATMAP --------
        st.subheader("🔥 Correlation Heatmap")

        corr = df.corr(numeric_only=True)

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm", ax=ax)

        st.pyplot(fig)

        # -------- CATPLOT (FIXED) --------
        st.subheader("📊 Categorical Plot")

        df_cat = pd.melt(
            df,
            id_vars=['cardio'],
            value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        )

        # 🔥 CRITICAL FIX (this removes pyarrow error)
        df_cat['value'] = df_cat['value'].astype(int)
        df_cat['cardio'] = df_cat['cardio'].astype(int)
        df_cat['variable'] = df_cat['variable'].astype(str)

        fig2 = sns.catplot(
            x="variable",
            hue="value",
            col="cardio",
            data=df_cat,
            kind="count",
            height=5,
            aspect=1
        )

        st.pyplot(fig2.fig)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

else:
    st.info("👆 Upload a CSV file to start")
