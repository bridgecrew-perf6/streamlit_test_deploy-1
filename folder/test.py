import streamlit as st
from pathlib import Path
import pandas as pd
# df = pd.read_csv('pytube_eg.csv')
# st.write(df)

st.write('Test successful!!')
path_df = Path(__file__).parents[0]/ 'pytube_eg.csv'
st.write(path_df)
# 'GarretBurhennData/Garret_Burhenn_Pitches.csv'
df = pd.read_csv(path_df)
st.write(df)


reverse_target_word_index = np.load('reverse_target_word_index.npy',allow_pickle='TRUE').item()
target_word_index = np.load('target_word_index.npy',allow_pickle='TRUE').item()
reverse_source_word_index = np.load('reverse_source_word_index.npy',allow_pickle='TRUE').item()

print(reverse_target_word_index)
