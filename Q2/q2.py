import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

st.title('Question 2: Vaccine Distributing Modeling')

df1_state1 = pd.read_csv('state1_centrecost.csv')
df2_state1 = pd.read_csv('state1_vacnum.csv')
df1_state2 = pd.read_csv('state2_centrecost.csv')
df2_state2 = pd.read_csv('state2_vacnum.csv')
df1_state3 = pd.read_csv('state3_centrecost.csv')
df2_state3 = pd.read_csv('state3_vacnum.csv')
df1_state4 = pd.read_csv('state4_centrecost.csv')
df2_state4 = pd.read_csv('state4_vacnum.csv')
df1_state5 = pd.read_csv('state5_centrecost.csv')
df2_state5 = pd.read_csv('state5_vacnum.csv')

st.write('State 1')
st.write(df1_state1)
st.write(df2_state1)

st.write('State 2')
st.write(df1_state2)
st.write(df2_state2)

st.write('State 3')
st.write(df1_state3)
st.write(df2_state3)

st.write('State 4')
st.write(df1_state4)
st.write(df2_state4)

st.write('State 5')
st.write(df1_state5)
st.write(df2_state5)
