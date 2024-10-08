import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_data = pd.read_csv('data/day.csv')  # Sesuaikan dengan file data yang ada

# Convert numeric columns to categorical labels
season_mapping = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
weather_mapping = {1: 'Cerah/Mendung', 2: 'Berkabut', 3: 'Hujan Ringan', 4: 'Hujan Lebat'}

day_data['season'] = day_data['season'].map(season_mapping)
day_data['weathersit'] = day_data['weathersit'].map(weather_mapping)

# Menampilkan judul
st.title('Dashboard Peminjaman Sepeda')

# Menampilkan deskripsi
st.write('Visualisasi data peminjaman sepeda sesuai pertanyaan bisnis yang diajukan.')

# Visualisasi 1: Heatmap peminjaman sepeda berdasarkan musim dan kondisi cuaca
st.subheader('Rata-rata Peminjaman Sepeda Berdasarkan Musim dan Kondisi Cuaca')

avg_peminjaman = day_data.groupby(['season', 'weathersit'])['cnt'].mean().unstack()

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(avg_peminjaman, annot=True, fmt=".1f", cmap="YlGnBu", 
            cbar_kws={'label': 'Rata-rata Jumlah Peminjaman'}, ax=ax)
ax.set_title('Rata-rata Peminjaman Sepeda Berdasarkan Musim dan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Musim')
st.pyplot(fig)

# Visualisasi 2: Pengaruh suhu terhadap pengguna casual dan registered
st.subheader('Pengaruh Suhu Terhadap Pengguna Casual dan Registered')

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', hue='season', data=day_data, ax=ax)
ax.set_title('Pengaruh Suhu Terhadap Peminjaman Sepeda (Casual dan Registered)')
ax.set_xlabel('Suhu (Normalisasi)')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Visualisasi 3: Tren waktu peminjaman sepeda
st.subheader('Tren Peminjaman Sepeda Sepanjang Waktu')

day_data['dteday'] = pd.to_datetime(day_data['dteday'])
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='dteday', y='cnt', data=day_data, ax=ax)
ax.set_title('Tren Peminjaman Sepeda dari Waktu ke Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)
