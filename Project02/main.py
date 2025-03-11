from turtle import width
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from my_model import calc_model, predict

st.set_page_config(page_icon='😶', page_title='Nothing', layout='wide')

session = st.session_state
if 'x' not in session: session['x'] = np.array([1, 1, 2, 4, 6])
if 'y' not in session: session['y'] = np.array([1, 2, 4, 2, 7])

st.header("ML Regression 😶")

# plt.figure()
# plt.plot(session['x'], session['y'], '.')


df = pd.DataFrame()
df['x'] = session['x']
df['y'] = session['y']
col1, col2, col3 = st.columns((1, 1, 1))
with col1:
    echo_plt = st.empty()
    with echo_plt:
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(session['x'], session['y'], '.')
        st.pyplot(fig)
with col2:
    with st.expander('Data information'):
        #file = st.file_uploader("Add file csv", type=['csv'])
        st.dataframe(df)
        with st.form('Form Data'):
            x_input = st.number_input('x value')
            y_input = st.number_input('y value')

            submit_btn = st.form_submit_button()
        if submit_btn:
            session['x'] = np.append(session['x'], [x_input])
            session['y'] = np.append(session['y'], [y_input])
            st.rerun()
with col3:
    with st.expander('Model information'):
        if 'model_arg' not in session: session['model_arg'] = ''
        model_arg = st.text_input('Edit Hyperparameter', value=session['model_arg'])
        if model_arg != session['model_arg']:  
            session['model_arg'] = model_arg  
            st.rerun()  
        if 'str_latex' not in session: session['str_latex'] = ''
        if 'str_latex_model' not in session: session['str_latex_model'] = ''
        val = session['model_arg'].split()
        session['str_latex'] = ''
        for i in range(len(val)):
            session['str_latex'] += f'\Phi_{i}x^{{{val[i]}}}'
            if i != len(val) - 1: session['str_latex'] += '+'
        
        session['str_latex'] += '=y'
        # st.write(session['model_arg'], str_latex)
        st.latex(
            session['str_latex']
        )
        if len(session['model_arg'].split()) != 0:
            if 'theta' not in session: session["theta"] = 0
            session["theta"] = calc_model(session['model_arg'], session['x'], session['y'])
            st.write(session["theta"])
            session['str_latex_model'] = ''
            for i in range(len(session["theta"])):
                session['str_latex_model'] += f'{session["theta"][i]}x^{{{val[i]}}}'
                if i != len(val) - 1: session['str_latex_model'] += '+'
            st.latex(session['str_latex_model'])
            plt.figure()
            plt.plot(session['x'], session['y'], '.')

            x_plot = np.linspace(min(session['x']), max(session['x']), 100)
            y_plot = [predict(session['model_arg'], session["theta"], xi) for xi in x_plot]

            mse = 0
            for i in range(len(session['y'])):
                yi = predict(session['model_arg'], session["theta"], session['x'][i])
                mse += (yi - session['y'][i])**2
            mse /= len(session['y'])
            plt.title(f'MSE = {mse}')

            plt.plot(x_plot, y_plot, 'r-')
            echo_plt.pyplot(plt)

