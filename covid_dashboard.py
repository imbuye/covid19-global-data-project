import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("owid-covid-data.csv")
df = df[df['iso_code'].str.len() == 3]
df['date'] = pd.to_datetime(df['date'])

# Sidebar country selector
country = st.sidebar.selectbox("Select a Country", df['location'].unique())

# Filter data
country_df = df[df['location'] == country]

# Title
st.title(f"COVID-19 Dashboard: {country}")

# Line charts
fig1 = px.line(country_df, x='date', y='total_cases', title='Total Cases Over Time')
st.plotly_chart(fig1)

fig2 = px.line(country_df, x='date', y='total_deaths', title='Total Deaths Over Time')
st.plotly_chart(fig2)

fig3 = px.line(country_df, x='date', y='total_vaccinations', title='Total Vaccinations Over Time')
st.plotly_chart(fig3)
