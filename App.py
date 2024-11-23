import streamlit as st
st.title("My First App")
num = st.slider("Choose your number", 1, 100)
if st.button("Find"):
	st.write('square of ', num, 'is', num ** 2)