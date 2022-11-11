import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Admin Page')
df = pd.read_csv('class.csv')
st.write(df)
values = st.slider('Please select a range of ID',0, 20, (1, 20))
st.write('Values selected: ', values)

BRANCH = df['BRANCH'].unique().tolist()
b_selection = st.multiselect('BRANCH:',
                                    BRANCH,
                                    default=BRANCH)

NAME = df['NAME'].unique().tolist()
N_selection = st.multiselect('NAME:',
                                    NAME,
                             default=NAME
                                    )

mask = (df['ID'].between(*values)) & (df['BRANCH'].isin(b_selection)) & (df['NAME'].isin(N_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')
col1, col2 = st.columns(2)
st.write(df[mask])

N1_selection = st.multiselect('NAME:',
                                    NAME,

                                    )
mask1 = (df['NAME'].isin(N1_selection))
number_of_result = df[mask1].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')
col1, col2 = st.columns(2)
st.write(df[mask1])
