import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
day_data = pd.read_csv(r'D:/UNS FORM/Perkuliahan duniawi/SEMESTER 5/bangkit/data/day.csv')

# Sidebar filters
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime(day_data['dteday'].min()))
end_date = st.sidebar.date_input("End Date", pd.to_datetime(day_data['dteday'].max()))

# Season and Weather filters
selected_season = st.sidebar.multiselect(
    "Select Season",
    options=day_data['season'].unique(),
    default=day_data['season'].unique()
)

selected_weather = st.sidebar.multiselect(
    "Select Weather Condition",
    options=day_data['weathersit'].unique(),
    default=day_data['weathersit'].unique()
)

# Apply filters
filtered_data = day_data[
    (pd.to_datetime(day_data['dteday']) >= pd.to_datetime(start_date)) &
    (pd.to_datetime(day_data['dteday']) <= pd.to_datetime(end_date)) &
    (day_data['season'].isin(selected_season)) &
    (day_data['weathersit'].isin(selected_weather))
]

# Dashboard title
st.title("Bike Sharing Usage Analysis - Interactive Dashboard")
st.write(f"Data from {start_date} to {end_date}")

# Pertanyaan 1: Bagaimana kondisi peminjaman sepeda berdasarkan musim?
st.subheader("Pertanyaan 1: Bagaimana kondisi peminjaman sepeda berdasarkan musim?")
season_data = filtered_data.groupby('season')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=season_data, ax=ax)
ax.set_title("Total Rentals per Season")
ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# Pertanyaan 2: Bagaimana pengaruh kondisi cuaca terhadap peminjaman sepeda?
st.subheader("Pertanyaan 2: Bagaimana pengaruh kondisi cuaca terhadap peminjaman sepeda?")
weather_data = filtered_data.groupby('weathersit')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weather_data, ax=ax)
ax.set_title("Total Rentals by Weather Condition")
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# Pertanyaan 3: Apakah suhu mempengaruhi jumlah peminjaman sepeda?
st.subheader("Pertanyaan 3: Apakah suhu mempengaruhi jumlah peminjaman sepeda?")
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=filtered_data, ax=ax)
ax.set_title("Temperature vs. Total Rentals")
ax.set_xlabel("Normalized Temperature")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# Analisis Lanjutan: Penggunaan sepeda berdasarkan hari kerja dan hari libur
st.subheader("Analisis Lanjutan: Penggunaan sepeda berdasarkan hari kerja dan hari libur")
workingday_data = filtered_data.groupby('workingday')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=workingday_data, ax=ax)
ax.set_title("Total Rentals by Working Day Status")
ax.set_xlabel("Working Day Status")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

# Analisis Lanjutan: Total Peminjaman per Bulan
st.subheader("Analisis Lanjutan: Total Peminjaman Sepeda per Bulan")
monthly_data = filtered_data.groupby('mnth')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
ax.plot(monthly_data['mnth'], monthly_data['cnt'], marker='o')
ax.set_title("Total Rentals per Month")
ax.set_xlabel("Month")
ax.set_ylabel("Total Rentals")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)
