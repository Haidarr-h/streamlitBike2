import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style='dark')

hour_df = pd.read_csv("https://raw.githubusercontent.com/Haidarr-h/streamlitBike/main/hour_df.csv")

workingday_season_df = hour_df[(hour_df['workingday'] == 1) & (hour_df['season'] == 3)]
result = workingday_season_df.groupby(by="hr").agg({"cnt": "sum", "casual": "sum", "registered": "sum"})
result = result.rename_axis("Jam").rename(columns={"cnt": "Jumlah Total", "casual": "Jumlah Casual", "registered": "Jumlah Registered"})

option = st.sidebar.selectbox(
    'Lihat Korelasi Penggunaan Sepeda',
    ('Jam dengan Jumlah Pengguna', 'Cuaca dengan Jumlah Pengguna', 'Musim dengan Jumlah Pengguna')
)

if option == 'Jam dengan Jumlah Pengguna':
    st.header("Number of bike usage per hour")
    
    
    st.subheader("Based on working day in Fall Season")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(result.index, result["Jumlah Casual"], marker="o", linewidth=2, color="#FF5733", label="Jumlah Casual")
    ax.plot(result.index, result["Jumlah Registered"], marker="o", linewidth=2, color="#72BCD4", label="Jumlah Registered")
    ax.set_title("Number of bike usage per hour in a working day in fall divided into user status", fontsize=15)
    ax.set_xlabel("Hour in a day", fontsize=10)
    ax.set_ylabel("Total Usage", fontsize=10)
    ax.set_xticks(np.arange(24))
    ax.set_xticklabels(np.arange(24), fontsize=10)
    ax.set_yticklabels(ax.get_yticks(), fontsize=10)
    ax.grid(True)

    ax.legend(fontsize=10)

    st.pyplot(fig)
    
    workingday_season_df = hour_df[(hour_df['workingday'] == 1) & (hour_df['season'] == 3)]
    result = workingday_season_df.groupby(by="hr").agg({"cnt": "sum", "casual": "sum", "registered": "sum"})
    result = result.rename_axis("Jam").rename(columns={"cnt": "Jumlah Total", "casual": "Jumlah Casual", "registered": "Jumlah Registered"})
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(result.index, result["Jumlah Total"], marker="o", linewidth=2, color="#72BCD4")
    ax.set_title("Number of bike usage per hour in a working day in fall", loc="center", fontsize=20)
    ax.set_xlabel("Hour in a day", fontsize=15)
    ax.set_ylabel("Total Usage", fontsize=15)
    ax.set_xticks(np.arange(24))
    ax.set_xticklabels(np.arange(24), fontsize=10)
    ax.set_yticklabels(ax.get_yticks(), fontsize=10)
    ax.grid(True)
    
    st.pyplot(fig)
    
    st.write("Kesimpulan informasi yang didapatkan berdasarkan data visualisasi dan explanatory analysis, yakni menunjukan pengaruh yang signifikan antara penggunaan sepeda dengan aspek waktu (jam) pada suatu hari. Ditunjukan bahwasannya puncak terbanyak peminjaman pada pukul 17 dimana diasumsikan waktu pulang kerja atau berkegiatan dan peminjaman terendah terjadi pada pukul 3.")
    
    


elif option == 'Cuaca dengan Jumlah Pengguna':


    day_df = pd.read_csv("https://raw.githubusercontent.com/Haidarr-h/streamlitBike/main/hour_df.csv")

    working_weather_day = day_df.groupby("weathersit")["cnt"].sum()
    working_weather_day.index = ["Clear", "Mist", "Rain", "Storm"]

    st.header("Number of bike usage affected by weather in a working day")

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(working_weather_day.index, working_weather_day, color="#72BCD4") 

    ax.set_title("Number of bike usage affected by weather in a working day", fontsize=20)
    ax.set_xlabel("Weather Condition", fontsize=15)
    ax.set_ylabel("Total Usage", fontsize=15)
    ax.set_xticklabels(working_weather_day.index, fontsize=10)
    ax.set_yticklabels(ax.get_yticks(), fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))

    st.pyplot(fig)
    st.write("Berdasarkan data yang divisualisasikan dan analisis yang telah dilakukan, terdapat pengaruh yang sangat signifikan dari faktor cuaca terhadap jumlah penggunaan sepeda. Di mana ditunjukan, cuaca clear atau cerah menunjukan penggunaan tertinggi, mist atau mendung menduduki peringkat kedua, dan hujan menduduki peringkat terakhir")

elif option == 'Musim dengan Jumlah Pengguna':
    st.header("Number of bike usage affected by season")
    
    day_df = pd.read_csv("https://raw.githubusercontent.com/Haidarr-h/streamlitBike/main/hour_df.csv")
    season_names = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

    season_counts = day_df.groupby(by="season").cnt.sum()
    season_counts.index = season_counts.index.map(season_names)

    plt.figure(figsize=(10, 6))
    season_counts.plot(kind='bar', color='skyblue')
    plt.title('Total Counts by Season')
    plt.xlabel('Season')
    plt.ylabel('Total Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt.gcf())
    
    st.write("Berdasarkan penggambaran visualisasi tersebut, terlihat bahwasannya musim panas, gugur, dan dingin merupakan musim yang diminati dalam penggunaan sepeda. Berbeda dengan musim semi yang cenderung berkurang cukup signifikan")
