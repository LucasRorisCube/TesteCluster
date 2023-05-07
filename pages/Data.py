import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Temperatura")

# CSS to inject contained in a string
hide_table_row_index = """
                            <style>
                            thead tr th:first-child {display:none}
                            tbody th {display:none}
                            </style>
                            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

option_entity = st.radio('Options:', ('Spreadsheet', 'Chart'), horizontal=False)

df = pd.read_csv('data/temperaturas.csv')

if option_entity == 'Chart':
    dates = df.Data
    selected_data = st.selectbox("Select the desired date:",dates)
    if st.button('Go'):

        fig, ax = plt.subplots(facecolor='#0e1117')

        ax.plot(df.Temperature, df.Time,color='#800080')

        ax.set_title("Temperatures",color='white')
        ax.set_xticks(df.Temperature)
        ax.tick_params(axis='x',colors='white')
        ax.tick_params(axis='y',colors='white')
        st.pyplot(fig)
else:
    st.dataframe(df)

#myquery = { "_id": { "$regex": date } }