import streamlit as st
import pandas as pd

data = pd.DataFrame({'Home':['Own','Rented'],
                    'Vehicle':['Own',"Rented"],
                    'Status':["Yes",'No']})

home = st.selectbox('Your House is ',data['Home'])
'You live in your-',home,'-house!'

vehicle = st.selectbox('Your Vehicle is ',data['Vehicle'])
'Your have a vehicle which is - ',vehicle

status = st.selectbox('Your status as a US-Citizen is valid',data['Status'])
'You are a citizen of US? - ', status



