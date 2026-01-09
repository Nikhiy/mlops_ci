import streamlit as st

st.title("power calculator")
st.write("enter a number to calculate its square,cube and fifth power")

n=st.number_input("enter a number",value=1,step=1)
square=n**2
cube=n**3
fifth_pwr=n**5

st.write(f"the square is {square}")
st.write(f"the cube is {cube}")
st.write(f"fifth power is {fifth_pwr}")

