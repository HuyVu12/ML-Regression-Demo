import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import matplotlib.pyplot as plt

np.random.seed(37)
st.set_page_config(layout="centered", page_title='Hello World!', page_icon='😶')

with st.sidebar:
    show_demo_data_frame = st.toggle("Data Frame Demo")
    show_demo_data_slider = st.toggle("Slider Demo")
    show_demo_data_LineChart = st.toggle("Line Chart Demo")
    show_demo_data_Help = st.toggle("Help Demo")
    show_demo_data_selectBox = st.toggle("Select Box Demo")
    show_demo_data_MultiselectBox = st.checkbox("MultiselectBox Demo")
    show_demo_uploadFile = st.toggle("Upload File Demo")
    demo_uploadFile02 = st.toggle("Upload a csv file Demo")
    demo_progress = st.toggle("Progress demo:")
    demo_form = st.toggle("Form Demo")

if show_demo_data_frame:
    st.header("DataFame")
    df = pd.DataFrame(
        {
            'Column 1': np.random.randint(0, 10, size = 10), 
            'Column 2': np.random.randint(0, 10, size = 10)
        }
    )
    st.write(df)

    arr = np.random.randn(200, 10)
    st.write(arr)

if show_demo_data_slider:
    st.header("Slider")
    my_date1 = st.slider('x1 = ', datetime(2025, 10, 3), datetime(2030, 1, 1))
    my_date2 = st.slider('x2 = ', 0, 100, format='hi %d')

    st.write(my_date1, my_date2)

if show_demo_data_LineChart:
    st.header("Line Chart")
    data2 = pd.DataFrame(
        # np.random.randint(0, 100, (30, 2)),
        np.random.randn(10, 2),
        columns=["A", "B"]
    )
    st.write(data2)
    st.line_chart(data2, color=['#ff0000', '#00ffdd'])

if show_demo_data_Help:
    st.header("Help")
    st.help(st.line_chart)

if show_demo_data_selectBox:
    st.header("Select Box")
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

if show_demo_data_MultiselectBox:
    st.header("Multiselect Box")
    m_select = st.multiselect(
        "What is your age?",
        range(1, 100)
    )

    st.write(m_select)
    for i in m_select:
        st.write(i)

#.streamlit/config.toml
st.write(st.secrets)

if show_demo_uploadFile:
    st.title("Upload File")
    upload_file = st.file_uploader("Select a file", type=["png", 'jpg', 'jfif'],accept_multiple_files=True)
    if upload_file:    
        for file in upload_file:
            st.write(f"""
        * file_id:{file.file_id}
        * name:{file.name}
        * size:{file.size}
        * _file_urls:{file._file_urls}
        """)

    import os
    os.makedirs('uploads', exist_ok=True)
    if upload_file is not None:
        for file in upload_file:
            file_path = os.path.join("uploads", file.name)
            with open(file_path, 'wb') as f:
                f.write(file.getbuffer())

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
        st.dataframe(list_file)
        # for file in files:
        #     path_image = os.path.join('uploads', file)
        #     st.image(path_image, width=300)

if demo_uploadFile02:
    file = st.file_uploader("Select a csv file", type=['csv'])
    
    if file is None: st.stop()
    st.write(file.type)
    df = pd.read_csv(file)
    select_remove = st.multiselect("Select filter", df.columns)
    df_review = pd.DataFrame()
    for col in df.columns:
        if col not in select_remove:
            df_review[col] = (df[col])
    # st.dataframe(df[selects] if len(selects) > 0 else df)
    st.dataframe(df_review, height=300)

with st.expander("Preview Data"):
    st.write("Demo Data Preview")
    df = pd.DataFrame(np.random.randn(20, 4), columns=['A', 'B', 'C', 'D'])
    st.dataframe(df)
    st.line_chart(df)

if demo_progress:
    my_progress = st.progress(0, 'Progress Hello World!')
    btn_start = st.button('Start 😆')
    if btn_start:
        for i in range(0, 100 + 1, 10):
            my_progress.progress(i, f'{i} %')
            time.sleep(1)
    
    with st.status('Running for something...'):
        for i in range(10):
            st.write(f'Running Process {i}')
            time.sleep(.2)
    with st.status('Running 2...'):
        st.write('ZZZ')
        time.sleep(1)
        st.write('ZZZ1')
        time.sleep(1)
        st.write('ZZZ2')
        time.sleep(1)
        st.write('ZZZ3')
        time.sleep(1)

if demo_form:
    with st.form('form login'):
        username = st.text_input('Username')
        password = st.text_input('Password')

        btn_submitted = st.form_submit_button('Login', type='primary')
    if btn_submitted:
        st.write(username, '-', password)
st.query_params
# st.help(st.query_params)

x = np.random.rand(100, 1)

plt.figure()
plt.plot(x, '.')
plt.grid(True)
st.pyplot(plt)