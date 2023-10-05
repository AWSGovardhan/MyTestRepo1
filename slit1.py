import streamlit as slit

#Creating a slider widget
v = slit.slider('Select a value ',0,50)

#Compute the square of the value 
square = v**2

#display the value and the square of the value
slit.write("Square of the value",v,' is ',square)

