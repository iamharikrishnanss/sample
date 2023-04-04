import streamlit as st
import pandas as pd
from PIL import Image
import os
main = pd.read_excel("../VISUALIZATION.xlsx")
st.dataframe(main)
set = st.selectbox("Choose the sheet which want to get your visualize: ", ('Select an option','Year-Count','Diversity among the participant','State-Count','Reason for Registration'))
if not set=='Select an option':
    if set == 'Year-Count':
        df = pd.read_excel('Intership1.xlsx', sheet_name=0)
        st.dataframe(df)
        st.subheader("Relationship")

        folder_path = "Year"
        for filename in os.listdir(folder_path):
            image = Image.open("Year/"+filename)
            st.image(image)


    elif set == 'Diversity among the participant':
        df = pd.read_excel('Intership1.xlsx', sheet_name=1)
        st.dataframe(df)
        st.subheader("Compositions")

        folder_path = "Diversity among the participants"
        for filename in os.listdir(folder_path):
            image = Image.open("Diversity among the participants/"+filename)
            st.image(image)

    elif set == 'State-Count':
        df = pd.read_excel('Intership1.xlsx', sheet_name=2)
        st.dataframe(df)
        # st.subheader("Compositions")

        folder_path = "State"
        for filename in os.listdir(folder_path):
            image = Image.open("State/"+filename)
            st.image(image)
    else:
        df = pd.read_excel('Intership1.xlsx', sheet_name=3)
        st.dataframe(df)
        # st.subheader("Compositions")

        folder_path = "Reason for Registration"
        for filename in os.listdir(folder_path):
            image = Image.open("Reason for Registration/"+filename)
            st.image(image)