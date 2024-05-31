import streamlit as st 
import pandas as pd

# Initialize the list of phrases
if 'phrases' not in st.session_state:
    st.session_state.phrases = []

# Function to display and edit the list of phrases
def display_phrases():
    st.text_area("Edit Phrases", value="\n".join(st.session_state.phrases), height=200, key="phrases_input")

# Function to update the list of phrases from the text area
def update_phrases():
    st.session_state.phrases = st.session_state.phrases_input.split("\n")

# Function to sort the list of phrases
def sort_phrases():
    st.session_state.phrases.sort()

st.title("Edit and Sort Phrases")

# Display the phrases
display_phrases()

# Button to update the list of phrases
if st.button("Update List"):
    update_phrases()
    st.success("List updated!")

# Button to sort the list of phrases
if st.button("Sort List"):
    sort_phrases()
    st.success("List sorted!")

# Display the updated list of phrases
st.text_area("Updated Phrases", value="\n".join(st.session_state.phrases), height=200, key="updated_phrases", disabled=True)


