import streamlit as st

import pandas as pd

st.title("Data Registeration")

df = pd.read_csv('class.csv')
#st.write(df)
st.header("Existing File")

st.write(df)

st.sidebar.header("Enter Details")

options_form = st.sidebar.form("options_form")

user_name = options_form.text_input("NAME")

#user_branch = options_form.text_input("BRANCH")
user_branch = options_form.selectbox("BRANCH",(' ','CSE','ECE','EEE','MECH','CIV'))

user_id = options_form.text_input("ID")
user_c = options_form.text_input("Contact")
user_ad = options_form.text_input("Address")
image_file = options_form.file_uploader("Upload Images", type=["png","jpg","jpeg"])

add_data = options_form.form_submit_button()



if add_data:
    new_data = {"NAME": user_name, "BRANCH": user_branch, "ID": int(user_id), "Contact": int(user_c) , "Address": user_ad , "Profile": image_file}

    df = df.append(new_data, ignore_index=True)
    df.to_csv("class.csv", index=False)

