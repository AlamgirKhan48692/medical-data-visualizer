import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title("Medical Data Visualizer 🩺")

df = pd.read_csv("medical_examination.csv")

# BMI calculation
df['overweight'] = (df['weight'] / (df['height']/100)**2) > 25

# Normalize cholesterol and glucose
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

st.subheader("Dataset Preview")
st.write(df.head())

# Correlation heatmap
corr = df.corr()

fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm")

st.subheader("Correlation Heatmap")
st.pyplot(fig)