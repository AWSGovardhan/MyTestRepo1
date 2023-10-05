import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('View New York Data'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['My Col1', 'My_Col2', 'MyCol3'])

    chart_data


if st.checkbox('View Chicago Data'):
    gen_details = pd.DataFrame(
        np.random.rand(10,2),
        columns=['C1',"C2"])
    gen_details 