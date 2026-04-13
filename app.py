import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Analiza Agentie Imobiliara")

st.write("Dashboard initial pentru analiza datelor imobiliare")

# citire date
df = pd.read_csv("data/sample_data.csv")

st.subheader("Preview date")
st.dataframe(df.head())

st.subheader("Statistici")
st.write(df.describe())