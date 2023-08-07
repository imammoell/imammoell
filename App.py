import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("merge-csv.com__646494771c178.csv")
df = pd.DataFrame(data=df)

start = '2023-05-30' 
end = '2023-12-31'  
prices = pd.read_csv('merge-csv.com__646494771c178.csv')['Harga'][:216].values
date = pd.read_csv('merge-csv.com__646494771c178.csv')['date'][:216].values 

st.title("Penentu Masa Tanam")
st.write("masukan rencana tanggal tanam mu")

x = st.date_input("Select a date")


start_date = pd.to_datetime(x, errors='coerce', format='%Y-%m-%d') 
start_date = pd.to_datetime(start_date, errors='coerce', format='%Y-%m-%d').date()
start_date += pd.Timedelta('90 days')
new_date = pd.Timestamp(start_date).date()
start_date = new_date.strftime('%Y-%m-%d') 

start_date = pd.Timestamp(start_date).date()
start_date = np.datetime64(start_date)  
df['date'] = pd.to_datetime(df['date'])

offset = np.timedelta64(5, 'D') 
slice = df[(df['date'] >= start_date) & (df['date'] <= start_date + offset)]


max_harga = slice['Harga'].max()
max_date = slice.loc[slice['Harga'].idxmax(), 'date'].date()

y = slice['Harga'].max()
z = (slice.loc[slice['Harga'].idxmax(), 'date'] - pd.DateOffset(days=90)).date()
    

def streamlit() :
    st.write(f"Harga tertinggi: {y} pada tanggal {z}")
    st.write(f"Berdasarkan rencana tanggal tanam yang kamu pilih dan jangka waktu tanam dianggap 90 hari maka akan didapatkan harga terbaik pada {max_date} dengan harga {max_harga}")
    st.write("dan dapat dipetakan yaitu ")
    st.write(slice)
    st.write(f"90 hari sebelum tanggal {max_date} adalah {z}")

streamlit()

