# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_data = pd.read_csv('data/day.csv')


# Dashboard Title
st.title("Bike Rentals Analysis Dashboard")

# Pertanyaan 1: Visualisasi penggunaan sepeda per musim
st.header("Average Bike Rentals by Season")
seasonal_avg_cnt = day_data.groupby('season')['cnt'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=seasonal_avg_cnt, ax=ax, palette='Blues_d')
ax.set_title('Average Bike Rentals by Season')
ax.set_xlabel('Season (1: Spring, 2: Summer, 3: Fall, 4: Winter)')
ax.set_ylabel('Average Bike Rentals')
st.pyplot(fig)

# Pertanyaan 2: Visualisasi penggunaan sepeda di hari kerja vs hari libur
st.header("Average Bike Rentals on Working Days vs Non-working Days")
workingday_avg_cnt = day_data.groupby('workingday')['cnt'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=workingday_avg_cnt, ax=ax, palette='coolwarm')
ax.set_title('Average Bike Rentals on Working Days vs Non-working Days')
ax.set_xlabel('Working Day (0: Non-working Day, 1: Working Day)')
ax.set_ylabel('Average Bike Rentals')
st.pyplot(fig)
