import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_data = pd.read_csv('data/day.csv')  # Sesuaikan dengan path file Anda
day_data['dteday'] = pd.to_datetime(day_data['dteday'])  # Konversi kolom tanggal ke format datetime

# Menampilkan judul
st.title('Dashboard Peminjaman Sepeda')

# Menampilkan deskripsi
st.write('Visualisasi data peminjaman sepeda.')

#   menggunakan widget Streamlit
st.sidebar.subheader('Filter tanggal')
start_date = st.sidebar.date_input('Tanggal Mulai', day_data['dteday'].min())
end_date = st.sidebar.date_input('Tanggal Akhir', day_data['dteday'].max())

# Filter data berdasarkan rentang tanggal yang dipilih
filtered_data = day_data[(day_data['dteday'] >= pd.to_datetime(start_date)) & 
                         (day_data['dteday'] <= pd.to_datetime(end_date))]

# Visualisasi 1: Heatmap peminjaman sepeda berdasarkan musim dan kondisi cuaca
st.subheader('Rata-rata Peminjaman Sepeda Berdasarkan Musim dan Kondisi Cuaca ')

avg_peminjaman = filtered_data.groupby(['season', 'weathersit'])['cnt'].mean().unstack()

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(avg_peminjaman, annot=True, fmt=".1f", cmap="YlGnBu", 
            cbar_kws={'label': 'Rata-rata Jumlah Peminjaman'}, ax=ax)
ax.set_title('Rata-rata Peminjaman Sepeda Berdasarkan Musim dan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Musim')
st.pyplot(fig)

# Visualisasi 2: Pengaruh suhu terhadap pengguna casual dan registered (warna disesuaikan)
st.subheader('Pengaruh Suhu Terhadap Pengguna Casual dan Registered')

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', hue='season', palette='coolwarm', data=filtered_data, ax=ax)
ax.set_title('Pengaruh Suhu Terhadap Peminjaman Sepeda (Casual dan Registered)')
ax.set_xlabel('Suhu (Normalisasi)')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Visualisasi 3: Tren waktu peminjaman sepeda (tanpa filter warna khusus)
st.subheader('Tren Peminjaman Sepeda Sepanjang Waktu ')

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='dteday', y='cnt', data=filtered_data, ax=ax, color='b')
ax.set_title('Tren Peminjaman Sepeda dari Waktu ke Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)
