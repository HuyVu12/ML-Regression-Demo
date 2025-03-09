from turtle import up
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
np.random.seed(37)
st.set_page_config(layout="wide")

st.header("DataFame")

show_demo_data_frame = st.toggle("Show data frame?")
if show_demo_data_frame:
    df = pd.DataFrame(
        {
            'Column 1': np.random.randint(0, 10, size = 10), 
            'Column 2': np.random.randint(0, 10, size = 10)
        }
    )
    st.write(df)

    arr = np.random.randn(200, 10)
    st.write(arr)

st.header("Slider")
show_demo_data_slider = st.toggle("Show Slider?")
if show_demo_data_slider:
    my_date1 = st.slider('x1 = ', datetime(2025, 10, 3), datetime(2030, 1, 1))
    my_date2 = st.slider('x2 = ', 0, 100, format='hi %d')

    st.write(my_date1, my_date2)

st.header("Line Chart")
show_demo_data_LineChart = st.toggle("Show Line Chart?")
if show_demo_data_LineChart:
    data2 = pd.DataFrame(
        # np.random.randint(0, 100, (30, 2)),
        np.random.randn(10, 2),
        columns=["A", "B"]
    )
    st.write(data2)
    st.line_chart(data2, color=['#ff0000', '#00ffdd'])

st.header("Help")
show_demo_data_Help = st.toggle("Show Help?")
if show_demo_data_Help:
    st.help(st.line_chart)

st.header("Select Box")
show_demo_data_selectBox = st.toggle("Show Select Box?")
if show_demo_data_selectBox:
    option = st.selectbox(
        "Select Box", 
        [f"Box {i} 😶"for i in range(1, 10)]
    )

    data3 = pd.DataFrame(
        np.random.rand(20, 5), 
        columns='A B C D E'.split(),
    )
    st.dataframe(data3, height=100)

    selected_column = st.selectbox("Select column", data3.columns)
    st.write(selected_column)
    st.line_chart(data3, x = None, y=selected_column)

st.header("Multiselect Box")
show_demo_data_MultiselectBox = st.checkbox("Show MultiselectBox?")
if show_demo_data_MultiselectBox:
    m_select = st.multiselect(
        "What is your age?",
        range(1, 100)
    )

    st.write(m_select)
    for i in m_select:
        st.write(i)

#.streamlit/config.toml
st.write(st.secrets)

st.title("Upload File")
upload_file = st.file_uploader("Select a file", type=["png", 'jpg', 'jfif'])
if upload_file:    
    st.write(f"""
    * file_id:{upload_file.file_id}
    * name:{upload_file.name}
    * size:{upload_file.size}
    * _file_urls:{upload_file._file_urls}
    """)

import os
os.makedirs('uploads', exist_ok=True)
if upload_file is not None:
    file_path = os.path.join("uploads", upload_file.name)
    with open(file_path, 'wb') as f:
        f.write(upload_file.getbuffer())

    st.success(file_path)

files = os.listdir('uploads')
width_image = st.slider("Width image:", 1, 1000, 200, 10)
if files:
    list_file = [os.path.join('uploads', file) for file in files]
    st.image(list_file, width=width_image)
    df_image = pd.DataFrame(
        list_file, 
        columns=['File Path']
    )
    st.dataframe(df_image)
    # for file in files:
    #     path_image = os.path.join('uploads', file)
    #     st.image(path_image, width=300)
