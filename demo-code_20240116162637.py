print ("Streamlit Code")
import streamlit as st

# Add a title
st.title("My Streamlit App")

# Add some text
st.write("Welcome to my app!")

# Add a header
st.header("Some Data")

# Add a slider
age = st.slider("Select your age:", 0, 100, 25)

# Add a selectbox
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

# Add a button
if st.button("Submit"):
    st.write(f"Your age is {age} and your gender is {gender}.")
